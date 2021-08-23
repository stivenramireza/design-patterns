import logging as _logger

_logger.basicConfig(level='INFO')


class Subject: # Represents what is being 'observed'

    def __init__(self) -> None:
        self._observers = []    # This where references to all the observers are being kept
                                # Note that this is a one-to-many relationship: there will be one subject to be observed by mutiple _observers
    
    def attach(self, observer: object) -> None:
        if observer not in self._observers:     # If the observer is not already in the observers list
            self._observers.append(observer)    # Append the observer to the list

    def detach(self, observer: object) -> None: # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier: object = None) -> None:
        for observer in self._observers:    # For all the observers in the list
            if modifier != observer:        # Don't notify the observer who is actually updating the temperature
                observer.update(self)       # Alert the observers!


class Core(Subject): # Inherits from the Subject class

    def __init__(self, name: str = '') -> None:
        Subject.__init__(self)
        self._name = name   # Set the name of the core
        self._temp = 0      # Initialize the temperature of the core

    @property   # Getter that gets the core temperature
    def temp(self) -> int:
        return self._temp

    @temp.setter    # Setter that sets the core temperature
    def temp(self, temp) -> None:
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature


class TempViewer:

    def update(self, subject: object) -> None:  #Alert method that is invoked when then notify() method in a concrete subject is invoked
        _logger.info('Temperature Viewer: {} has Temperature {}'.format(subject._name, subject._temp))


def main() -> None:
    # Let's create our subjects
    c1 = Core('Core 1')
    c2 = Core('Core 2')

    # Let's create our observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Let's attach our observers to the first core
    c1.attach(v1)
    c1.attach(v2)

    # Let's change the temperature of ou first core
    c1.temp = 80
    c1.temp = 90


if __name__ == '__main__':
    main()
