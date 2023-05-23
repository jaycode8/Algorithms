
from util import time_it

@time_it
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1



if __name__ == '__main__':
    # list = [0,1,6,12,34,65,76,89,123]
    # num = 12
    list = [i for i in range(10000)]
    num = 10000
    found_index = binary_search(list, num)
    if found_index == -1:
        print(f'{num} is not present in the list')
    else:
        print(f'{num} is found at position {found_index+1}')
