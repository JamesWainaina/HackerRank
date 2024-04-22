#!/usr/bin/python3
"""
Given a String of length N  that is indexed from 0 to N - 1. Print its even_indexed characters and 
odd indexed characters as 2 spaced strings on a single line. 
"""

num_test_cases = int(input())


for i in range(num_test_cases):
    test_string = input()
    even_indexed_characters = ''
    odd_indexed_characters = ''

    for j in range(len(test_string)):
        if j % 2 == 0 :
            even_indexed_characters += test_string[j]
        else:
            odd_indexed_characters += test_string[j]
    print("{} {}".format(even_indexed_characters, odd_indexed_characters))
