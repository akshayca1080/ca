#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the workbook function below.
def workbook(n, k, arr):
    l = []
    for i in arr:
        p = 1
        while p <= i:
            h = []
            t = 1
            while t <= k and p<=i:
                h.append(p)
                p = p + 1
                t = t + 1
            l.append(h)
    count=0
    u=1
    for j in l:
       if u in j:
           count=count+1
       u=u+1
    print(count)


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    workbook(n, k, arr)

