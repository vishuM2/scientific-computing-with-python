class Rectangle:

  def __init__(self, width, height):
    self.width = max(0, width)
    self.height = max(0, height)

  def set_width(self, width):
    self.width = max(0, width)

  def set_height(self, height):
    self.height = max(0, height)

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side, side)

  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)

  def __str__(self):
    return f"Square(side={self.width})"