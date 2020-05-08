#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    s=n//c
    d=s
    while d//m>0:
        s=s+d//m
        k=d%m
        d=d//m+k
    print(s)


if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        chocolateFeast(n, c, m)

