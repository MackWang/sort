#!/usr/bin/python
# test.py
# test the various sort algorithms

import numpy as np
import copy
import sort


LIST = np.random.randint(1000, size=100)


def test(list):
    copylist = copy.copy(list)
    sort.bubble_sort(copylist)


def main():
    print LIST
    test(LIST)


if __name__ == '__main__':
    main()
