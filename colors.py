from collections import namedtuple

Colour = namedtuple("Colour", ["r", "g", "b"])

BACKGROUND = Colour(r=1, g=22, b=39)
SNAKE = Colour(r=255, g=0, b=25)
FOOD = Colour(r=255, g=253, b=65)
TEXT = Colour(r=255, g=255, b=255)