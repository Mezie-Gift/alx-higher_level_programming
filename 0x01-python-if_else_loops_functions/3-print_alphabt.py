#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z') + 1):
    if alphabet == ord('e') or alphabet == ord('q'):
        continue
    print("{:c}".format(alphabet), end="")
