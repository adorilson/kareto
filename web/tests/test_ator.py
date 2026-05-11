import random

import pytest

from web.entities import Ator, Direcao
from web.world import World


def make_actor(x=2, y=3, direcao=Direcao.LESTE, shape=""):
    actor = Ator(world=None, command_queue=None, x=x, y=y, direcao=direcao)
    actor._shape = shape
    actor._value = ""
    actor.x = x
    actor.y = y
    actor.direcao = direcao
    return actor


def test_shape_getter_setter():
    actor = make_actor()

    assert actor.shape() == ""
    actor.shape("abelha_leste.gif")
    assert actor.shape() == "abelha_leste.gif"


def test_setheading_updates_direction_and_shape():
    actor = make_actor()

    actor.setheading(Direcao.NORTE)

    assert actor.heading() == Direcao.NORTE
    assert actor.shape() == Ator.IMAGENS[Direcao.NORTE]


def test_setheading_none_returns_current_direction():
    actor = make_actor(direcao=Direcao.OESTE)

    assert actor.setheading(None) == Direcao.OESTE
    assert actor.heading() == Direcao.OESTE


def test_setheading_invalid_direction_raises():
    actor = make_actor()

    with pytest.raises(ValueError):
        actor.setheading(42)


def test_goto_updates_position_and_posicao():
    actor = make_actor(x=0, y=0)

    actor.goto(5, 7)

    assert actor.x == 5
    assert actor.y == 7
    assert actor.posicao == (5, 7)


def test_value_property_returns_value():
    actor = make_actor()
    actor._value = "nectar"

    assert actor.value == "nectar"


def test_str_includes_position_and_direction():
    actor = make_actor(x=4, y=6, direcao=Direcao.SUL)

    text = str(actor)

    assert "(4, 6)" in text
    assert f"facing {Direcao.SUL}" in text


def test_init_randomizes_y_when_missing_and_x_provided():
    random.seed(123)
    world = World(width=4, height=6)

    actor = Ator(world=world, command_queue=[], x=1, y=None)

    assert isinstance(actor.y, int)
    assert world.in_bounds(actor.x, actor.y)
