from functools import wraps

import logging as _logger

_logger.basicConfig(level='INFO')


def make_blink(function: object) -> object:
    """ Defines the decorator """

    # This makes the decorator transparent in terms of its name and docstring
    @wraps(function)
    # Define the inner function
    def decorator() -> str:
        # Grab the return value of the function being decorated
        ret = function()
        # Add new functionality to the function being decorated
        return '<blink>' + ret + '</blink>'
    return decorator


# Apply the decorator here!
@make_blink
def hello_world() -> str:
    """ Original function! """
    return 'Hello, world!'


def main() -> None:
    # Check the result of decorating
    _logger.info(hello_world())

    # Check if the function name is still the same name of the function being decorated
    _logger.info(hello_world.__name__)

    # Check if the docstring is still the same as that of the function being decorated
    _logger.info(hello_world.__doc__)


if __name__ == '__main__':
    main()
