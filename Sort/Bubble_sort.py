
def bubble_sort(list):
    size = len(list)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    # list = [23,1,4,88,76,45,3,8,0]
    list =['James','Ian','Ann']
    bubble_sort(list)
    print(list)