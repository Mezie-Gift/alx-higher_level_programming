#!/usr/bin/python3
# AUTHOR: Mezie Gift
"""Module imports all functions from the file
calculator_1.py and handles basic operations.
"""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    lent = len(sys.argv) - 1
    if lent != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
# Performing additions
    elif sys.argv[2] == '+':
        result = add(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1],
                                     sys.argv[2], sys.argv[3], result))
# Performing subtractions
    elif sys.argv[2] == '-':
        result = sub(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1],
                                     sys.argv[2], sys.argv[3], result))
# Performing multiplications
    elif sys.argv[2] == '*':
        result = mul(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1],
                                     sys.argv[2], sys.argv[3], result))
# Performing divisions
    elif sys.argv[2] == '/':
        result = div(int(sys.argv[1]), int(sys.argv[3]))
        print("{} {} {} = {}".format(sys.argv[1],
                                     sys.argv[2], sys.argv[3], result))
    else:
        print("Unknown operator. Available operator: +, -, * and /")
        sys.exit(1)
