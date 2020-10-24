# Scientific Computing with Python Projects

This repository contains **my** solutions for the projects of the python course [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/) from [freeCodeCamp](https://www.freecodecamp.org/).

## Note

The solutions in this repository are made with `Python 3.9.0`.

## [Arithmetic Formatter](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)

Link to **my** project solution [click me](arithmetic_arranger/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/arithmetic-formatter#README.md)

## [Time Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)

Link to **my** project solution [click me](time_calculator/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/time-calculator#README.md)

## [Budget App](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)

Link to **my** project solution [click me](budget_app/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/budget-app#README.md)

## [Polygon Area Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

Link to **my** project solution [click me](polygon_area_calculator/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/polygon-area-calculator#README.md)

## [Probability Calculator](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

**Note:**

The tip with the `copy` module, that was not known to me before, saved me. (I mean who knows everything ¯\\\_(ツ)_/¯). Without it I would have no clue of to solve this one as easy as i did 😋.

Till I was hitting the unit tests, I did not think at all, that if I pull out of the hat, the taken out balls are missing for the next iteration (although the task description says, that it is to treat like an urn drawing...).
Thus every iteration did not have the same pool of balls.
Fortunately there is the `copy.deepcopy` method. With this I could solve the problem.
Also I ran into `ValueError: empty range for randrange() (0, 0, 0)` errors and had to use all mighty google to find help in a [GitHub issue](https://github.com/timgrossmann/InstaPy/issues/2208#issuecomment-396048533). That was also refreshing 😅.

Link to **my** project solution [click me](probability_calculator/)

Link to **my** `repl.it` [click me](https://repl.it/@ueberBrot/probability-calculator#README.md)
