#!/usr/bin/python3
# AUTHOR: Mezie Gift
def safe_print_division(a, b):
    """function  divides 2 integers and prints the result """
    ans = 0
    try:
        ans = a / b
    except (ZeroDivisionError, TypeError):
        ans = None
    finally:
        print("inside result: {}".format(ans))
        return (ans)
