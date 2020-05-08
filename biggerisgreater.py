
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    a = "abcdefghijklmnopqrstuvwxyz"
    l = []
    p = []
    r = []
    t=[]
    count = 0
    for i in w:
        if i in a:
            l.append(a.index(i))
    l.reverse()
    for i in range(1):
        j = i + 1
        while j < len(l)-1:
            if l[j] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
                count = count + 1
                break
            j = j + 1
        if count != 0:
            break
    print(j)
    r = l[:j]
    t=[l[j]]
    p = l[j:]
    print(r)
    print(p)
    r.sort()
    print(r)
    r.reverse()
    print(r)
    r.extend(p)
    r.reverse()
    print(r)
    if count == 0:
        print("no answer")

    else:
        for i in r:
            print(a[i], end="")
        print()
if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        biggerIsGreater(w)

