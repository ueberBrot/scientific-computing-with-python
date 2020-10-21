"""
This module uses the function arithmetic_arranger to display aritmethic problems
vertically and if wanted with the solution.
"""


def arithmetic_arranger(problems: list[str], calculate_solution: bool = False) -> str:
    """Display the input problems (max 5) vertically and if wanted with the solution.

    Args:
        problems (list[str]): Input list with problems
        calculate_solution (bool, optional): Value to indicate if a calculated solution
        is wanted. Defaults to False.

    Returns:
        str: Formatted string in a vertically layout
    """
    SPACE: str = " " * 4
    top_row: str = ""
    bot_row: str = ""
    spacers: str = ""
    results: str = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    # loop through the list of problems and apply every operation seperatly
    for problem in problems:
        active_problem = problem.split()
        num_1: str = active_problem[0]
        operator: str = active_problem[1]
        num_2: str = active_problem[2]

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not (num_1.isdecimal() and num_2.isdecimal()):
            return "Error: Numbers must only contain digits."

        if (len(num_1) and len(num_2)) > 4:
            return "Error: Numbers cannot be more than four digits."

        # calculate the length of the longest operand and add 2
        # because of the operator and the needed space
        length: int = max(len(num_1), len(num_2)) + 2
        top: str = num_1.rjust(length)
        bot: str = operator + num_2.rjust(length - 1)
        spacer: str = "-" * length
        result: str = "".rjust(length)

        if calculate_solution:
            # convert the strs to ints and add or sub the operands
            # convert the result back to str
            if operator == "+":
                result = str(int(num_1) + int(num_2)).rjust(length)
            else:
                result = str(int(num_1) - int(num_2)).rjust(length)

        if problem == problems[-1]:
            top_row += top
            bot_row += bot
            spacers += spacer
            results += result
        else:
            top_row += top + SPACE
            bot_row += bot + SPACE
            spacers += spacer + SPACE
            results += result + SPACE

    if calculate_solution:
        arranged_problems: str = (
            top_row + "\n" + bot_row + "\n" + spacers + "\n" + results
        )
    else:
        arranged_problems: str = top_row + "\n" + bot_row + "\n" + spacers

    return arranged_problems
