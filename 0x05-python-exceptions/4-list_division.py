#!/usr/bin/python3
# AUTHOR: Mezie Gift
def list_division(my_list_1, my_list_2, list_length):
    """function divides elements of my_list_1 by elements of my_list_2 lists"""
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return (new_list)
