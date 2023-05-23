
from util import time_it

@time_it
def linear_search(arr,target):
    for index, ele in enumerate(arr):
        if ele == target:
            return index
    return -1


if __name__ == '__main__':
    # list = [0, 1, 6, 12, 34, 65, 76, 89, 123]
    list = [i for i in range(10000)]
    num = 10000
    found_index = linear_search(list, num)
    if found_index == -1:
        print(f'{num} is not present in the list')
    else:
        print(f'{num} is found at position {found_index + 1}')