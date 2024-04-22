#!/usr/bin/python3

"""
Compute a database table. Emails which has the attribute FirstName  and Email ID .Given N rows
of data simulating the Emails table, print an alphabetically-ordered list of people whose email 
address ends in @gmail.com.
"""

import math 
import os
import random
import re
import sys



if __name__ == "__main__":
    N = int(input())

    pattern = r"@gmail.com$"

    regex = re.compile(pattern)

    firstNameList = []

    for N_itr in range(N):
        firstNameEMailID = input().split()

        firstName = firstNameEMailID[0]

        emailID = firstNameEMailID[1]

        if regex.search(emailID):
            firstNameList.append(firstName)

    firstNameList.sort()

    for name in firstNameList:
        print(name)

        