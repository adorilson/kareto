import ast
import sys
import traceback

import interpreter
import browser
from browser import window, document, timer

from snapshot import SnapshotStatus, send_snapshot, send_interpreter_snapshot
from svg import estimate_time

FIRST_TIME = True
command_queue = []

editor = None

# O cÃ³digo inicial (carregado do CodeInsights)
code = document.getElementById("init").textContent.strip()


# O cÃ³digo de reset (carregado do CodeInsights)
reset_code = document.getElementById("reset").textContent.strip()


def inform(*args):
    document["status-info"].html = "".join(args)


# Redirecionamento de prints e exceções para a interface web
def escape_tags(text):
    return text.replace("<", "&lt;").replace(">", "&gt;")


class StdOutput:
    def write(self, *args):
        if args != ('\n',):
            args = (args[0] + '\n')

        document["turtle-print-output"].html += '<pre class="editor-output">' + escape_tags("".join(args)) + "</pre>"


class ErrorOutput:
    def write(self, *args):
        document["turtle-print-output"].html += '<pre class="error">' + escape_tags("".join(args)) + "</pre>"


def _write(*args):
    document["turtle-print-output"].html += '<span class="output">' + "".join(args) + "</span>"

def __write(*args):
    document["turtle-print-output"].html += '<span class="error">' + "".join(args) + "</span>"


sys.stdout = StdOutput()
sys.stderr = ErrorOutput()

def clear_print():
    document["turtle-print-output"].html = ""

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


init_editor()

def report_exception(e=None):
    """Show traceback in the output and send snapshot with error details"""
    if type(e) == Exception:
        sys.stderr.write("Erro inesperado. Parem as máquinas.\n")

    traceback.print_exc(limit=-1)
    tb = traceback.format_exc(limit=-1)

    code = document["editoraux"].value

    send_snapshot(code, SnapshotStatus.ERROR, tb)


def load_test_cases():
    # Proteção contra ausencia de id = test-cases
    test_cases = None
    try:
        test_cases = str(document.getElementById("test-cases").innerHTML).strip()
    except Exception as e:
        window.console.log('Não há elemento com id = test-cases')
        window.console.log(e)
        return

    if test_cases:
        try:
            test_cases = ast.literal_eval(test_cases)
            return test_cases
        except Exception as e:
            report_exception(e)
            return


def call_tests():
    window.console.log('Iniciando execução dos testes...')
    _code = document["editoraux"].value

    test_cases = load_test_cases()

    try:
        import validators
        validators.run_tests(test_cases)
        window.console.log('Testes concluídos sem erros.')
    except AssertionError as e:
        window.console.log(f'AssertionError durante execução dos testes: {str(e)}')
        msg = f'Falha ao analisar a saída: {str(e)}'
        sys.stderr.write(msg)
        send_snapshot(_code, SnapshotStatus.FAIL, msg)
    except Exception as e:
        window.console.log(f'Exception durante execução dos testes: {str(e)}')
        report_exception(e)
    else:
        print('Tarefa realizada com sucesso.')
        send_snapshot(_code, SnapshotStatus.SUCCESS, "")


def trigger_tests():
    turtle_canvas = document.getElementById('turtle-canvas')
    if not turtle_canvas:
        window.console.log('Não há elemento com id = turtle-canvas (svg)')
        return

    dur_sec = estimate_time(turtle_canvas.outerHTML)
    window.console.log(f'Estimativa de tempo para finalização das animações: {dur_sec} s')

    test_timeout = int(dur_sec * 750)
    window.console.log(f'Setando timeout para execução dos testes: {test_timeout} ms')
    timer.set_timeout(call_tests, test_timeout)


def run_code(ev):
    global FIRST_TIME

    ensure_editor_initialized()
    clear_print()
    if FIRST_TIME:
        FIRST_TIME = False
        inform("Importando o módulo turtle pela primeira vez e executando o código. Aguarde.")
    else:
        inform("Executando o código. Aguarde.")
    #document["run1"].class_name = "btn btn-xs btn-success"
    # delay to allow updated DOM with above text to be shown.
    #clear(ev)

    # Isso precisa ser redefinido por causa do REPL
    sys.stdout = StdOutput()
    sys.stderr = ErrorOutput()

    try:
        exec_code()

        # 10ms foi um tempo ótimo para SVG já estar pronto, embora ainda não
        # tenha terminado de ser processado.
        # Tanto pra programas de execução rápida # (apenas 2 linhas, por exemplo)
        # quando pra execuções mais demoradas
        # Pode ser que precise ser alterado no futuro
        # Vai setar apenas se não ouve erro durante exec_code
        timer.set_timeout(trigger_tests, 10)
    except Exception as e:
        report_exception(e)


def reset_the_code(ev):

    ensure_editor_initialized()
    if(browser.confirm("IrÃ¡ recomeÃ§ar o exercÃ­cio com o cÃ³digo inicialmente fornecido pelo professor. IrÃ¡ perder todas as alteraÃ§Ãµes que tenha realizado entretanto. Deseja mesmo continuar?")):
        editor.setValue(reset_code)

document["reset-btn"].bind("click", reset_the_code)




document["run-btn"].class_name = "btn btn-xs btn-default"
document["run-btn"].bind("click", run_code)


def exec_code():
    #_code = document["code"].value
    ensure_editor_initialized()
    delayed_clear()
    _code = editor.getValue()

    #para o cÃ³digo estar disponÃ­vel para o pedido AJAX
    document["editoraux"].value = document["code_header"].textContent + "\n" + _code

    try:
        import validators
        is_valid, message = validators.validate_code(_code, '<string>')
    except RuntimeError as e:
        window.console.log(f'Capturou RuntimeError on exec_code: {e}')
        msg = f'Falha ao analisar o código: {str(e)}'
        sys.stderr.write(msg)
        send_snapshot(_code, SnapshotStatus.FAIL, msg)
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
            send_snapshot(_code, SnapshotStatus.ERROR, message)
            return
        print('Análise de código concluída sem erros de sintaxe.')

    #print(_code)

#try:
    # executa o import e configurações antes do código principal para que as linhas nas
    # mensagens de erro realmente correspondam à linha do editor.
    exec("import turtle as tt \ntt.set_defaults(\n    turtle_canvas_wrapper = document['turtle-div']\n)")
    exec(_code)

    print('Executando o código. Aguarde...')
#except:
#    try:
#        traceback.print_exc(limit=1)
#    except:
#        print("could not print traceback")
    document["clear"].class_name = "btn btn-xs btn-danger"
    document["replay-scene"].class_name = "btn btn-xs btn-enabled"
    inform("")

def delayed_clear():
    from turtle import restart
    restart()
    inform("")
    document["run-btn"].class_name = "btn btn-xs btn-default"
    document["replay-scene"].class_name = "btn btn-xs btn-disabled"
    document["clear"].class_name = "btn btn-xs btn-danger"
    document["clear"].class_name = "hidden"

def clear(ev):
    global FIRST_TIME
    if FIRST_TIME:
        FIRST_TIME = False
        inform("Importing turtle module for the first time and processing; please wait")
        document["run-btn"].class_name = "btn btn-xs btn-default"
    # delay to allow updated DOM with above text to be shown.
    timer.set_timeout(delayed_clear, 1)

document["clear"].bind("click", clear)

def replay(ev):
    # importing turtle earlier slows down the loading
    # of this page
    from turtle import replay_scene
    replay_scene()

document["replay-scene"].bind("click", replay)

class Interpreter(interpreter.Interpreter):
    def handle_line(self, event=None):
        super().handle_line(event)
        content = self.get_content().strip()
        window.console.log("Entrada do usuário no REPL:", content)
        if content.endswith(">>>"):
            lines = [line.strip() for line in content.splitlines() if line.strip()]
            prev_line = ""
            for idx in range(len(lines) - 1, 0, -1):
                if lines[idx].endswith(">>>"):
                    prev_line = lines[idx - 1]
                    break

            has_error = ("Error:" in prev_line) or ("Exception:" in prev_line)
            result = 4 if has_error else 1
            details = prev_line if has_error else ""
            send_interpreter_snapshot(result, details = details, code=content)

    def focus(self, *args):
        sys.stdout = sys.stderr =  interpreter.Output(self)


Interpreter("console", globals=globals())


hide_loading_overlay_and_focus_on_top(250)
