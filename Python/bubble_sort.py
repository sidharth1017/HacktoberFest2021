
def bubble_sort(lst):
    length = len(lst) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(length):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False
    return lst
print(bubble_sort([7, 10, 4, 3, 20, 15]))
