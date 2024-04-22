#!/usr/bin/python3

"""
The AdvancedArithmetic interface and the method declaration for the abstruct divisionSum(n) method 
are provided for you in the editor below.
complete the implementation of Calcualtor class, which implements the AdvancedArithmetic interface. 
The implementations for the divisionSum(n) method must return the sum of all divisors of n"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
    
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        running_total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                running_total += i
        return running_total

n = int(input())
mycalculator = Calculator()
s = mycalculator.divisorSum(n)
print("1 implemented:"  + type(mycalculator).__bases__[0].__name__)
print(s)