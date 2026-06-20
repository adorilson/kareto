
from playwright.sync_api import sync_playwright

from common import assert_ator

TILE_SIZE = 65 #deveria vir de renderer.TILE_SIZE
    

def test_renderer_atores():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1&gsp=3,2,2&n=4,1&np=2,2&c=1,2")

        page.wait_for_function("() => document.querySelectorAll('#actors > div').length >= 1")

        # Abelha
        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert abelha.locator('.actor-value').inner_text() == ''

        x_px = 1 * TILE_SIZE
        y_px = 1 * TILE_SIZE
        assert abelha.evaluate(f"el => el.style.transform.includes('translate({x_px}px, {y_px}px)')")
        assert abelha.evaluate("el => el.style.zIndex == '3'")

        assert abelha.locator('img').evaluate("img => img.style.width") == '80%'
        assert abelha.locator('img').evaluate("img => img.style.height") == '80%'

        # Girassol
        girassol = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        assert girassol.locator('.actor-value').inner_text() == ''

        x_px = 2 * TILE_SIZE
        y_px = 1 * TILE_SIZE
        assert girassol.evaluate(f"el => el.style.transform.includes('translate({x_px}px, {y_px}px)')")
        assert girassol.evaluate("el => el.style.zIndex == '1'")

        assert girassol.locator('img').evaluate("img => img.style.width") == '80%'
        assert girassol.locator('img').evaluate("img => img.style.height") == '80%'


        # Girassol Persistente
        girassolpersist = assert_ator(page, '#actors > div:nth-child(3)', x=3, y=2, z_index=1, img_src="img/girassol.gif")
        assert girassolpersist.locator('.actor-value').inner_text() == '2'

        x_px = 3 * TILE_SIZE
        y_px = 2 * TILE_SIZE
        assert girassolpersist.evaluate(f"el => el.style.transform.includes('translate({x_px}px, {y_px}px)')")
        assert girassolpersist.evaluate("el => el.style.zIndex == '1'")

        assert girassolpersist.locator('img').evaluate("img => img.style.width") == '80%'
        assert girassolpersist.locator('img').evaluate("img => img.style.height") == '80%'


        # Colmeia
        colmeia = assert_ator(page, '#actors > div:nth-child(4)', x=1, y=2, z_index=1, img_src="img/colmeia.gif")
        assert colmeia.locator('.actor-value').inner_text() == '0'
        x_px = 1 * TILE_SIZE
        y_px = 2 * TILE_SIZE
        assert colmeia.evaluate(f"el => el.style.transform.includes('translate({x_px}px, {y_px}px)')")
        assert colmeia.evaluate("el => el.style.zIndex == '1'")

        assert colmeia.locator('img').evaluate("img => img.style.width") == '80%'
        assert colmeia.locator('img').evaluate("img => img.style.height") == '80%'


        # Nuvem
        nuvem = assert_ator(page, '#actors > div:nth-child(5)', x=4, y=1, z_index=2, img_src="img/nuvem.gif")
        assert nuvem.locator('.actor-value').inner_text() == ''
        assert nuvem.evaluate(f"el => el.style.transform.includes('translate({4 * TILE_SIZE}px, {TILE_SIZE}px)')")
        assert nuvem.evaluate("el => el.style.zIndex == '2'")

        assert nuvem.locator('img').evaluate("img => img.style.width") == '140%'
        assert nuvem.locator('img').evaluate("img => img.style.height") == '140%'


        # Nuvem Pequena
        nuvem_pequena = assert_ator(page, '#actors > div:nth-child(6)', x=2, y=2, z_index=2, img_src="img/nuvem.gif")
        assert nuvem_pequena.locator('.actor-value').inner_text() == ''

        X_OFFSET = 20
        Y_OFFSET = 20
        x_px = 2 * TILE_SIZE + X_OFFSET
        y_px = 2 * TILE_SIZE + Y_OFFSET
        assert nuvem_pequena.evaluate(f"el => el.style.transform.includes('translate({x_px}px, {y_px}px)')")
        assert nuvem_pequena.evaluate("el => el.style.zIndex == '2'")

        assert nuvem_pequena.locator('img').evaluate("img => img.style.width") == '40%'
        assert nuvem_pequena.locator('img').evaluate("img => img.style.height") == '40%'
