import logging as _logger

_logger.basicConfig(level='INFO')


class Borg:
    """ Borg class making class attributes global """
    _shared_state = {} # Attribute dictionary

    def __init__(self) -> None:
        self.__dict__ = self._shared_state # Make it an attribute dictionary


class Singleton(Borg): # Inherits from the Borg class
    """ This class now shares all its attributes among its various instances """
    # This essentially makes the singleton objects on object-oriented global variable """

    def __init__(self, **kwargs) -> None:
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


def main() -> None:
    # Let's create a singleton object and add our first acronym
    x = Singleton(HTTP='Hyper Text Transfer Protocol')
    _logger.info(x)

    # Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
    y = Singleton(SNMP='Simple Network Management Protocol')
    _logger.info(y)


if __name__ == '__main__':
    main()
