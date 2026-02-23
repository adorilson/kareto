from browser import document, window, timer
from world import World
from renderer import Renderer
from entities import Abelha, Girassol


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
    g1 = Girassol(world, renderer, command_queue, x=3, y=4)
    g2 = Girassol(world, renderer, command_queue, x=5, y=4)
    g3 = Girassol(world, renderer, command_queue, x=6, y=4)

    return bee


bee = create_world()


# ----------------------------
# Executor da fila
# ----------------------------

def process_queue():
    global is_running

    if not command_queue:
        is_running = False
        return

    is_running = True

    command = command_queue.pop(0)
    command()

    # agenda próximo passo
    timer.set_timeout(process_queue, 500)

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

def run_code(event):
    global is_running

    if is_running:
        return  # impede execução simultânea

    code = editor.getValue()

    try:
        exec(code)
        process_queue()
    except Exception as e:
        window.alert(f"Erro: {e}")

document["run-btn"].bind("click", run_code)