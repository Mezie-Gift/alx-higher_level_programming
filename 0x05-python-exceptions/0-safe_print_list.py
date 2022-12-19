#!/usr/bin/python3
# AUTHOR:Mezie Gift
def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list"""
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
