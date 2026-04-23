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
queue_delay_ms = 500
auto_collect_delay_ms = 300

# ----------------------------
# Setup do mundo
# ----------------------------

world = World(8, 8)
renderer = Renderer(world)

def create_world(confs):
    global command_queue, is_running, coleta_automatica_de_girassol, queue_delay_ms, auto_collect_delay_ms
    command_queue = []
    is_running = False
    renderer.reset()
    # isso será algo pra vir na configuração da fase

    window.console.log("create_world: aplicando configuracoes")

    queue_delay_ms = 500
    auto_collect_delay_ms = 300
    if 'fast' in confs or 'test' in confs:
        queue_delay_ms = 0
        auto_collect_delay_ms = 0
        window.console.log("create_world: modo rapido habilitado")
    else:
        window.console.log(f"create_world: delays padrao (fila={queue_delay_ms}ms, coleta={auto_collect_delay_ms}ms)")

    world.girassois = []

    if 'cag' in confs:
        cag_value = confs['cag'][0]
        try:
            cag_value = int(cag_value)
        except ValueError, TypeError:
            pass
        coleta_automatica_de_girassol = bool(cag_value)
        window.console.log(f"create_world: coleta automatica={'ligada' if coleta_automatica_de_girassol else 'desligada'}")
    else:
        coleta_automatica_de_girassol = False
        window.console.log("create_world: coleta automatica=desligada (sem cag)")

    if 'maia' in confs:
        maia_coords = confs['maia'][0].split(',')
        x, y, direcao = int(maia_coords[0]), int(maia_coords[1]), int(maia_coords[2])
        maia = Abelha(world, renderer, command_queue, x=x, y=y, direcao=direcao)
        window.console.log(f"create_world: maia em ({x}, {y}) direcao={direcao}")
    else:
        window.console.log("create_world: sem maia na configuracao")

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
        window.console.log(f"create_world: girassois={len(world.girassois)}")
    else:
        window.console.log("create_world: sem girassois na configuracao")

    return maia

confs = parse_qs(document.location.search[1:])  # Ignora o '?'
valid_world_keys = {"maia", "gs", "cag"}
if confs and valid_world_keys.intersection(confs.keys()):
    window.console.log("confs: origem=querystring")
else:
    if confs:
        window.console.log("confs: querystring ignorada (sem chaves de mundo)")
    confs = document.getElementById("confs").textContent.strip()
    confs = ast.literal_eval(confs)
    window.console.log("confs: origem=documento")

initial_confs = {
    key: list(value) if isinstance(value, (list, tuple)) else [value]
    for key, value in confs.items()
}

try:
    maia = create_world(confs)
except Exception as e:
    sys.stderr = ErrorOutput()
    traceback.print_exc()

# ----------------------------
# Executor da fila
# ----------------------------

def verifica_girassol():
    for girassol in world.girassois:
        if girassol.posicao == maia.posicao:
            girassol.esconda()
            girassol.ativa = False


def _update_runtime_state():
    window.is_running = is_running
    window.command_queue_len = len(command_queue)


def _handle_command_error(error, repl=None):
    window.alert(f"Erro lógico: {str(error)}")
    command_queue.clear()
    window.console.log('TEM repl. inserindo coisas no repl após exceção' if repl is not None else 'nao tem repl. imprimindo traceback no painel de saída')
    if repl is not None:
        repl.trata_excecao()
    else:
        traceback.print_exc()


def _run_next_command(repl=None):
    global is_running

    command = command_queue.pop(0)
    try:
        command()
    except Exception as e:
        is_running = False
        _update_runtime_state()
        _handle_command_error(e, repl)
        return False

    if coleta_automatica_de_girassol:
        if auto_collect_delay_ms == 0:
            verifica_girassol()
        else:
            timer.set_timeout(verifica_girassol, auto_collect_delay_ms)

    return True


def process_queue(repl=None):
    global is_running

    if not command_queue:
        is_running = False
        _update_runtime_state()
        return

    is_running = True
    _update_runtime_state()

    if queue_delay_ms == 0:
        while command_queue:
            if not _run_next_command(repl):
                return

        is_running = False
        _update_runtime_state()
        return

    if not _run_next_command(repl):
        return

    timer.set_timeout(lambda: process_queue(repl), queue_delay_ms)

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
    maia.avance()
    maia.avance()
    maia.direita()
    maia.avance()

for _ in range(4):
    maia.avance()
    maia.avance()
    maia.esquerda()
    maia.avance()
"""
)

window.editor = editor

def limpa_output():
    document["output-content"].html = ""


def reset_scene(event=None):
    global maia, is_running, command_queue

    if is_running:
        command_queue.clear()
        is_running = False

    limpa_output()
    maia = create_world(initial_confs)


window.reset_scene = reset_scene


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

