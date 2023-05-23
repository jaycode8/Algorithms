
def bubble_sort(list, key=None):
    size = len(list)
    for i in range(size-1):
        swapped = False
        for j in range(size-i-1):
            a = list[j][key]
            b = list[j+1][key]
            if a > b:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [
        {"name": "James", "transaction_price": 20000, "device": "iphone"},
        {"name": "Hilton", "transaction_price": 10000, "device": "samsung"},
        {"name": "Phill", "transaction_price": 7600, "device": "redmi"},
        {"name": "John", "transaction_price": 20000, "device": "iphone"},
        {"name": "Ole", "transaction_price": 6700, "device": "xiaomi"},
        {"name": "Ally", "transaction_price": 5600, "device": "techno"},
        {"name": "Rony", "transaction_price": 15000, "device": "techno"}
    ]
    bubble_sort(elements, key='device')
    print(elements)