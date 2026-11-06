"""
Lab 2.2 – Comprehensions and Transformations
--------------------------------------------
Practice list, set and dictionary comprehensions.

Write these functions. Each one should return a SINGLE comprehension
(one line after `return`), not a for loop that appends:
- squares(numbers)      -> list : the square of each number, same order
- positives(numbers)    -> list : only the numbers greater than 0
                                  (0 is NOT positive), same order
- even_squares(numbers) -> set  : the squares of the EVEN numbers only
                                  (0 and negative even numbers count too)
- cubes(numbers)        -> dict : maps each number to its cube

In the main block: use the list NUMBERS below, call each function and
print the results.

Example run:
    Squares: [9, 64, 4, 49, 0, 25, 100]
    Positives: [3, 8, 7, 10]
    Even squares: {64, 0, 4, 100}      (a set has no fixed order)
    Cubes: {3: 27, 8: 512, -2: -8, 7: 343, 0: 0, -5: -125, 10: 1000}

Examples (these are also used to check your work):
>>> squares([1, -2, 3])
[1, 4, 9]
>>> squares(NUMBERS)
[9, 64, 4, 49, 0, 25, 100]
>>> positives(NUMBERS)
[3, 8, 7, 10]
>>> sorted(even_squares(NUMBERS))
[0, 4, 64, 100]
>>> type(even_squares(NUMBERS))
<class 'set'>
>>> cubes([2, -3])
{2: 8, -3: -27}
>>> squares([]), positives([]), even_squares([]), cubes([])
([], [], set(), {})
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    """Return a list with the square of each number (list comprehension)."""
    return [n ** 2 for n in numbers]


def positives(numbers: list[int]) -> list[int]:
    """Return only the numbers greater than 0 (list comprehension)."""
    return [n for n in numbers if n > 0]


def even_squares(numbers: list[int]) -> set[int]:
    """Return a set of the squares of the even numbers (set comprehension)."""
    return {n ** 2 for n in numbers if n % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    """Return a dict mapping each number to its cube (dict comprehension)."""
    return {n: n ** 3 for n in numbers}


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    print(f"Squares: {squares(NUMBERS)}")
    print(f"Positives: {positives(NUMBERS)}")
    print(f"Even squares: {even_squares(NUMBERS)}")
    print(f"Cubes: {cubes(NUMBERS)}")
