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
    print list


def main():
    bubble_sort([34, 8, 3, 5, 6, 4, 2, 3, 4, 7, 98, 1000, 4, 2, 7, 8, 45])


if __name__ == '__main__':
    main()
