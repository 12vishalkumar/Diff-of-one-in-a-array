#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'pickingNumbers' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def pickingNumbers(a):
    # Write your code here
    c = 0
    a.sort()
    L = len(a)
    for i in range(L):
        for j in range(n):
            if(abs(a[i]-a[j])<=1):
                c = max(c, j-i+1) 
    return c   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()
