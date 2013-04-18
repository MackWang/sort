#!/usr/bin/python
# sort.py
# collection of sort algorithm

# import for quick testing
import numpy as np


# constant for quick test
LIST_OF_INT = np.random.randint(1000, size=100)


def bubble_sort(list):
    '''Bubble sort'''
    switch = True
    while(switch):
        switch = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True


def bubble_sort_opt(list):
    '''Bubble sort - nth pass finds nth largest item'''
    n = len(list)
    switch = True
    while(switch):
        switch = False
        for i in range(n-1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True
        n = n - 1


def bubble_sort_opt2(list):
    '''Bubble sort - multiple items can be placed on final
    spot in the same pass
    '''
    n = len(list)
    while(n != 0):
        newn = 0
        for i in range(0, n - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                newn = i + 1
        n = newn


def main():
    pass


if __name__ == '__main__':
    main()
