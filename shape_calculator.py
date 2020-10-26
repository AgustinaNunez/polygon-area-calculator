class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, another_rectangle):
        return (self.width // another_rectangle.width) \
               * (self.height // another_rectangle.height)


class Square(Rectangle):
    side = 0

    def __init__(self, side):
        super(Square, self).__init__(side, side)
        self.side = side

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self, side):
        self.side = side
        super(Square, self).set_width(side)
        super(Square, self).set_height(side)

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
