import logging as _logger

_logger.basicConfig(level='INFO')


class DrawingAPIOne(object):
    """ Implementation-specific abstraction: concrete class one """
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        _logger.info('API 1 drawing a circle at ({}, {}) with radius {}!'.format(x, y, radius))


class DrawingAPITwo(object):
    """ Implementation-specific abstraction: concrete class two """
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        _logger.info('API 2 drawing a circle at ({}, {}) with radius {}!'.format(x, y, radius))


class Circle(object):
    """ Implementation-independent abstraction: for example, there coul be a rectangle class!"""

    def __init__(self, x: float, y: float, radius: float, drawing_api: object) -> None:
        """ Initialize the necessary attributes """
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self) -> None:
        """ Implementation-specific abstraction taken care of by antoher class: DrawingAPI """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent: float) -> None:
        self._radius *= percent


# Build the first Circle object using API One
circle1 = Circle(1, 2, 3, DrawingAPIOne())
# Draw a circle
circle1.draw()

# Build the second Circle object using API Two
circle2 = Circle(2, 3, 4, DrawingAPITwo())
# Draw a circle
circle2.draw()
