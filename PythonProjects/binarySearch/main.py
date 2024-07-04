import random
import time

def naive_search(l, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

def binarySearch(list, target):
    start = 0
    end = len(list) - 1
    while(start <= end):
        midpoint = start + (end - start) // 2
        if target < list[midpoint]:
            end = midpoint - 1
        elif target > list[midpoint]:
            start = midpoint + 1
        else:
            return midpoint
    return -1

def binaryRecurs(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) -1

    if high < low:
        return -1

    midpoint = low + (high - low)// 2
    if list[midpoint] == target:
        return midpoint
    elif target > list[midpoint]:
        return binaryRecurs(list, target, midpoint+1, high)
    else:
        return binaryRecurs(list, target, low, midpoint-1)

if __name__ == "__main__":
    list = [12, 34, 45, 56, 67, 78, 89, 90, 99, 123, 345, 456, 567,678, 678]
    target = 345
    print(binaryRecurs(list, target))
    