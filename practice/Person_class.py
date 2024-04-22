#!/usr/bin/python3

"""

write a Person class with an instance variable, and a constructor that takes an interger, initail Age,
as a parameter.The constructor must assign initialAge to age, after confirming the argument as initialAge
is not negative, if a negative agrument is passed as initialAge, the constructor should set the age to 0
and print Age is not valid, setting age to 0.You must write the following instance methods:
1. yearPassed() should increase the age instance varaible to 1
2. amIOld()  should perform the following actions:
    . if age < 13, print you are young.
    . if age >= 13 and age < 15, print , You are a teenager.
    . otherwise print you are old
"""

class Person:
    def __init__(self, initial_age):
        if initial_age < 0:
            print("Age is not valid")
            self.age = 0
        else:
            self.age = initial_age
    def amIold(self):
            if self.age < 13:
                 print("you are young")
            elif self.age < 18:
                 print("you are a teenager")
            else:
                 print("you are old")
    def yearpassed(self):
        self.age += 1


Age = int(input().strip())
person = Person(Age)
person.amIold()
