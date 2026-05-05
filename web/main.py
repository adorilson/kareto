import ast
import sys
import traceback
from urllib.parse import parse_qs

import interpreter
from browser import document, window, timer, bind

from snapshot import send_snapshot, send_interpreter_snapshot

from world import World
from renderer import Renderer
from entities import Abelha, Girassol, Direcao


editor = None

# O cÃ³digo inicial (carregado do CodeInsights)
code = document.getElementById("init").textContent.strip()


# O cÃ³digo de reset (carregado do CodeInsights)
reset_code = document.getElementById("reset").textContent.strip()

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


# Isso é manipulado quando o foco alterna entre editor e console interativo
sys.stdout = StdOutput()
sys.stderr = ErrorOutput()


command_queue = []
is_running = False
coleta_automatica_de_girassol = False
queue_delay_ms = 500
auto_collect_delay_ms = 300

has_exception = False


# ----------------------------
# Setup do ambiente de desenvolvimento
# ----------------------------

def init_editor():
    global editor
    if editor is not None:
        return

    editor = window.CodeMirror.fromTextArea(
        document["editor"],
        {
            "lineNumbers": True,
            "mode": "python",
            "theme": "default",
            "indentUnit": 4,
        }
    )
    editor.setValue(code)


def ensure_editor_initialized():
    if editor is None:
        init_editor()

def keep_focus_on_top():
    console_el = document.getElementById("console")
    if console_el:
        console_el.blur()
    document.body.focus()
    window.scrollTo(0, 0)


def hide_loading_overlay_and_focus_on_top(delay_ms=0):
    overlay = document.getElementById("loading-overlay")
    if not overlay:
        return

    def _hide():
        overlay.class_name = "hidden"

    if delay_ms > 0:
        timer.set_timeout(_hide, delay_ms)
    else:
        _hide()

    keep_focus_on_top()



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
        maia = Abelha(world, renderer, command_queue, x=x, y=y, direcao=Direcao(direcao))
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
    global has_exception
    has_exception = True
    command_queue.clear()
    window.console.log('TEM repl. inserindo coisas no repl após exceção' if repl is not None else 'nao tem repl. imprimindo traceback no painel de saída')
    if repl is not None:
        repl.trata_excecao()
    else:
        report_exception(error)


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


def limpa_output():
    document["output-content"].html = ""


def reset_scene(event=None):
    global maia, is_running, command_queue

    window.console.log('Resetando cena...')

    if is_running:
        command_queue.clear()
        is_running = False

    limpa_output()
    maia = create_world(initial_confs)





# ----------------------------
# Execução do código
# ----------------------------

#common
def report_exception(e=None):
    """Show traceback in the output and send snapshot with error details"""
    if type(e) == Exception:
        sys.stderr.write("Erro inesperado. Parem as máquinas.\n")

    traceback.print_exc(limit=-1)
    tb = traceback.format_exc(limit=-1)

    code = document["editoraux"].value

    send_snapshot(code, 4, tb)

# common
def load_test_cases():
    # Por enquanto, não há definição de "test_cases" para ambiente Kareto,
    # mas essa função é necessária para manter a compatibilidade com a estrutura
    # de testes. Ela pode ser expandida no futuro se quisermos adicionar casos de
    # teste específicos para o mundo do Kareto.
    global world
    return {'world': world}


# common
def call_tests():
    window.console.log('Iniciando execução dos testes...')
    _code = document["editoraux"].value

    test_cases = load_test_cases()

    sys.stdout = StdOutput()

    try:
        import validators
        validators.run_tests(test_cases)
        window.console.log('Testes concluídos sem erros.')
    except AssertionError as e:
        window.console.log(f'AssertionError durante execução dos testes: {str(e)}')
        msg = f'Falha ao analisar a saída: {str(e)}'
        sys.stderr.write(msg)
        send_snapshot(_code, 3, msg)
    except Exception as e:
        window.console.log(f'Exception durante execução dos testes: {str(e)}')
        report_exception(e)
    else:
        print('Tarefa realizada com sucesso.')
        send_snapshot(_code, 1, "")


# common
def trigger_tests():
    global is_running
    global has_exception

    if is_running:
        window.console.log('Código ainda em execução, aguardando para rodar os testes...')
        timer.set_timeout(trigger_tests, 1000)
        return

    if not has_exception:
        call_tests()


@bind(document["run-btn"], "click")
def run_code(event):
    global is_running

    if is_running: # impede execução simultânea
        window.alert("O código já está em execução. Por favor, aguarde.")
        return  

    _code = editor.getValue()

    #para o cÃ³digo estar disponÃ­vel para o pedido AJAX
    document["editoraux"].value = document["code_header"].textContent + "\n" + _code

    reset_scene()
    limpa_output()

    # Isso precisa ser redefinido por causa do REPL
    sys.stdout = StdOutput()
    sys.stderr = ErrorOutput()

    try:
        import validators
        is_valid, message = validators.validate_code(_code, '<string>')
    except RuntimeError as e:
        window.console.log(f'Capturou RuntimeError on exec_code: {e}')
        msg = f'Falha ao analisar o código: {str(e)}'
        sys.stderr.write(msg)
        send_snapshot(_code, 3, msg)
        return
    except SyntaxError as e:
        window.console.log(f'Capturou SyntaxError on exec_code: {e}')
        report_exception(e)
        return
    except Exception as e:
        window.console.log(f'Capturou Exception on exec_code: {e}')
        report_exception(e)
        return
    else:
        if not is_valid:
            print(message)
            _code = document["editoraux"].value
            send_snapshot(_code, 4, message)
            return
        print('Análise de código concluída sem erros de sintaxe.')

    exec(_code)
    print('Executando o código. Aguarde...')
    global has_exception
    has_exception = False
    process_queue()
    trigger_tests()


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


def start_ambiente():
    window.console.log('Iniciando ambiente interativo...')
    Interpreter("console", globals=globals())

    ensure_editor_initialized()
    hide_loading_overlay_and_focus_on_top(250)

    window.reset_scene = reset_scene
    window.reset_code = reset_code
    window.editor = editor


# Chamar no final para garantir que tudo esteja definido antes de iniciar o ambiente
# mover a chamada para o cliente
start_ambiente()
