#!/usr/bin/python3
import os
import sys

"""
At the annual meeting of Board of Directors of Acme Inc.
If everyone attending shakes hands exactly one time with
every other attendee, how many handshakes are there?

Example 
n = 3

There are 3 attendees,p1 , p2 and p3 .
p1  shakes hands with p2 and p2, 
and p2 shakes hands with p3 . 
Now they have all shaken hands after 3 handshakes.

Function Description

Complete the handshakes function in the editor below.

handshakes has the following parameter:

int n: the number of attendees

Returns

int: the number of handshakes
"""

def handshake(n):
    # formula to calculate number of handshakes 
    return (n * (n - 1)) // 2

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        print(result)
