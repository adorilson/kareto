import sys
import traceback

import interpreter
from browser import document, window, timer, bind

from world import World
from renderer import Renderer
from entities import Abelha, Girassol


# Redirecionamento de prints e exceções para a interface web
def _write(*args):
    document["kareto-print-output"].html += "".join(args)


def __write(*args):
    document["kareto-print-output"].html += '<span class="error">' + "".join(args) + "</span>"


command_queue = []
is_running = False

# ----------------------------
# Setup do mundo
# ----------------------------

world = World(8, 8)
renderer = Renderer(world)

def create_world():
    global command_queue, is_running
    command_queue = []
    is_running = False
    renderer.reset()
    # isso será algo pra vir na configuração da fase
    bee = Abelha(world, renderer, command_queue, x=1, y=4)
    world.girassois = []
    world.girassois.append(Girassol(world, renderer, command_queue, x=3, y=4))
    world.girassois.append(Girassol(world, renderer, command_queue, x=5, y=4))
    world.girassois.append(Girassol(world, renderer, command_queue, x=6, y=4))

    return bee


bee = create_world()


# ----------------------------
# Executor da fila
# ----------------------------

def verifica_girassol():
    for girassol in world.girassois:
        if girassol.posicao == bee.posicao:
            girassol.esconda()
            girassol.ativa = False

def process_queue(repl=None):
    global is_running

    if not command_queue:
        is_running = False
        return

    is_running = True

    command = command_queue.pop(0)
    # Talvez isso deve ser ativado apenas quando código do editor estiver em execução, para evitar confusão com mensagens de debug do próprio sistema
    # ver também como o módulo logging pode ser integrado a isso
    # TODO print não está funcionando corretamente
    if repl is not None:
        sys.stdout = sys.stderr = interpreter.Output(repl)
    else:
        sys.stdout.write = _write
        sys.stderr.write = __write

    try:
        command()
    except Exception as e:
        # Limpa a fila para evitar comportamentos estranhos após erro
        # Isso precisa ser feito aqui pois assíncrono
        command_queue.clear() 
        is_running = False
        if repl is not None: #TODO melhorar isso, talvez criando um método específico para lidar com erros no repl
            repl.insert_cr()
            repl.insert_prompt()
            repl.cursor_to_end()
        else:
            window.alert('nao tem repl')
        window.alert(f"Erro: {str(e)}")
        raise e # levanta novamente para ser tratada no bloco de execução do código do usuário

    timer.set_timeout(verifica_girassol, 300)

    # agenda próximo passo
    timer.set_timeout(lambda: process_queue(repl), 500)

# ----------------------------
# CodeMirror 5 Setup
# ----------------------------

editor = window.CodeMirror.fromTextArea(
    document["editor"],
    {
        "lineNumbers": True,
        "mode": "python",
        "theme": "default",
        "indentUnit": 4,
    }
)

editor.setValue(
"""
for _ in range(4):
    bee.avance()
    bee.avance()
    bee.direita()
    bee.avance()

for _ in range(4):
    bee.avance()
    bee.avance()
    bee.esquerda()
    bee.avance()
"""
)

# ----------------------------
# Execução do código
# ----------------------------

@bind(document["run-btn"], "click")
def run_code(event):
    global is_running

    if is_running: # impede execução simultânea
        window.alert("O código já está em execução. Por favor, aguarde.")
        return  

    code = editor.getValue()

    try:
        exec(code)
    except Exception as e:
        window.alert(f"Erro ao analisar o código: \n\n{traceback.format_exc()}")
        traceback.print_exc()
        return

    process_queue()


class Interpreter(interpreter.Interpreter):
    def keypress(self, event):
        super().keypress(event)
        try:
            # Processa a fila de comandos após cada entrada do usuário
            process_queue(repl=self)
        except Exception as e:
            window.alert(f"Erro durante a execução do repl: \n\n{traceback.format_exc()}")
            traceback.print_exc()
            self.insert_cr()
            self.insert_prompt()
            self.cursor_to_end()


    def focus(elf, *args):
        pass

