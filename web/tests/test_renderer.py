from playwright.sync_api import sync_playwright

from common import assert_ator


def test_renderer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1")

        page.wait_for_function("() => document.querySelectorAll('#actors > div').length >= 1")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        assert g1.locator('.actor-value').inner_text() == ''
