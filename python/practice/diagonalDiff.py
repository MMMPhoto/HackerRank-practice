#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Get length of array
    length = len(arr)
    
    # Define diagonals
    firstDiag = 0
    secDiag = 0
    
    # Loop array first diagonal
    for i in range(len(arr)):
        val = arr[i][i]
        firstDiag += val
    
    j = (len(arr)) - 1
    # Loop array second diagonal
    for i in range(len(arr)):
        val = arr[i][j]
        secDiag += val
        j -= 1
    
    # Calculate difference
    diff = abs(secDiag - firstDiag)
    
    return diff
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
