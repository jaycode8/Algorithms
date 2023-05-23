
def swap(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(list):
    pivot_index = 0
    pivot = list[pivot_index]
    start = 1
    end = len(list) - 1
    while start < end:
        while list[start] <= pivot:
            start += 1
        while list[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, list)
    swap(pivot_index, end, list)

def quick_sort(list):
    partition(list)


if __name__ == '__main__':
    elements = [78, 12, 15, 8, 61, 53, 23, 27]
    quick_sort(elements)
    print(elements)