"""
Task 3 – Function with Combined Logic
-------------------------------------
Write a function `analyze_sentence(text)` that returns a tuple of three values,
in this order:
1. total character count of the text exactly as given, spaces included (len)
2. word count, where words are separated by whitespace (.split())
3. True if "python" appears anywhere in the text, ignoring case, else False
   (a simple substring check: "Pythonic" and "PYTHON!" both count)

Return type: (int, int, bool)

In the main block: read a sentence, call the function, and print a summary.

Example run:
    Enter a sentence: I love Python
    Characters: 13
    Words: 3
    Contains 'Python': True

Examples (these are also used to check your work):
>>> analyze_sentence("I love Python")
(13, 3, True)
>>> analyze_sentence("  Hello   world  ")
(17, 2, False)
>>> analyze_sentence("PYTHONIC code!")
(14, 2, True)
>>> analyze_sentence("")
(0, 0, False)
"""


def analyze_sentence(text: str) -> tuple[int, int, bool]:
    """Return (length, word count, contains 'python') for the given text."""
    character_count = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()

    return character_count, word_count, contains_python


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    characters, words, contains_python = analyze_sentence(sentence)

    print(f"Characters: {characters}")
    print(f"Words: {words}")
    print(f"Contains 'Python': {contains_python}")
