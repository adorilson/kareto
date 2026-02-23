import random

from browser import document

TILE_SIZE = 50

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

    def render_actor(self, actor):
        el = self.actor_elements[actor]
        x_px = actor.x * TILE_SIZE
        y_px = actor.y * TILE_SIZE
        el.innerHTML = f'<img src="img/{actor.shape()}" style="width: 100%; height: 100%;"/>'
        el.style.transform = f"translate({x_px}px, {y_px}px)"
        el.style.zIndex = actor.z_index

        print(actor, actor.shape())

    def remove_actor(self, actor):
        print(f"Removendo ator: {actor}")
        el = self.actor_elements[actor]
        el.remove()
        del self.actor_elements[actor]