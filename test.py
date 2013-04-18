#!/usr/bin/python
# test.py
# test the various sort algorithms

from timeit import timeit


setup = '''
import numpy as np
from copy import copy
from sort import bubble_sort, bubble_sort_opt, bubble_sort_opt2

LIST = np.random.randint(1000, size=100)
'''


NUMBER_OF_SORTS = 1000


def main():
    print "Running bubble_sort()..."
    t = timeit('bubble_sort(copy(LIST))', setup, numbe=NUMBER_OF_SORTS)
    print "Average sort time : %f" % (t / NUMBER_OF_SORTS)
    print
    print "Running bubble_sort_opt()..."
    t = timeit('bubble_sort_opt(copy(LIST))', setup, number=NUMBER_OF_SORTS)
    print "Average sort time : %f" % (t / NUMBER_OF_SORTS)
    print
    print "Running bubble_sort_opt2()..."
    t = timeit('bubble_sort_opt2(copy(LIST))', setup, number=NUMBER_OF_SORTS)
    print "Average sort time : %f" % (t / NUMBER_OF_SORTS)
    print


if __name__ == '__main__':
    main()
