def find(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_del = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_del.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_del = list(set(index_to_del))
        index_to_del.sort()
        if index_to_del:
            for i in index_to_del[-1::-1]:
                del arr[i]
            div *= 2
            n = len(arr)
            gap = n//div


def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap >0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >=gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    elements = [23,1,4,88,76,1,45,3,8,0]
    shell_sort(elements)
    # find(elements)
    print(elements)
    # test_case = [
    #     [3, 98, 56, 4, 0],
    #     [],
    #     [9],
    #     [10, 6, 5, 3, 2, 1],
    #     [5, 7, 12, 0, 4],
    #     [34, 56, 77, 88, 98, 111]
    # ]
    # for elements in test_case:
    #     shell_sort(elements)
    #     print(elements)