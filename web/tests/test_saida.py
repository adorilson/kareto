"""
Testa saidas do sistema.
"""

import textwrap

from playwright.sync_api import sync_playwright

from common import monitor_dialogs


def test_saida_tarefa_concluida_com_sucesso():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        dialog_state = monitor_dialogs(page)
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&fast=1")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(5): maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        output = page.locator("#output-content").inner_text()
        assert "Análise de código concluída sem erros de sintaxe." in output
        assert "Executando o código. Aguarde..." in output
        assert "Tarefa concluída com sucesso!" in output
        assert dialog_state["dialogs"] == []


def test_print42_editor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        dialog_state = monitor_dialogs(page)
        page.goto("http://localhost:8000")

        assert page.locator('.CodeMirror').is_visible()

        data = 'print(42)'
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.click("#run-btn")

        assert page.locator("#output-content").inner_text() == '42\n'
        assert dialog_state["dialogs"] == []


def test_print42_console():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
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


def test_sem_erro_ao_girar_apos_coleta_automatica():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
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


def test_erro_sintaxe():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        dialog_state = monitor_dialogs(page)
        page.goto("http://localhost:8000")

        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(3):\n    maia.avance("""
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()

        output = page.locator("#output-content").inner_text()
        assert "SyntaxError: '(' was never closed" in output
        assert dialog_state["dialogs"] == []



