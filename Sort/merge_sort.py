
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)  #------------ recursive
    merge_sort(right)

    return merge_two_sorted_list(left, right, arr)

def merge_two_sorted_list(a,b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

if __name__ == '__main__':
    # arr = [5,7,13,56,0,3,15,77]
    test_case = [
        [3,98,56,4,0],
        [],
        [9],
        [10,6,5,3,2,1],
        [5,7,12,0,4],
        [34,56,77,88,98,111]
    ]
    for arr in test_case:
        merge_sort(arr)
        print(arr)
