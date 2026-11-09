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
    name = name.strip()

    if not name:
        name = "Stranger"
    else:
        name = name.capitalize()

    return f"Hello, {name}! Welcome to Python!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet_user(name))