#!/usr/bin/env python3

""" implementation of simple bubble sort algorithm
"""

import random
import sys

def bubble_sort(input_list):
    sorted_list = input_list 
    switched = True

    while switched:
        switched = False
        
        for counter in range(0, len(sorted_list)-1):
            a = sorted_list[counter]
            b = sorted_list[counter+1]
            if a > b:
                a, b = b, a
                switched = True
                sorted_list[counter] = a
                sorted_list[counter+1] = b

    return sorted_list


def randomize_list(items, limit):
    """ create randomized list of integers """
    random_list = []

    while len(random_list) < items:
        rand_num = random.randrange(0, limit)
        if not rand_num in random_list:
            random_list.append(rand_num)

    return random_list


def main():
    if len(sys.argv) != 3:
        print('Please enter [amount] and [max], e.g. 10 100')
        return

    amount = int(sys.argv[1])
    max = int(sys.argv[2])

    my_list = randomize_list(amount, max)
    print('Original list', my_list)
    sorted = bubble_sort(my_list)
    print('Sorted list', sorted)


if __name__ == '__main__':
    main()


""" HOWTO get it done:

    * take list and compare 1st and 2nd element
    * if first is bigger, switch them 
    * else keep the order

"""
