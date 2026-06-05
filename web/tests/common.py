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
