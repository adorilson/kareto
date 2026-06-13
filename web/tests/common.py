import pytest


TILE_SIZE = 65 #deveria vir de renderer.TILE_SIZE

def assert_ator(page, tile_selector, x, y, z_index, img_src=None):
    tile = page.locator(tile_selector)
    assert tile.is_visible()
    assert tile.get_attribute("style") == f"transform: translate({x*TILE_SIZE}px, {y*TILE_SIZE}px); z-index: {z_index};"
    if img_src:
        assert tile.locator("img").get_attribute("src") == img_src
    return tile


def wait_for_output_content(page, message):
    page.wait_for_function(f"""
        () => document.querySelector("#output-content").innerText
            .includes("{message}")
    """)


def monitor_dialogs(page):
    """Registra dialogs exibidos pela pagina e os dispensa automaticamente."""
    state = {"dialogs": []}

    def _on_dialog(dialog):
        state["dialogs"].append({"type": dialog.type, "message": dialog.message})
        dialog.dismiss()

    page.on("dialog", _on_dialog)
    return state


@pytest.fixture(autouse=True)
def fail_on_console_errors(request):
    messages = {
        "debug": [],
        "error": [],
        "log": [],
        "info": [],
    }

    def _on_console(msg):
        if msg.type not in messages:
            raise Exception(f"Console message of type {msg.type} not handled: {msg.text}")

        messages[msg.type].append(msg.text)

    def _on_page_error(exc):
        raise Exception(f"Page error: {exc}")

    def attach(page):
        page.on("console", _on_console)
        page.on("pageerror", _on_page_error)

    # Disponibiliza para o teste, se quiser
    request.node.console_attach = attach
    request.node.messages = messages

    yield

    for msg in messages["error"]:
        print(f"{msg}")

    assert not messages["error"], f"Errors: {messages['error']}"  
