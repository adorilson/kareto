TILE_SIZE = 65 #deveria vir de renderer.TILE_SIZE

def assert_ator(page, tile_selector, x, y, z_index, img_src):
    tile = page.locator(tile_selector)
    assert tile.is_visible()
    assert tile.get_attribute("style") == f"transform: translate({x*TILE_SIZE}px, {y*TILE_SIZE}px); z-index: {z_index};"
    assert tile.locator("img").get_attribute("src") == img_src
    return tile
