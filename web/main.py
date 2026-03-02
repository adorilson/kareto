import sys
import traceback
from urllib.parse import parse_qs

import interpreter
from browser import document, window, timer, bind

from world import World
from renderer import Renderer
from entities import Abelha, Girassol


# Redirecionamento de prints e exceções para a interface web
def escape_tags(text):
    return text.replace("<", "&lt;").replace(">", "&gt;")


def _write(*args):
    document["output-content"].html += escape_tags("".join(args))


def __write(*args):
    document["output-content"].html += '<pre class="error">' + escape_tags("".join(args)) + "</pre> <br/><br/>"


command_queue = []
is_running = False
coleta_automatica_de_girassol = False

# ----------------------------
# Setup do mundo
# ----------------------------

world = World(8, 8)
renderer = Renderer(world)

def create_world(confs):
    global command_queue, is_running, coleta_automatica_de_girassol
    command_queue = []
    is_running = False
    renderer.reset()
    # isso será algo pra vir na configuração da fase

    world.girassois = []

    if 'cag' in confs:
        cag_value = confs['cag'][0]
        try:
            cag_value = int(cag_value)
        except ValueError, TypeError:
            pass
        coleta_automatica_de_girassol = bool(cag_value)

    if 'bee' in confs:
        bee_coords = confs['bee'][0].split(',')
        x, y, direcao = int(bee_coords[0]), int(bee_coords[1]), int(bee_coords[2])
        bee = Abelha(world, renderer, command_queue, x=x, y=y, direcao=direcao)

    if 'gs' in confs:
        for i, gs in enumerate(confs['gs']):
            x, y = gs.split(',')
            world.girassois.append(Girassol(world, renderer, command_queue, x=int(x), y=int(y)))

    return bee

confs = parse_qs(document.location.search[1:])  # Ignora o '?'
bee = create_world(confs)


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

    if coleta_automatica_de_girassol:
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

