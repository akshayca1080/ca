

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(n, m):
    while n <= m:
        y = n * n
        d = len(str(n))
        t = []
        r = []
        l = []
        new = str(y)
        for i in new:
            t.append(i)
        if len(new) > 1:
            r = t[len(new) - d:]
            p = t[:len(new) - d]
            new = ""
            dup = ""
            for i in r:
                dup = dup + i
            for i in p:
                new = new + i
            k = int(new) + int(dup)
            if k == n:
                print(k,end=" ")
        else:
            if n == y:
                print(n,end=" ")
        n = n + 1



if __name__ == '__main__':
    n = int(input())

    m = int(input())

    kaprekarNumbers(n, m)
