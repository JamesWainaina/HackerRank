#!/usr/bin/python3

"""
Given n names and phone numbers, assemble a phone book that maps friend's names to their
respective phone numbers.You will then be given an unkown number of names to query you phone book.
for each name queried,print the associated entry from your phone book on a new line in the 
form name = phoneNumber. If an entry for name is not found, print Not found instead.

N/B: Your phone book should be  a Dictionary/Map/Hashmap data structure
"""

import sys

n = int(sys.stdin.readline().strip())

phone_book = dict()

for i in range(n):
    entry = sys.stdin.readline().strip().split()
    phone_book[entry[0]] = entry[1]

query = sys.stdin.readline().strip()
while query:
    phone_number = phone_book.get(query)
    if phone_number:
        print(query + '=' + phone_number)
    else:
        print("not found")
    query = sys.stdin.readline().strip()

