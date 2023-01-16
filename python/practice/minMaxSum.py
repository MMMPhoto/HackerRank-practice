#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Get max and min nums
    maxNum = max(arr)
    minNum = min(arr)
    # Remove min and max
    minArray = arr.copy()
    maxArray = arr.copy()
    minArray.remove(maxNum)
    maxArray.remove(minNum)
    # Sum of arrays
    minSum = sum(minArray)
    maxSum = sum(maxArray)
    
    print(f'{minSum} {maxSum}')
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
