#!/usr/bin/python
# sort.py
# collection of sort algorithm

import numpy as np
from timeit import timeit


LIST_OF_INT = np.random.randint(1000, size=100)


def bubble_sort(list):
    switch = True
    while(switch):
        switch = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True


def main():
    it = timeit('bubble_sort(LIST_OF_INT)', 'from __main__ import bubble_sort;\
                                             from __main__ import LIST_OF_INT')
    print it


if __name__ == '__main__':
    main()
