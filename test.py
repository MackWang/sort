#!/usr/bin/python
# test.py
# test the various sort algorithms


from timeit import timeit


setup = '''
import numpy as np
from copy import copy
from sort import bubble_sort

LIST = np.random.randint(1000, size=100)
'''


NUMBER_OF_SORTS = 1000


def main():
    print "Running bubble_sort()..."
    t  = timeit('bubble_sort(copy(LIST))', setup, number = NUMBER_OF_SORTS)
    print "Average sort time : %f" % (t / NUMBER_OF_SORTS)


if __name__ == '__main__':
    main()
