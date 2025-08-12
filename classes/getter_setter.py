class Rectangle():
    def __init__(self, length, width):
        if not isinstance(length, (int, float)):
            raise TypeError(f"expected a number, got {type(length)}")
        if not isinstance(width, (int, float)):
            raise TypeError(f"Expected a number and got {type(width)}")
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):
        if not isinstance(new_length, (int, float)):
            print("Length is not a number")
            return
        self._length = new_length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (int, float)):
            print("Width is not a number")
            return
        self._width = new_width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def info(self):
        print("-------------------------")
        print("Shape is rectangle")
        print("Length is", self.length)
        print("Width", self.width)
        print("Area", self.area())
        print("Perimeter", self.perimeter())
        print("-------------------------")

r1 = Rectangle(length=30, width=12)

r1.info()

r1.length = "hello world"
r1.info()

r1.length = 80
r1.info() 