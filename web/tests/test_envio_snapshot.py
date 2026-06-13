import pytest

from playwright.sync_api import sync_playwright
from playwright._impl._api_types import TimeoutError

from common import monitor_dialogs, wait_for_output_content, fail_on_console_errors

def assert_api_snapshot_response(response):
    status = response.value.status
    json = response.value.json()
    assert json["status"] == "ok", f"API response status not ok: {json}"
    assert status == 200, f"API call failed with status {status}"


def test_envio_snapshot(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e testes
        # pós-execução.
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=2,4")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()
        data = """maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        with page.expect_response("*codesnapshotweb.php*") as api:
            page.locator("#run-btn").click()

            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            SUCESSO = "Tarefa realizada com sucesso."
            wait_for_output_content(page, SUCESSO)
            assert dialog_state["dialogs"] == []

            status = api.value.status
            response = api.value.json()
            assert response["status"] == "ok", f"API response status not ok: {response}"
            assert status == 200, f"API call failed with status {status}"


def test_dupla_execucao_com_codigo_igual(request):
    """No caso de reexecução, com mesmo código e mesmo resultado, não deve ser
    feito novo envio de snapshot."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e testes
        # pós-execução.
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=2,4")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()
        data = """maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        SUCESSO = "Tarefa realizada com sucesso."
        with page.expect_response("*codesnapshotweb.php*") as api:
            page.locator("#run-btn").click()

            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            wait_for_output_content(page, SUCESSO)

        # Reexecutando para testar se é feito novo enviou ou não.
        with pytest.raises(TimeoutError):
            with page.expect_response("*codesnapshotweb.php*", timeout=2000) as api:
                page.locator("#run-btn").click()
                assert_api_snapshot_response(api)


def test_dupla_execucao_com_código_diferente(request):
    """No caso de reexecução, com mesmo resultado mas código diferente, deve ser
    feito novo envio de snapshot."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()

        request.node.console_attach(page)
        dialog_state = monitor_dialogs(page)

        # Com mudanças recentes, o teste passou a falhar com o fast=1 aqui.
        # Talvez devido os timers para processamentos da fila e testes
        # pós-execução.
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=2,4")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert page.locator('.CodeMirror').is_visible()
        data = """maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        SUCESSO = "Tarefa realizada com sucesso."
        with page.expect_response("*codesnapshotweb.php*") as api:
            page.locator("#run-btn").click()

            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            wait_for_output_content(page, SUCESSO)
            assert_api_snapshot_response(api)

        # Reexecutando para testar se é feito novo enviou ou não.
        data2 = """maia.avance()\nmaia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data2)
        with page.expect_response("*codesnapshotweb.php*") as api:
            page.locator("#run-btn").click()

            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            wait_for_output_content(page, SUCESSO)
            assert_api_snapshot_response(api)
