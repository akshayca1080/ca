#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    new = ""
    for i in s:
        if i != " ":
            new = new + i
    n = len(new)
    a = int(math.sqrt(n))
    if a*a==n:
        b=a
    else:
        b = a + 1
    j = 1
    t = []
    l = []
    dup = ""
    l.append(new[0])
    for i in range(a):
        while j < n:
            if j % b == 0:
                t.append(l)
                l = []
            l.append(new[j])
            j = j + 1
    t.append(l)
    print(t)
    lo = max(len(elem) for elem in t)
    for k in range(lo):
        h = k
        for y in t:
            if h < len(y):
                dup = dup + y[h]
        print(dup, end=" ")
        dup = ""
if __name__ == '__main__':

    s = input()

    encryption(s)

