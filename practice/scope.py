#!/usr/bin/python3

"""
The absolute difference between two integers, a and b is written as [a - b]. The maximum absolute 
difference between two integers in a set of positive integers, elements, in the largest absolute 
difference between the two integers in elements.
Task:

Complete the Difference class has the following:
. A class constructor that takes an array of integers as a parameter and saves it to the elements 
instance variable.
. A computeDifference() method that finds the maximum absloute difference between any 2 numbers 
in N and stores it in the maximumDifference variable. 
"""

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximum_difference = 0
    
    def computeDifference(self):
        min_element = 101
        max_element = 0
        for element in self.__elements:
            if element < min_element:
                min_element = element
            if element > max_element:
                max_element = element

        self.max_abs_diff = max_element - min_element

_ = input()
a = [int(a) for a in input().strip(' ')]

d = Difference(a)
d.computeDifference()
print(d.max_abs_diff)

