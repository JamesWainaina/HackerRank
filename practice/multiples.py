#!/usr/bin/python3
n = int(input().strip())
# printing the multiples of i untill 10.
for i in range (1, 11):
    product = n * i
    print("{} * {} = {}".format(n, i, product))