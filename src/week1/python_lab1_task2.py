"""
Task 2 – Greeting Function with String Manipulation
---------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces at the start and end with .strip()
- capitalizes the first letter with .capitalize()
  (note: .capitalize() also makes the REST of the string lowercase)
- returns exactly: "Hello, <Name>! Welcome to Python!"
- if the name is empty (or only spaces), uses "Stranger" as the name

In the main block: ask the user for their name and print the greeting.

Example run:
    Enter your name:   alice
    Hello, Alice! Welcome to Python!

Examples (these are also used to check your work):
>>> greet_user("alice")
'Hello, Alice! Welcome to Python!'
>>> greet_user("   bob  ")
'Hello, Bob! Welcome to Python!'
>>> greet_user("anna MARIE")
'Hello, Anna marie! Welcome to Python!'
>>> greet_user("   ")
'Hello, Stranger! Welcome to Python!'
"""


def greet_user(name: str) -> str:
    """Return a greeting message after cleaning and capitalizing the name."""
    # TODO: implement cleaning, the empty-name case, and formatting
    cn = name.strip()
    if not cn:
        cn = "stranger"
    else:
        cn = cn.capitalize()
    return f"Hello, {cn}! Welcome to Python!"
    raise NotImplementedError("greet_user() is not implemented yet")


if __name__ == "__main__":
    # Keep all input() calls inside this block, otherwise the autograder
    # cannot import your file.
    # TODO: read name from input and print greeting
    ui = input("Enter your name: ")
    print(greet_user(ui))
    pass
