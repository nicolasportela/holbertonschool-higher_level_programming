#!/usr/bin/python3
"""this module contains the class Rectangle derivated from Base"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, width):
        """width value"""

        self.__width = width
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, height):
        """height value"""

        self.__height = height
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, x):
        """x value"""

        self.__x = x
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, y):
        """y value"""

        self.__y = y
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calculates the area of the rectangle"""

        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        a = 0
        while a < self.__y:
            print("")
            a += 1
        b = 1
        while b <= self.__height:
            print((" " * self.__x) + ("#" * self.__width))
            b += 1

    def __str__(self):
        """string representation"""

        s = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                                                            self.id,
                                                            self.__x,
                                                            self.__y,
                                                            self.__width,
                                                            self.__height
                                                            )
        return s

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""

        list_attr = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        rect_dict = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
        return rect_dict
