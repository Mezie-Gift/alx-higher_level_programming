#!/usr/bin/python3
# AUTHOR: Mezie Gift
if __name__ == "__main__":

    import hidden_4
    names = dir(hidden_4)
    for check in names:
        if check[:2] != '__':
            print(check)
