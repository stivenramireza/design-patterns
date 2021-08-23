import logging as _logger

_logger.basicConfig(level='INFO')


class House:    # The class being visited

    def accept(self, visitor: object) -> None:
        """ Interface to accept a visitor """
        # Triggers the visiting operation!
        pass

    def work_on_hvac(self, hvac_specialist: object) -> None:
        # Note that we now have a reference to the HVAC specialist object in the house object!
        _logger.info(f'{self} worked on by {hvac_specialist}')

    def work_on_electricity(self, electrician: object) -> None:
        # Note that we now have a reference to the electrician object in the house object!
        _logger.info(f'{self} worked on by {electrician}')

    def __str__(self) -> str:
        return self.__class__.__name__


class Visitor:
    """ Abstract Visitor """
    def __str__(self) -> str:
        """ Simply return the class name when the Visitor object is printed """
        return self.__class__.__name__


class HvacSpecialist(Visitor):  # Inherits from the parent class, Visitor
    """ Concrete visitor: HVAC specialist """
    def visit(self, house: object) -> None:
        house.work_on_hvac(self) # Note that the visitor now has a reference to the house object


class Electrician(Visitor): # Inherits from the parent class, Visitor
    """ Concrete visitor: electrician """
    def visit(self, house: object) -> None:
        house.work_on_electricity(self) # Note that the visitor now has a reference to the house object


def main() -> None:
    # Create an HVAC specialist
    hvac_specialist = HvacSpecialist()

    # Create an electrician
    electrician = Electrician()

    # Create a house
    house = House()

    # Let the house accept the HVAC specialist and work on the house by invoking the visit() method
    house.accept(hvac_specialist)

    # Let the house accept the electrician and work on the house by invoking the visit() method
    house.accept(electrician)


if __name__ == '__main__':
    main()
