#!/usr/bin/python3

"""
you are given two classes Person and Student, where Person is the base class,
and Student is the derived class.

complete the student class by writing the following:
. A student classs constructor, which has 4 parameters:
        1. A string, fistName.
        2. A string , lastName.
        3. An integer, int
        4. An integer array (or vector) of test scores, scores

. A chief calculator() method that calculates a student objects average and 
returns the grade character representative of their calculated average.

use this chart:
Letter    Average
O         90 <= a <= 100
E         80 <= a < 90
A         70 <= a < 80
P         55 <= a < 70
D         40 <= a < 55
T         a < 40
"""

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name", self.lastName + "," , self.firstName)
        print("10:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def calculate(self):
        sum = 0
        for score in scores:
            sum += score
        average = sum /len(scores)

        if average < 40:
            return 'T'
        elif average < 55:
            return 'D'
        elif average < 70:
            return 'P'
        elif average < 80:
            return 'A'
        elif average < 90:
            return 'E'
        else:
            return 'O'
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade", s.calculate())