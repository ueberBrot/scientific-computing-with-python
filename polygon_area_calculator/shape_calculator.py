"""
Rectangle and Square class for working with quadrilateral.
Square class is a subclass of Rectangle.
"""
from dataclasses import dataclass
from typing import Union


@dataclass
class Rectangle:
    """Class represents a rectangle quadrilateral."""

    width: int
    height: int

    def set_width(self, width: int) -> None:
        """Set the width of the quadrilateral.

        Args:
            width (int): Width for the quadrilateral.
        """
        self.width = width

    def set_height(self, height: int) -> None:
        """Set the height of the quadrilateral.

        Args:
            height (int): Height for the quadrilateral.
        """
        self.height = height

    def get_area(self) -> int:
        """Get the area of the quadrilateral.

        Returns:
            int: Area of the quadrilateral.
        """
        return self.width * self.height

    def get_perimeter(self) -> int:
        """Get the perimeter of the quadrilateral.

        Returns:
            int: The perimeter for the quadrilateral.
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> Union[int, float]:
        """Get the diagonal of the quadrilateral.

        Returns:
            Union[int, float]: The diagonal for the quadrilateral.
        """
        return pow(pow(self.width, 2) + pow(self.height, 2), 0.5)

    def get_picture(self) -> str:
        """Print a representaion of the quadrilateral with `*`.
        The number of lines are equal to the height and the
        number of "*" in each line are equal to the width.
        If width or height exceed 50 it can't be printed.

        Returns:
            str: Str representation of the quadrilateral.
        """
        if not (self.width or self.height) > 50:
            picture: str = ("*" * self.width + "\n") * self.height
            picture

            return picture
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape) -> int:
        """Checks of often the input shape fits inside the shape.
        It it is calculated with a floor division.

        Args:
            shape ([type]): New shape to be checked how much it fits
            into the shape.

        Returns:
            int: How much it fits inisde the shape.
        """
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    """Subclass of Rectangle that represents a square quadrilateral."""

    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def set_side(self, side: int) -> None:
        """Set the side of the quadrilateral.

        Args:
            side (int): Side for the quadrilateral.
        """
        self.width = side
        self.height = side

    def __repr__(self) -> str:
        return self.__class__.__qualname__ + f"(side={self.width!r})"
