"""
Lab 2.4 – Functional Tools Practice
-----------------------------------
Practice map(), filter() and zip(), and compare them with comprehensions.

IMPORTANT: map(), filter() and zip() do not return lists. They return
"lazy" objects (printing one shows something like <map object at 0x...>).
Wrap the result in list(...) before returning it.

Part A – functional style (use the tool named for each function):
- item_totals(prices, quantities)   -> list
    Use map() with a lambda to compute price * quantity for each item.
    Hint: map() can take two lists: map(lambda p, q: ..., prices, quantities)
- filter_above(totals, threshold=30) -> list
    Use filter() with a lambda to keep only totals GREATER than threshold.
- pair_up(prices, quantities)        -> list of tuples
    Use zip() to pair each price with its quantity.

Part B – the same with list comprehensions:
- item_totals_comp(prices, quantities)    -> list
    Same result as item_totals(). Hint: [... for p, q in zip(prices, quantities)]
- filter_above_comp(totals, threshold=30) -> list
    Same result as filter_above().

All functions keep the original order of the items.

In the main block: use PRICES and QUANTITIES below, call every function
and print the results. Which style do you find easier to read?

Example run:
    Totals: [25.0, 49.5, 15.0, 66.9, 20.0]
    Totals > 30: [49.5, 66.9]
    Price-quantity pairs: [(12.5, 2), (9.9, 5), (15.0, 1), (22.3, 3), (5.0, 4)]
    Totals (comprehension): [25.0, 49.5, 15.0, 66.9, 20.0]
    Totals > 30 (comprehension): [49.5, 66.9]

Examples (these are also used to check your work):
>>> item_totals(PRICES, QUANTITIES)
[25.0, 49.5, 15.0, 66.9, 20.0]
>>> filter_above([25.0, 49.5, 15.0, 66.9, 20.0])
[49.5, 66.9]
>>> filter_above([5, 10, 15], threshold=8)
[10, 15]
>>> pair_up([1.5, 2.0], [3, 4])
[(1.5, 3), (2.0, 4)]
>>> item_totals_comp(PRICES, QUANTITIES) == item_totals(PRICES, QUANTITIES)
True
>>> filter_above_comp([5, 10, 15], threshold=8)
[10, 15]
>>> type(item_totals(PRICES, QUANTITIES))
<class 'list'>
"""

PRICES = [12.5, 9.9, 15.0, 22.3, 5.0]
QUANTITIES = [2, 5, 1, 3, 4]


# ---------- Part A: functional style ----------

def item_totals(prices: list[float], quantities: list[int]) -> list[float]:
    """Return price * quantity for each item, using map() and a lambda."""
    # TODO: implement with map()
    raise NotImplementedError("item_totals() is not implemented yet")


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    """Return totals greater than threshold, using filter() and a lambda."""
    # TODO: implement with filter()
    raise NotImplementedError("filter_above() is not implemented yet")


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:
    """Return a list of (price, quantity) tuples, using zip()."""
    # TODO: implement with zip()
    raise NotImplementedError("pair_up() is not implemented yet")


# ---------- Part B: list comprehensions ----------

def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:
    """Same as item_totals(), but with a list comprehension."""
    # TODO: implement with a list comprehension
    raise NotImplementedError("item_totals_comp() is not implemented yet")


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:
    """Same as filter_above(), but with a list comprehension."""
    # TODO: implement with a list comprehension
    raise NotImplementedError("filter_above_comp() is not implemented yet")


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.
    # TODO: call every function with PRICES and QUANTITIES and print results
    pass
