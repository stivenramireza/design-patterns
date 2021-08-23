import logging as _logger

_logger.basicConfig(level='INFO')


def count_to(count: int) -> None:
    """ Our iterator implementation """

    # Our list
    numbers_in_german = ['eins', 'zwei', 'drei', 'vier', 'funf']

    # Out built-in iterator
    # Creates a tuple such as (1, 'eins')
    iterator = zip(range(count), numbers_in_german)

    # Iterate thorugh our iterable list
    # Extract the German numbers
    # Put them in a generator called number
    for position, number in iterator:
        # Returns a 'generator' containing numbers in German
        yield number


def main() -> None:
    # Let's test the generator returned by our iterator
    for num in count_to(3):
        _logger.info('{}'.format(num))

    for num in count_to(5):
        _logger.info('{}'.format(num))


if __name__ == '__main__':
    main()
