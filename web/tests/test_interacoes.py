"""
Testa interações do usuário
"""

from time import sleep
import textwrap

from playwright.sync_api import sync_playwright



from web.tests.common import assert_ator
# Mudar para 
#import renderer.TILE_SIZE
TILE_SIZE = 65


def test_captura_automatica():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&gs=6,4")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=4, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=5, y=4, z_index=1, img_src="img/girassol.gif")
        g3      = assert_ator(page, '#actors > div:nth-child(4)', x=6, y=4, z_index=1, img_src="img/girassol.gif") 
        
        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(5): maia.avance()"""
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


def test_recomecar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=3,2&gs=4,3")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=3, y=2, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=4, y=3, z_index=1, img_src="img/girassol.gif")

        data = "maia.avance()"
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        sleep(1)

        assert abelha.is_visible()
        assert abelha.get_attribute("style") != f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"

        page.locator("#clear").click()
        sleep(1)

        assert abelha.get_attribute("style") == f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert g1.is_visible()
        assert g1.get_attribute("style") == f"transform: translate({3*TILE_SIZE}px, {2*TILE_SIZE}px); z-index: 1;"
        assert g2.is_visible()
        assert g2.get_attribute("style") == f"transform: translate({4*TILE_SIZE}px, {3*TILE_SIZE}px); z-index: 1;"


def test_recomecar_com_nectar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1&gs=4,3")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=4, y=3, z_index=1, img_src="img/girassol.gif")

        data = """
        maia.avance()
        maia.extraia_nectar()
        maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        sleep(2)

        assert abelha.is_visible()
        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=3, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert page.locator(
            f'#actors > div[style="transform: translate({3*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 0
        assert page.locator(
            f'#actors > div[style="transform: translate({4*TILE_SIZE}px, {3*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 1

        page.locator("#clear").click()
        sleep(1)

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=4, y=3, z_index=1, img_src="img/girassol.gif")
