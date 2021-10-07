class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

square = Square(4, 4)
cube = Cube(4, 4, 4)

# super() funksiyasi class ning otasini ko'rsatadi.