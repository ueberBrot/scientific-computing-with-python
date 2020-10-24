"""
This module contains the `Hat` class.
The class takes a variable number of arguments that specify
the number of balls of each color that are in the hat. For example,
a class object could be created in any of these ways:

```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```
"""
import copy
import random


class Hat:
    """Represents a hat that is filled with different colored balls.
    Also it has a method that can draw a random ball from the hat.
    """

    def __init__(self, **kwargs) -> None:
        # for the __repr__ method
        self.kwargs: dict[str, int] = kwargs
        self.contents: list[str] = []

        # loop through the keyword arguments
        for color in kwargs.keys():
            # the index is not needed so `_` is sufficient
            # epeat the loop as often as the value in the keyword argument
            # and append the key as much
            for _ in range(kwargs[color]):
                self.contents.append(color)

    def draw(self, num_of_balls: int) -> list[str]:
        """Draw balls from the hat by random.

        Args:
            num_of_balls (int): A number of balls to draw from the hat.

        Returns:
            list[str]: Drawn balls.
        """
        # safety or the pop() method
        # so that pop can't pop from an empty list
        # and raise an `IndexError`
        if num_of_balls >= len(self.contents):
            return self.contents

        balls: list[str] = []

        # repeat the loop for every ball wanted
        for _ in range(num_of_balls):
            # choose a random ball out of the list
            # to get a int value `random.randint` is the perfect function
            # ref:
            # https://github.com/timgrossmann/InstaPy/issues/2208#issuecomment-396048533
            choice: int = random.randint(0, abs(len(self.contents) - 1))

            # `pop()` removes the item from the list so it can not be drawn again
            balls.append(self.contents.pop(choice))

        return balls

    def __repr__(self) -> str:
        """For the `print` representation of the Hat.
        Because I like to look at stuff...

        Returns:
            str: Str representation of the Hat class with the instance variables.
        """
        return __class__.__qualname__ + f"({self.kwargs})"


# ref:
# https://medium.com/i-math/can-you-solve-this-intro-probability-problem-807c59543c32
# https://en.wikipedia.org/wiki/Urn_problem
def experiment(
    hat: Hat,
    expected_balls: dict[str, int],
    num_balls_drawn: int,
    num_experiments: int,
) -> float:
    """Calculate the probability of specific balls been drawn.

    Args:
        hat (Hat): An instantiation of a Hat object.
        expected_balls (dict[str, int]): Representation of what balls should
        be drawn and how many.
        num_balls_drawn (int): A number of balls that are drawn per experiment.
        num_experiments (int): How many experiments should be performed.

    Returns:
        float: Probability that the requested balls are drawn.
    """
    # variable to count successful draws
    num_successes: int = 0

    for _ in range(num_experiments):
        # grab a new, fresh copy of the hat everytime the loop is run through
        # https://docs.python.org/3/library/copy.html
        # using the `copy` method is not suffcient
        # so we use the `deepcopy` method instead
        hat_copy: Hat = copy.deepcopy(hat)

        # draw balls
        balls: list[str] = hat_copy.draw(num_balls_drawn)

        # variable to indicate a successful draw
        successful_draws: bool = True

        for color in expected_balls.keys():
            # ref:
            # https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count
            if balls.count(color) < expected_balls[color]:
                successful_draws = False
                continue

        if successful_draws:
            num_successes += 1

    return float(num_successes / num_experiments)
