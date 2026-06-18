"""
Testa saidas do sistema.
"""

import textwrap

import pytest

from playwright.sync_api import sync_playwright

from common import monitor_dialogs, wait_for_output_content, fail_on_console_errors


def test_saida_tarefa_concluida_com_sucesso(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e testes
        # pós-execução.
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

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

        NAO_ENVIO = "Código e status idênticos ao último enviado, não enviando snapshot."
        assert NAO_ENVIO not in request.node.messages["log"]

        # Reexecutando para testar se é feito novo enviou ou não.
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        wait_for_output_content(page, SUCESSO)

        assert NAO_ENVIO in request.node.messages["log"]


def test_saida_tarefa_nao_concluida_com_nectar_nao_coletado(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)
        
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(2): maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        NECTAR_NAO_COLETADO = "Algum néctar não foi coletado."
        wait_for_output_content(page, NECTAR_NAO_COLETADO)

        output = page.locator("#output-content").inner_text()
        assert "Tarefa realizada com sucesso." not in output
        assert dialog_state["dialogs"] == []


def test_saida_tarefa_nao_concluida_com_nectar_na_colmeia(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0&c=2,1,2&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()
        data = """
        maia.avance()
        maia.faça_mel()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        NECTAR_NAO_COLETADO = "Alguma colmeia ainda tem néctar."
        wait_for_output_content(page, NECTAR_NAO_COLETADO)

        output = page.locator("#output-content").inner_text()
        assert "Tarefa realizada com sucesso." not in output
        assert dialog_state["dialogs"] == []


def test_sem_erro_no_console_da_janela_quando_falha_code_rules(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)


        page.goto("http://localhost:8000/?maia=1,1,0&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


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
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


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
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


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
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


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

        FALHA = "Falha ao analisar a saída: Algum néctar não foi coletado."
        wait_for_output_content(page, FALHA)
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
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


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


def test_contagem_if(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()

        FALHA = "Falha ao validar o código:"
        SUCESSO = "Tarefa realizada com sucesso."

        msg = "O código deve conter pelo menos 1 estrutura condicional (if)."
        tests = """
        {
            "codeRules": [
                { "metric": "codeIfCount", "op": ">=", "value": 1, "msg": '""" + msg + """'}
            ]
        }
        """

        page.evaluate('tests => {document.getElementById("test-cases").innerHTML = tests}', tests)

        # Isso poderia ser dois testes separados, mas para evitar a demora do carregamento do ambiente,
        # coloquei os dois cenários aqui.

        # FALHA
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        wait_for_output_content(page, FALHA)

        output = page.locator("#output-content").inner_text()

        assert SUCESSO not in output
        assert FALHA in output
        assert msg in output

        # SUCESSO
        data = """
        if True:
            print(1)
        else:
            print(2)
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        wait_for_output_content(page, SUCESSO)

        output = page.locator("#output-content").inner_text()

        assert SUCESSO in output
        assert FALHA not in output
        assert msg not in output

        assert dialog_state["dialogs"] == []


def test_contagem_else(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()

        FALHA = "Falha ao validar o código:"
        SUCESSO = "Tarefa realizada com sucesso."

        msg = "O código deve conter pelo menos 1 instrução condicional else."
        tests = """
        {
            "codeRules": [
                { "metric": "codeElseCount", "op": ">=", "value": 1, "msg": '""" + msg + """'}
            ]
        }
        """

        page.evaluate('tests => {document.getElementById("test-cases").innerHTML = tests}', tests)

        # Isso poderia ser dois testes separados, mas para evitar a demora do carregamento do ambiente,
        # coloquei os dois cenários aqui.

        # FALHA
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        wait_for_output_content(page, FALHA)

        output = page.locator("#output-content").inner_text()

        assert SUCESSO not in output
        assert FALHA in output
        assert msg in output

        # SUCESSO
        data = """
        if True:
            print(1)
        else:
            print(2)
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        wait_for_output_content(page, SUCESSO)

        output = page.locator("#output-content").inner_text()

        assert SUCESSO in output
        assert FALHA not in output
        assert msg not in output

        assert dialog_state["dialogs"] == []


def test_saida_deve_ter_4_linhas(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        page.goto("http://localhost:8000/?maia=1,1,0&fast=1")
        page.wait_for_function(
            "() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()

        code = 'nome_invalido'
        code = textwrap.dedent(code)
        page.evaluate('code => {window.editor.setValue(code)}', code)
        page.locator("#run-btn").click()

        page.wait_for_function(
            "() => window.is_running === false && window.command_queue_len === 0")

        # Esperadas
        LINHA1 = 'Análise de código concluída sem erros de sintaxe.'
        LINHA2 = 'Traceback (most recent call last):'
        # r e \ para escapar as aspas do JavaScript
        LINHA3 = r'File \"<string>\", line 1, in <module>'
        LINHA4 = "NameError: name 'nome_invalido' is not defined"
        wait_for_output_content(page, LINHA1)
        wait_for_output_content(page, LINHA2)
        wait_for_output_content(page, LINHA3)
        wait_for_output_content(page, LINHA4)

        # 4 Linhas esperadas devem gerar 8 tags <pre> no output-content
        page.wait_for_function(
            "() => document.getElementById('output-content').children.length == 8")

        assert dialog_state["dialogs"] == []
