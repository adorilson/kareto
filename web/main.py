import ast
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


class StdOutput:
    def write(self, *args):
        if args != ('\n',):
            args = (args[0] + '\n') 

        document["output-content"].html += '<pre class="editor-output">' + escape_tags("".join(args)) + "</pre>"


class ErrorOutput:
    def write(self, *args):
        document["output-content"].html += '<pre class="error">' + escape_tags("".join(args)) + "</pre>"


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
            conf_gs = gs.split(',')
            x, y = conf_gs[0], conf_gs[1]
            try:
                nectares = conf_gs[2]
            except:
                nectares = None
            gs = Girassol(world, renderer, command_queue, x=int(x), y=int(y), nectares=nectares)
            world.girassois.append(gs)

    return bee

confs = parse_qs(document.location.search[1:])  # Ignora o '?'
if not confs:
    confs = document.getElementById("confs").textContent.strip() 
    confs = ast.literal_eval(confs)

try:
    bee = create_world(confs)
except Exception as e:
    sys.stderr = ErrorOutput()
    traceback.print_exc()

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

    try:
        command()
    except Exception as e:
        window.alert(f"Erro lógico: {str(e)}")
        # Limpa a fila para evitar comportamentos estranhos após erro
        # Isso precisa ser feito aqui pois assíncrono
        command_queue.clear() 
        is_running = False
        if repl is not None: #TODO melhorar isso, talvez criando um método específico para lidar com erros no repl
            window.console.log('TEM repl. inserindo coisas no repl após exceção')
            repl.trata_excecao()
        else:
            window.console.log('nao tem repl. imprimindo traceback no painel de saída')
            traceback.print_exc()
            return

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


def limpa_output():
    document["output-content"].html = ""


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

    sys.stdout = StdOutput()
    try:
        limpa_output()
        exec(code)
    except SyntaxError as e:
        window.alert(f"Erro de sintaxe. Veja detalhes na área de Saída.")
        sys.stderr = ErrorOutput()
        traceback.print_exc()
        return

    sys.stderr = ErrorOutput()
    process_queue()


class Interpreter(interpreter.Interpreter):
    def keypress(self, event):
        super().keypress(event)
        try:
            # Processa a fila de comandos após cada entrada do usuário
            process_queue(repl=self)
        except Exception as e:
            self.trata_excecao(e)

    def trata_excecao(self):
        self.insert_cr()
        traceback.print_exc()
        self.insert_cr()
        self.insert_prompt()
        self.cursor_to_end()

    def focus(self, *args):
        sys.stdout = sys.stderr =  interpreter.Output(self)


Interpreter("console", globals=globals())

