#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""module prints test with two new line"""


def text_indentation(text):
    """prints a text with 2 new lines after each
                 of these characters: ., ? and :
    args:
        test: prints a text.
    Errors:
        text must be a string else a TypeError is raised.
    """
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
