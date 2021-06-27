import copy
import logging as _logger

_logger.basicConfig(level='INFO')


class Prototype:

    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name: str, obj: object) -> None:
        """ Register an object """
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        """ Unregister an object """
        del self._objects[name]

    def clone(self, name, **attr) -> None:
        """ Clone a registered object and update its attributes """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:

    def __init__(self) -> None:
        self.name = 'Skylark'
        self.color = 'Red'
        self.options = 'Ex'

    def __str__(self) -> None:
        return f'{self.name} | {self.color} | {self.options}' 


def main() -> None:
    car1 = Car()
    prototype = Prototype()
    prototype.register_object('skylark', car1)

    car2 = prototype.clone('skylark')
    _logger.info(car2)


if __name__ == '__main__':
    main()
