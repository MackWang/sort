#!/usr/bin/python
# sort.py
# collection of sort algorithm


from timeit import timeit


setup = '''
import numpy as np
from copy import copy


LIST_OF_INT = np.random.randint(1000, size=100)


def bubble_sort(list):
    switch = True
    while(switch):
        switch = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True
'''

def main():
    it = timeit('bubble_sort(copy(LIST_OF_INT))', setup, number = 10000)
    print it / 10000


if __name__ == '__main__':
    main()
