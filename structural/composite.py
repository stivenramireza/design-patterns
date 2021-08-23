import logging as _logger

_logger.basicConfig(level='INFO')


class Component(object):
    """ Abstract class """
    def __init__(self, *args, **kwargs) -> None:
        pass

    def component_function(self) -> None:
        pass


class Child(Component): # Inherits from the abstract class, Component
    """ Concrete class """
    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self) -> None:
        # Print the name of your child item here!
        _logger.info('{}'.format(self.name))


class Composite(Component): # Inherits from the abstract class, Component
    """ Concrete class and maintains the tree recursive structure """
    def __init__(self, *args, **kwargs) -> None:
        Component.__init__(self, *args, **kwargs)

        # This is where we store the name of the composite object
        self.name = args[0]

        # This is where we keep our child items
        self.children = []

    def append_child(self, child: object) -> None:
        self.children.append(child)

    def remove_child(self, child: object) -> None:
        self.children.remove(child)

    def component_function(self) -> None:
        # Print the name of the composite object
        _logger.info('{}'.format(self.name))

        # Iterate though the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()


def main() -> None:
    # Build a composite submenu 1
    sub1 = Composite('submenu1')

    # Create a new child sub_submenu 11
    sub11 = Child('sub_submenu 11')
    # Create a new Child sub_menu 12
    sub12 = Child('sub_submenu 12')

    # Add the sub_submenu 11 to submenu 1
    sub1.append_child(sub11)
    # Add the sub_submenu 12 to submenu 1
    sub1.append_child(sub12)

    # Build a top-level composite menu
    top = Composite('top_menu')

    # Build a submenu 2 that is not a composite
    sub2 = Child('submenu2')

    # Add the composite submenu 1 to the top-level composite menu
    top.append_child(sub1)

    # Add the plain submenu 2 to the top-level composite menu
    top.append_child(sub2)

    # Let's test if our Composite pattern works!
    top.component_function()


if __name__ == '__main__':
    main()
