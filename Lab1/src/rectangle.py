from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def set_values(self):
        pass

    @abstractmethod
    def area(self):
        pass


"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""


class Rectangle:
    def __init__(self):
        self._width = None
        self._height = None

    def set_values(self, x, y):
        self._width = x
        self._height = y

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
