#!/usr/bin/python3

n = int(input().strip())

if n % 2 == 1:
    print("wierd")
elif n < 5:
    print("not wierd")
elif n <= 20:
    print("wierd")
else:
    print("not wierd")


