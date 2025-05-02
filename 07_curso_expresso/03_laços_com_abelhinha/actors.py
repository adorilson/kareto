import turtle
from turtle import *
import time
import random


BEE_EAST = "bee_east.gif"
BEE_NORTH = "bee_north.gif"
BEE_WEST = "bee_west.gif"
BEE_SOUTH = "bee_south.gif"

FLOWER = "sunflower.gif"

turtle.register_shape(BEE_EAST)
turtle.register_shape(BEE_WEST)
turtle.register_shape(BEE_NORTH)
turtle.register_shape(BEE_SOUTH)
turtle.register_shape(FLOWER)


class Bee(turtle.Turtle):
    def __init__(self, *args, ):
        super().__init__(visible=False)
        self.shape(BEE_EAST)
        self.penup()
        self.position = 0

    def forward(self):
        time.sleep(0.5)
        self.position = self.position+1
        update()
        time.sleep(0.5)

    def extract_nectar(self, flower):
        flower.extract_nectar()


class FlowerError(Exception):
    ...


class Flower(turtle.Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.shape(FLOWER)
        self.nectar = random.randint(0, 10)
        self.penup()

    def extract_nectar(self):
        if self.nectar>0:
            self.nectar = self.nectar - 1
        else:
            raise FlowerError("Não há mais nectar para ser colhido.")


if __name__=="__main__":
    bee = Bee()
    bee.goto(-100, 0)
    bee.showturtle()

    flower = Flower()
    flower.goto(100, 0)
    flower.showturtle()

    turtle.mainloop()
