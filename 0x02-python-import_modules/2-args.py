#!/usr/bin/python3
# AUTHOR: Mezie Gift

"""a program that prints the number of and the list of its arguments"""
if __name__ == "__main__":
    import sys
    lent = len(sys.argv)
    if lent <= 1:
        print("0 arguments.")
    else:
        if lent == 2:
            print("{:d} argument:".format(lent - 1))
        else:
            print("{:d} arguments:".format(lent - 1))
        for i in range(1, lent):
                print("{:d}: {}".format(i, sys.argv[i]))
