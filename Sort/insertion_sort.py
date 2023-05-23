
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i-1
        while j>=0 and anchor<elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor

if __name__ == '__main__':
    test_case = [
        [3, 98, 56, 4, 0],
        [],
        [9],
        [10, 6, 5, 3, 2, 1],
        [5, 7, 12, 0, 4],
        [34, 56, 77, 88, 98, 111]
    ]
    for arr in test_case:
        insertion_sort(arr)
        print(arr)