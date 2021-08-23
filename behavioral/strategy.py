import types    # Import the types module
import logging as _logger

_logger.basicConfig(level='INFO')


class Strategy:
    """ The Strategy Pattern class """

    def __init__(self, function: object = None) -> None:
        self.name = 'Default Strategy'

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self) -> None:  # This gets replaced by another version if another strategy is provided
        """ The default method that prints the name of the strategy being used """
        _logger.info('{} is used!'.format(self.name))


# Replacement method 1
def strategy_one(self) -> None:
    _logger.info('{} is used to execute method 1'.format(self.name))


# Repĺacement method 2
def strategy_two(self) -> None:
    _logger.info('{} is used to execute method 2'.format(self.name))


def main() -> None:
    # Let's create our default strategy
    s0 = Strategy()
    # Let's execute our default strategy
    s0.execute()

    # Let's create the first variation of our default strategy by providing a new behaviour
    s1 = Strategy(strategy_one)
    # Let's set its name
    s1.name = 'Strategy One'
    #Let's execute the strategy
    s1.execute()

    # Let's create the second variation of our default strategy by providing a new behaviour
    s2 = Strategy(strategy_two)
    # Let's set its name
    s2.name = 'Strategy Two'
    #Let's execute the strategy
    s2.execute()


if __name__ == '__main__':
    main()
