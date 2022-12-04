#!/usr/bin/python3
# AUTHOR: Mezie Gift

if __name__ == "__main__":
    """ Sum up all arguments"""
    import sys
    sum_num = 0
    for i in range(len(sys.argv) - 1):
        sum_num = sum_num + int(sys.argv[i + 1])
    print("{}".format(sum_num))
