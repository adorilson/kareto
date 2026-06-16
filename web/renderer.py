import random

from browser import document

TILE_SIZE = 65

class Renderer:
    def __init__(self, world):
        self.world = world
        self.board_element = document["board"]
        self.actors_element = document["actors"]
        self.actor_elements = {}

        self._create_board()

    def _create_board(self):
        self.board_element.clear()
        for _ in range(self.world.width * self.world.height):
            tile = document.createElement("div")
            tile.className = "tile"
            tons_de_verde = "green", "darkgreen", "forestgreen", "seagreen"
            tile.attrs['style'] = f'background-color: {random.choice(tons_de_verde)}'
            self.board_element <= tile

    def reset(self):
        self.actors_element.clear()
        self.actor_elements = {}

    def register_actor(self, actor):
        el = document.createElement("div")
        el.className = "actor"

        self.actors_element <= el
        self.actor_elements[actor] = el
        self.render_actor(actor)

    def as_tag_html(self, actor):
        width, height = getattr(actor, "image_size", (80, 80))
        s = actor.shape()
        v = actor.value if actor.value is not None else ''
        return f"""<img src="img/{s}" style="width: {width}%; height: {height}%;"/>
                    <div class="actor-value">{v}</div>"""

    def render_actor(self, actor):
        el = self.actor_elements[actor]
        el.innerHTML = f'{self.as_tag_html(actor)}'

        x_px = actor.x * TILE_SIZE
        y_px = actor.y * TILE_SIZE
        el.style.transform = f"translate({x_px}px, {y_px}px)"
        el.style.zIndex = actor.z_index

    def remove_actor(self, actor):
        el = self.actor_elements[actor]
        el.remove()
        del self.actor_elements[actor]