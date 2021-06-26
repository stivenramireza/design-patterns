import logging as _logger

_logger.basicConfig(level='INFO')


class Dog:

    """ A simple dog class """

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return 'Woof!'


class Cat:

    """ A simple cat class """

    def __init__(self, name: str) -> None:
        self._name = name

    def speak(self) -> str:
        return 'Meow!'


def get_pet(pet: str = 'dog') -> object:

    """ The factory method """

    pets = dict(dog=Dog('Hope'), cat=Cat('Negro'))
    return pets[pet]


def main() -> None:
    dog = get_pet('dog')
    _logger.info(dog.speak())

    cat = get_pet('cat')
    _logger.info(cat.speak())


if __name__ == '__main__':
    main()
