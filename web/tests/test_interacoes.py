"""
Testa interações do usuário
"""

import textwrap

from playwright.sync_api import sync_playwright



from web.tests.common import assert_ator, wait_for_output_content

# Mudar para 
#import renderer.TILE_SIZE
TILE_SIZE = 65


def test_captura_automatica():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        # com a mudança no gerenciamento da fila por causa dos condicionais,
        # o parametro fast deixou de funcionar neste caso específico
        page.goto("http://localhost:8000/?maia=1,4,0&cag=1&gs=3,4&gs=5,4&gs=6,4")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=4, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=3, y=4, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=5, y=4, z_index=1, img_src="img/girassol.gif")
        g3      = assert_ator(page, '#actors > div:nth-child(4)', x=6, y=4, z_index=1, img_src="img/girassol.gif") 
        
        assert page.locator('.CodeMirror').is_visible()
        data = """for _ in range(5): maia.avance()"""
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        # nova posicao da abelha
        x, y = 6, 4
        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({x*TILE_SIZE}px, {y*TILE_SIZE}px); z-index: 3;"

        assert g1.is_hidden()
        assert g2.is_hidden()
        assert g3.is_hidden()


def test_recomecar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=3,2&gs=4,3&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=3, y=2, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=4, y=3, z_index=1, img_src="img/girassol.gif")

        data = "maia.avance()"
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") != f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"

        page.locator("#clear").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.get_attribute("style") == f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert g1.is_visible()
        assert g1.get_attribute("style") == f"transform: translate({3*TILE_SIZE}px, {2*TILE_SIZE}px); z-index: 1;"
        assert g2.is_visible()
        assert g2.get_attribute("style") == f"transform: translate({4*TILE_SIZE}px, {3*TILE_SIZE}px); z-index: 1;"


def test_recomecar_com_nectar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1&gs=4,3&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

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
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=3, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert page.locator(
            f'#actors > div[style="transform: translate({3*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 0
        assert page.locator(
            f'#actors > div[style="transform: translate({4*TILE_SIZE}px, {3*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 1

        page.locator("#clear").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        abelha  = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1      = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        g2      = assert_ator(page, '#actors > div:nth-child(3)', x=4, y=3, z_index=1, img_src="img/girassol.gif")


def test_girassol_persistente_nao_some_e_mostra_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gsp=2,1,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")

        data = """
        maia.avance()
        maia.extraia_nectar()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert g1.is_visible()
        assert g1.locator(".actor-value").inner_text() == "0"


def test_colmeia_consume_nectar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=2,1,2&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        colmeia = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")

        data = """
        maia.avance()
        maia.faça_mel()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert colmeia.is_visible()
        assert colmeia.locator(".actor-value").inner_text() == "1"


def test_run_code_remove_nuvens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&n=2,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=2, img_src="img/nuvem.gif")

        data = "pass"
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert page.locator('img[src="img/nuvem.gif"]').count() == 0


def test_run_code_remove_girassol_probabilidade_um():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gsp=2,1,,p=1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")

        data = "pass"
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert page.locator('img[src="img/girassol.gif"]').count() == 0


def test_run_code_remove_girassol_probabilidade_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gsp=2,1,,p=0&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")

        data = "pass"
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert page.locator('img[src="img/girassol.gif"]').count() == 1


def test_na_colmeia_condicional_faz_mel():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=1,1,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=1, y=1, z_index=1, img_src="img/colmeia.gif")
        assert c1.inner_text() == "1"

        data = """
        if maia.na_colmeia():
            maia.faça_mel()
        else:
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert c1.inner_text() == "0"


def test_na_colmeia_condicional_else_avanca():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=2,1,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")
        assert c1.inner_text() == "1"

        data = """
        if maia.na_colmeia():
            maia.faça_mel()
        else:
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({2*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert c1.is_visible()
        assert c1.inner_text() == "1"


def test_na_colmeia_com_repeticao_e_multiplas_colmeias_em_linha():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=2,1,1&c=3,1,1&c=4,1,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")
        c2 = assert_ator(page, '#actors > div:nth-child(3)', x=3, y=1, z_index=1, img_src="img/colmeia.gif")
        c3 = assert_ator(page, '#actors > div:nth-child(4)', x=4, y=1, z_index=1, img_src="img/colmeia.gif")

        assert c1.inner_text() == "1"
        assert c2.inner_text() == "1"
        assert c3.inner_text() == "1"

        data = """
        for _ in range(3):
            if maia.na_colmeia():
                maia.faça_mel()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=4, y=1, z_index=3, img_src="img/abelha_leste.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")
        c2 = assert_ator(page, '#actors > div:nth-child(3)', x=3, y=1, z_index=1, img_src="img/colmeia.gif")
        c3 = assert_ator(page, '#actors > div:nth-child(4)', x=4, y=1, z_index=1, img_src="img/colmeia.gif")

        assert abelha.is_visible()
        assert c1.inner_text() == "0"
        assert c2.inner_text() == "0"
        assert c3.inner_text() == "1"


def test_na_colmeia_com_multiplos_colmeias_a_direita():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=2,2,1&c=2,3,1&fast=1")

        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        data = """
        maia.avance()
        maia.direita()
        for _ in range(3):
            if maia.na_colmeia():
                maia.faça_mel()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=2, y=4, z_index=3, img_src="img/abelha_sul.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=2, z_index=1, img_src="img/colmeia.gif")
        c2 = assert_ator(page, '#actors > div:nth-child(3)', x=2, y=3, z_index=1, img_src="img/colmeia.gif")

        assert c1.inner_text() == "0"
        assert c2.inner_text() == "0"


def test_na_colmeia_com_multiplos_colmeias_a_esquerda():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,3,180&c=0,4,1&c=0,3,1&fast=1")

        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        data = """
        maia.avance()
        maia.esquerda()
        for _ in range(2):
            if maia.na_colmeia():
                maia.faça_mel()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=0, y=5, z_index=3, img_src="img/abelha_sul.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=0, y=4, z_index=1, img_src="img/colmeia.gif")
        c2 = assert_ator(page, '#actors > div:nth-child(3)', x=0, y=3, z_index=1, img_src="img/colmeia.gif")

        assert c1.inner_text() == "0"
        assert c2.inner_text() == "0"


def test_no_girassol_condicional_extrai():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=1,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=1, y=1, z_index=1, img_src="img/girassol.gif")

        data = """
        if maia.no_girassol():
            maia.extraia_nectar()
        else:
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({1*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert g1.is_hidden()


def test_no_girassol_condicional_else_avanca():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")

        data = """
        if maia.no_girassol():
            maia.extraia_nectar()
        else:
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({2*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert g1.is_visible()


def test_no_girassol_com_repeticao_e_multiplos_girassois_em_linha():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,1&gs=3,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        assert_ator(page, '#actors > div:nth-child(3)', x=3, y=1, z_index=1, img_src="img/girassol.gif")

        data = """
        for _ in range(3):
            if maia.no_girassol():
                maia.extraia_nectar()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({4*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 3;"
        assert page.locator(
            f'#actors > div[style="transform: translate({2*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 0
        assert page.locator(
            f'#actors > div[style="transform: translate({3*TILE_SIZE}px, {1*TILE_SIZE}px); z-index: 1;"]'
        ).count() == 0


def test_no_girassol_com_multiplos_girassois_a_direita():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gs=2,2&gs=2,3&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=2, z_index=1, img_src="img/girassol.gif")
        g2 = assert_ator(page, '#actors > div:nth-child(3)', x=2, y=3, z_index=1, img_src="img/girassol.gif")

        data = """
        maia.avance()
        maia.direita()
        for _ in range(3):
            if maia.no_girassol():
                maia.extraia_nectar()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert abelha.get_attribute("style") == f"transform: translate({2*TILE_SIZE}px, {4*TILE_SIZE}px); z-index: 3;"
        assert g1.is_hidden()
        assert g2.is_hidden()


def test_no_girassol_com_multiplos_girassois_a_esquerda():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,3,180&gs=0,4&gs=0,3&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=3, z_index=3, img_src="img/abelha_oeste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=0, y=4, z_index=1, img_src="img/girassol.gif")
        g2 = assert_ator(page, '#actors > div:nth-child(3)', x=0, y=3, z_index=1, img_src="img/girassol.gif")

        data = """
        maia.avance()
        maia.esquerda()
        for _ in range(2):
            if maia.no_girassol():
                maia.extraia_nectar()
            maia.avance()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)
        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

        assert abelha.is_visible()
        assert g1.is_hidden()
        assert g2.is_hidden()


def test_girassol_e_colmeia_sob_nuvem():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gsp=2,1,1&c=2,1,1&n=2,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        g1 = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1, img_src="img/girassol.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(3)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")
        n1 = assert_ator(page, '#actors > div:nth-child(4)', x=2, y=1, z_index=2, img_src="img/nuvem.gif")

        data = """
        maia.avance()
        if maia.no_girassol():
            maia.extraia_nectar()
        else:
            maia.faça_mel()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        # rodar o código algumas vezes para garantir que tanto o girassol
        # quanto a colmeia sejam testados
        girassois = 0
        colmeias = 0
        for _ in range(4):
            page.locator("#run-btn").click()
            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            wait_for_output_content(page, 'Tarefa realizada com sucesso.')
            ator = assert_ator(page, '#actors > div:nth-child(2)', x=2, y=1, z_index=1)
            assert ator.locator("div.actor-value").inner_text() == "0"
            girassois =  girassois + (ator.locator("img").get_attribute("src") == "img/girassol.gif")
            colmeias = colmeias + (ator.locator("img").get_attribute("src") == "img/colmeia.gif")

            if girassois and colmeias:
                break

        assert girassois > 0
        assert colmeias > 0


def test_sorteia_colmeias():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&c=1,2,1,p=0.5&c=2,1,1,p=0.5&n=1,2&n=2,1&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")


        abelha = assert_ator(page, '#actors > div:nth-child(1)', x=1, y=1, z_index=3, img_src="img/abelha_leste.gif")
        c1 = assert_ator(page, '#actors > div:nth-child(2)', x=1, y=2, z_index=1, img_src="img/colmeia.gif")
        c2 = assert_ator(page, '#actors > div:nth-child(3)', x=2, y=1, z_index=1, img_src="img/colmeia.gif")
        n1 = assert_ator(page, '#actors > div:nth-child(4)', x=1, y=2, z_index=2, img_src="img/nuvem.gif")
        n2 = assert_ator(page, '#actors > div:nth-child(5)', x=2, y=1, z_index=2, img_src="img/nuvem.gif")

        data = """
        for _ in range(4):
            maia.avance()
            if maia.na_colmeia():
                maia.faça_mel()
            maia.direita()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        # rodar o código algumas vezes para garantir mais de uma configuração
        # de colmeias
        configuracoes_colmeias = [False, False, False]

        for _ in range(4):
            page.locator("#run-btn").click()
            page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")

            wait_for_output_content(page, 'Tarefa realizada com sucesso.')
            atores = page.locator('img[src="img/colmeia.gif"]').count()
            configuracoes_colmeias[atores] = True

            if sum(configuracoes_colmeias) >= 2:
                break

        assert sum(configuracoes_colmeias) >= 2


def test_tem_nectar_no_girassol_na_web():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,1,0&gsp=2,1,3&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        data = """
        while tem_nectar_no_girassol():
            maia.extraia_nectar()

        maia.avance()

        while tem_nectar_no_girassol():
            maia.extraia_nectar()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")
        wait_for_output_content(page, 'Tarefa realizada com sucesso.')


def test_tem_nectar_no_girassol_condicional_na_web():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"],)
        page = browser.new_page()
        page.goto("http://localhost:8000/?maia=1,3,0&gsp=3,4,2&gsp=1,5,3&cag=0&fast=1")
        page.wait_for_function("() => document.getElementById('loading-overlay').className == 'hidden'")

        data = """
        for _ in range(3):
            for _ in range(2):
                maia.avance()
                while tem_nectar_no_girassol():
                    maia.extraia_nectar()
            
            maia.direita()
        """
        data = textwrap.dedent(data)
        page.evaluate('data => {window.editor.setValue(data)}', data)

        page.locator("#run-btn").click()
        page.wait_for_function("() => window.is_running === false && window.command_queue_len === 0")
        wait_for_output_content(page, 'Tarefa realizada com sucesso.')