import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    # Capitalize in Python - HackerRank Solution START
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s
    # Capitalize in Python - HackerRank Solution END

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
