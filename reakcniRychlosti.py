"""Main script."""


import random
from time import time
import operator


def init():
    """Initialize variables.

    Returns:
        cycles (int)
        results ([int])
        times ([double])
        min (int)
        max (int)
        symbols (string)
        message (string)
    """
    cycles = 5
    results = [None] * cycles
    times = [None] * cycles
    min, max, symbols = -10, 10, "+-*/"
    message = "Answer:"
    return cycles, results, times, min, max, symbols, message


def introduction():
    """Return introductional text.

    Returns:
        intro_text (string): Introductional text.
    """
    return "Welcome, this will test your reaction.\n\nBe ready!"


def generate_equation(min, max, symbols):
    """Generate parts of equation.

    Parameters:
        max (int): Maximal generatable value.
        min (int): Minimal generatable value.
        symbols (string): Set of operators.
    Returns:
        a (int): First part of equation.
        b (int): Second part of equation.
        symbol (char): Math operation symbol used in equation.
    """
    return random.randint(min, max), random.randint(min, max), \
        symbols[random.randint(0, len(symbols) - 1)]


def get_equation(a, b, symbol):
    """Return generated equation.

    Parameters:
        a (int): First part of equation.
        b (int): Second part of equation.
        symbol (char): Math operation symbol used in equation.
    Returns:
        equation (string)
    """
    return str(a) + " " + str(symbol) + " " + str(b)


def get_user_input(message):
    """Wait for user input.

    Parameters:
        message (string): Message displayed when input is asked.
    Returns:
        user_input (int)
    """
    user_input = input(message + " ")
    return int(user_input)


def evaluate(a, b, symbol, user_input):
    """Solve equation and evaluate it against user input.

    Parameters:
        a (int): First part of equation.
        b (int): Second part of equation.
        symbol (char): Math operation symbol used in equation.
        user_input (int): User answer to equation.
    Returns:
        is_correct (bool) : Does solved equation is same as user input?
    """
    operator_map = {"+": operator.add, "-": operator.sub,
                    "*": operator.mul, "/": operator.truediv}
    correct_result = operator_map[symbol](a, b)
    return (correct_result == user_input)


def get_results(results, times):
    """Prints results and times."""
    print(results)
    print(times)


def reakcniRychlosti():
    """Main function."""
    cycles, results, times, min, max, symbols, message = init()
    print(introduction())

    for cycle in range(cycles):
        a, b, symbol = generate_equation(min, max, symbols)
        print(get_equation(a, b, symbol))
        time_start = time()
        user_input = get_user_input(message)
        time_taken = time() - time_start
        results[cycle], times[cycle] =\
            evaluate(a, b, symbol, user_input), time_taken
    get_results(results, time_taken)


if '__main__' == __name__:
    reakcniRychlosti()
