"""
Testa saidas do sistema.
"""

import textwrap

import pytest

from playwright.sync_api import sync_playwright

from common import monitor_dialogs, wait_for_output_content


@pytest.fixture(autouse=True)
def fail_on_console_errors(request):

    debug_msgs = []
    errors = []

    def _on_console(msg):
        if msg.type in ("debug", "error", "assert"):
            # TODO Melhorar isso fazendo mocks das chamadas http
            if 'XMLHttpRequest' not in msg.text and 'net::ERR_FAILED' not in msg.text:
                debug_msgs.append(msg.type + ": " + msg.text)

    def _on_page_error(exc):
        errors.append(exc)


    def attach(page):
        page.on("console", _on_console)
        page.on("pageerror", _on_page_error)

    # Disponibiliza para o teste, se quiser
    request.node.console_attach = attach
    request.node.debug_msgs = debug_msgs 
    request.node.errors = errors

    yield

    fails = debug_msgs + errors
    for msg in fails:
        print(f"{msg}")

    assert not fails, f"Fails: {fails}"



def test_saida_tarefa_concluida_com_sucesso(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e telas.
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(5): maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        SUCESSO = "Tarefa realizada com sucesso."
        wait_for_output_content(page, SUCESSO)

        output = page.locator("#output-content").inner_text()
        assert "Análise de código concluída sem erros de sintaxe." in output
        assert "Executando o código. Aguarde..." in output

        assert dialog_state["dialogs"] == []


def test_saida_tarefa_nao_concluida_com_nectar_nao_coletado(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)
        
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&fast=1")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(2): maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "Tarefa realizada com sucesso." not in output
        assert "Algum néctar não foi coletado." in output
        assert dialog_state["dialogs"] == []


def test_saida_tarefa_nao_concluida_com_nectar_na_colmeia(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0&c=2,1,2&fast=1")

        assert page.locator('.CodeMirror').is_visible()
        data = """
        maia.avance()
        maia.faça_mel()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "Tarefa realizada com sucesso." not in output
        assert "Alguma colmeia ainda tem néctar." in output
        assert dialog_state["dialogs"] == []


def test_sem_erro_no_console_da_janela_quando_falha_code_rules(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)


        page.goto("http://localhost:8000/?maia=1,1,0&fast=1")

        page.wait_for_function("() => document.getElementById('test-cases')")
        page.evaluate(
            """
            () => {
                document.getElementById('test-cases').innerHTML = "" +
                    "{'codeRules': [{'metric': 'codeLoopCount', 'op': '>=', 'value': 1, 'msg': 'Use loop.'}]}";
            }
            """
        )

        assert page.locator('.CodeMirror').is_visible()
        data = """
        print(1)
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert dialog_state["dialogs"] == []


def test_print42_editor(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0")

        assert page.locator('.CodeMirror').is_visible()

        data = 'print(42)'
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.click("#run-btn")
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert '42\n' in page.locator("#output-content").inner_text()
        assert dialog_state["dialogs"] == []


def test_print42_console(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000")

        page.locator("#console").click()
        page.keyboard.type("print(42)")
        page.keyboard.press("Enter")

        # A documentação do Playwright recomenda usar `expect..to_have_text` no
        # lugar de `inner_text`, mas isso não funcionou para mim.
        assert page.locator('//*[@id="console"]/pre[5]').is_visible()
        assert page.locator('//*[@id="console"]/pre[5]').inner_text() == '42'

        assert page.locator('//*[@id="console"]/pre[7]').is_visible()
        assert page.locator('//*[@id="console"]/pre[7]').inner_text() == '>>> '
        assert dialog_state["dialogs"] == []


def test_sem_erro_ao_girar_apos_coleta_automatica(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,3,0&gs=3,4&gs=1,5&cag=1&fast=1")

        page.wait_for_function("() => window.editor && typeof window.editor.setValue === 'function'")

        data = """
        maia.avance()
        maia.avance()
        maia.direita()

        maia.avance()
        maia.avance()
        maia.direita()

        maia.avance()
        maia.avance()
        maia.direita()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "KeyError" not in output
        assert dialog_state["dialogs"] == []


def test_erro_sintaxe(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(3):\n    maia.avance("""
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()

        output = page.locator("#output-content").inner_text()
        assert "SyntaxError: '(' was never closed" in output
        assert dialog_state["dialogs"] == []


def test_nectar_nao_coletado(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,3,0&gs=3,4&gs=1,5&cag=1&fast=1")
        page.wait_for_function("() => window.editor && typeof window.editor.setValue === 'function'")

        data = """
        maia.avance()
        maia.avance()
        maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "Falha ao analisar a saída: Algum néctar não foi coletado" in output
        assert dialog_state["dialogs"] == []


def test_nectar_nao_coletado(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,3,0&gs=3,4&gs=1,5&cag=1&fast=1")
        page.wait_for_function("() => window.editor && typeof window.editor.setValue === 'function'")

        data = """
        maia.avance()
        maia.avance()
        maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "Falha ao analisar a saída: Algum néctar não foi coletado" in output
        assert dialog_state["dialogs"] == []


def test_linhas_excedentes(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e telas.
        page.goto("http://localhost:8000/?maia=1,3,0&gs=2,3&cag=1")

        assert page.locator('.CodeMirror').is_visible()

        data = """
        maia.avance()
        maia.avance()
        maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        msg = "O código tem mais de 2 linhas, mas o limite é 2."
        tests = """
        {
            "codeRules": [
                { "metric": "codeLineCount", "op": "<=", "value": 2, "msg": '""" + msg + """'}
            ]
        }
        """
        page.evaluate('tests => {document.getElementById("test-cases").innerHTML = tests}', tests)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        FALHA = "Falha ao validar o código:"
        wait_for_output_content(page, FALHA)

        output = page.locator("#output-content").inner_text()
        assert "Tarefa realizada com sucesso." not in output
        assert FALHA in output
        assert msg in output
        assert dialog_state["dialogs"] == []
