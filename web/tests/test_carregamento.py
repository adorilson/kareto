"""
Testa se a página está sendo carregada corretamente, ou seja, se os componentes estáticos e dinâmicos estão presentes e visíveis na página.

Não testa interações do usuário, como clicar em botões ou digitar no console.
"""


from playwright.sync_api import sync_playwright

from web.tests.common import assert_ator


def test_componentes_estaticos():
    """Testa se os componentes estáticos estão presentes na página."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)  # Set headless=True if you don’t want browser UI
        page = browser.new_page()
        page.goto("http://localhost:8000")

        assert "Kareto Web" in page.title()

        assert page.locator("#editor-panel").is_visible()
        assert page.locator("#game-panel").is_visible()
        assert page.locator("#console-panel").is_visible()
        assert page.locator("#output-panel").is_visible()

        assert page.locator("#confs").is_visible() is False


def test_componentes_dinamicos():
    """Testa se os componentes carregados dinamicamente, seja via JavaScript, seja via Brython, estão visíveis na página."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        assert page.locator(".CodeMirror").is_visible()

        assert page.locator("#board > div:nth-child(1)").is_visible()
        assert page.locator("#board > div:nth-child(64)").is_visible()

        assert page.locator("#console > pre:nth-child(1)").is_visible()
        assert "Brython 3.14" in page.locator("#console > pre:nth-child(1)").inner_text()


def test_criacao_mundo_via_query_string():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&gs=6,4&c=2,4,2")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=4, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(3)', x=5, y=4, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(4)', x=6, y=4, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(5)', x=2, y=4, z_index=1, img_src="img/colmeia.gif")


def test_criacao_mundo_via_documento():
    """Testa se o mundo é criado corretamente a partir das configurações
    presentes no documento HTML, caso a query string não esteja presente.
    
    Assume que existe a seguinte configuração no documento:
    {
      "maia": ["1,3,0"],
      "gs": ["3,4", "1,5"],
      "cag":[1]
    }
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        page.wait_for_function("() => document.querySelectorAll('#actors > div').length >= 3")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=3, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(3)', x=1, y=5, z_index=1, img_src="img/girassol.gif")


def test_criacao_mundo_com_query_string_sem_chaves_validas():
    """Testa se a query string é ignorada quando não contém chaves de
    configuração de mundo válidas. Neste caso, o mundo deve ser criado a
    partir das configurações presentes.
    
    Assume que existe a seguinte configuração no documento:
    {
      "maia": ["1,3,0"],
      "gs": ["3,4", "1,5"],
      "cag":[1]
    }"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000?aid=314&type=new")

        page.wait_for_function("() => document.querySelectorAll('#actors > div').length >= 3")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=3, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(3)', x=1, y=5, z_index=1, img_src="img/girassol.gif")



def test_configuracao_abelha_invalida():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,7&cag=1") # falta a direção da abelha

        # Verificar se a mensagem de erro foi exibida
        assert "Traceback" in page.locator("#output-content").inner_text().strip()
        assert "IndexError" in page.locator("#output-content").inner_text().strip()


def test_overlay():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        assert page.locator("#loading-overlay").is_visible()

        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")
        assert page.locator("#loading-overlay").is_visible() is False
