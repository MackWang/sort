#!/usr/bin/python
# sort.py
# collection of sort algorithm


def bubble_sort(list):
    switch = True
    while(switch):
        switch = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True


def bubble_sort_opt(list):
    n = len(list)
    switch = True
    while(switch):
        switch = False
        for i in range(n-1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                switch = True
        n = n - 1


def main():
    pass


if __name__ == '__main__':
    main()
