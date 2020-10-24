"""
Category class for working with budgets.

The method create_spend_chart can be used to plot a chart that show the percentage
spent in each category passed in to the function.
The percentage spent is calculated only with the withdrawals and not with deposits.

Calculated is it like the following:
The percentages spent in each category to the total sum spent in all categories.
ref: https://forum.freecodecamp.org/t/scientific-programming-budget-app/414111/2
"""
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Dict,
    List,
    Union,
)


@dataclass
class Category:
    """This class represents budget for a categorie,
    that can be specified during the instantiation.
    """

    # class instance variables
    # because the dataclass decorator is used we get cool perks like
    # a __init__ , __repr__ and a __eq__ method automaticlly created
    categorie: str
    ledger: List[Dict[str, Union[str, int, float]]] = field(default_factory=list)
    # like double entry bookkeeping
    spent: float = 0.0
    income: float = 0.0

    def deposit(self, amount: Union[int, float], description: str = "") -> None:
        """Append a new deposit to the ledger list as a dictionary.

        Args:
            amount (Union[int, float]): Amount of money. No currency symbol.
            description (str, optional): A good description for the deposit.
            Defaults to "".
        """
        self.ledger.append(
            {"amount": round(float(amount), 2), "description": description}
        )
        self.income += amount

    def withdraw(self, amount: Union[int, float], description: str = "") -> bool:
        """Append a withdraw to the ledger. But only if enough funds are available.

        Args:
            amount (Union[int, float]): Amount to withdraw
            description (str, optional): A good description for the withdraw.
            Defaults to "".

        Returns:
            bool: True if the withdraw is possible or flase when it isn't.
        """
        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": round(float(-amount), 2),
                    "description": description,
                }
            )
            self.spent += amount
            self.income -= amount

            return True
        else:
            return False

    def get_balance(self) -> float:
        """Get the stored balance of the ledger.

        Returns:
            float: Current balance.
        """
        return round(float(self.income), 2)

    def transfer(self, amount: Union[int, float], categorie_obj) -> bool:
        """Transfer money to another categorie object.

        Args:
            amount (Union[int, float]): Money to transfer.
            categorie_obj ([type]): Transfer recipient.

        Returns:
            bool: True when the transfere is possible otherwiese false.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {categorie_obj.categorie}")
            categorie_obj.deposit(amount, f"Transfer from {self.categorie}")

            return True
        else:
            return False

    def check_funds(self, amount: Union[int, float]) -> bool:
        """Check if the input value is more or less than the balance.

        Args:
            balance (Union[int, float]): Input balance to check.

        Returns:
            bool: True if the stored balance is more or equal or false when it isn't.
        """
        if self.income >= round(float(amount), 2):
            return True
        else:
            return False

    def __str__(self):
        """String representation of the class object when print(str(class_obj))
        is used.
        """
        titel_row: str = self.categorie.center(30, "*") + "\n"
        items: str = ""

        for entry in self.ledger:
            # take only the first 23 characters of the description if its less or
            # more the length is still fixed to 23
            # the amount is right aligned and a has a max length of 7 inc.
            # 2 decimal point numbers
            items += (
                f"{entry.get('description')[0:23]:23}"
                + f"{entry.get('amount'):>7.2f}"
                + "\n"
            )

        return titel_row + items + "Total: " + f"{self.income:.2f}"


def create_spend_chart(categories: List) -> str:
    """Create a chart that to show the percentage spent in each category passed in to
    the function.
    The percentage spent is calculated only with the withdrawals and not with deposits.

    Args:
        categories (List): List of instantiated Category objects.

    Returns:
        str: Chart in a bar-ish style.
    """
    plot: str = "Percentage spent by category\n"
    # calculate the total of everything spent in all categories
    total_spent: float = sum(x.spent for x in categories)
    # create a list with the percentage values of the spending for every category
    # with the help of the floor division operator
    percentages: List[float] = [(x.spent / total_spent) // 0.01 for x in categories]

    for p_value in range(100, -10, -10):
        plot += str(p_value).rjust(3, " ") + "|"
        for percentage in percentages:
            # if the percentage of the categorie is equal or greater than
            # the percentage value of the row add a new "bar"
            # else append 3 spaces
            if percentage >= p_value:
                plot += " o "
            else:
                plot += " " * 3
        plot += " \n"

    # build the x axis
    plot += " " * 4 + "-" * 3 * len(percentages) + "-\n"
    # calculate the length of the longest categorie
    longest_name: int = max(len(x.categorie) for x in categories)

    for char in range(longest_name):
        # prepend 4 spaces before every row
        plot += " " * 4
        # for every name
        for name in categories:
            # append the char to the row
            if char < len(name.categorie):
                plot += " " + name.categorie[char] + " "
            else:
                # or if no char append 3 spaces
                plot += " " * 3

        plot += " \n"

    # because a new line is appended rstrip() is nessesary
    # or the test failes
    # because rstrip() strips all trailing whitespace
    # 2 whitespaces must be added after the last appended value
    plot = plot.rstrip() + " " * 2

    return plot
