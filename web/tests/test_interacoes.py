"""
Testa interações do usuário
"""

from time import sleep

from playwright.sync_api import sync_playwright


# Mudar para 
#import renderer.TILE_SIZE
TILE_SIZE = 65


def test_captura_automatica():
    def assert_ator(tile_selector, x, y, z_index, img_src):
        tile = page.locator(tile_selector)
        assert tile.is_visible()
        assert tile.get_attribute("style") == f"transform: translate({x*TILE_SIZE}px, {y*TILE_SIZE}px); z-index: {z_index};"
        assert tile.locator("img").get_attribute("src") == img_src
        return tile

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?bee=1,4,0&cag=1&gs=3,4&gs=5,4&gs=6,4")

        abelha = assert_ator('#actors > div:nth-child(1)', x=1, y=4, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator('#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        g2 = assert_ator('#actors > div:nth-child(3)', x=5, y=4, z_index=1, img_src="img/girassol.gif")
        g3 = assert_ator('#actors > div:nth-child(4)', x=6, y=4, z_index=1, img_src="img/girassol.gif") 
        
        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(5): bee.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()

        sleep(3)

        # nova posicao da abelha
        x, y = 6, 4
        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({x*TILE_SIZE}px, {y*TILE_SIZE}px); z-index: 3;"

        assert g1.is_hidden()
        assert g2.is_hidden()
        assert g3.is_hidden()



def test_print42_editor():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        assert page.locator('.CodeMirror').is_visible()

        data = 'print(42)'
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.click("#run-btn")

        assert page.locator("#output-content").inner_text() == '42\n'


def test_print42_console():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
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
