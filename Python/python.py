# SORTING ALGORITHS 

# -----------------BUBBLE SORT-----------------
def bubbleSort(ls):
    count = 0
    # while True:
    #     count += 1
    #     print(count)
    for i in range(len(ls)):
        flag = True
        count += 1
        print(count)
        for j in range(i+1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
                flag = False
        if flag:
            return ls

# -----------------SELECTION SORT-----------------
def selectionSort(ls):
    for i in range(len(ls)):
        Min = i
        for j in range(i+1, len(ls)):
            if ls[j] < ls[Min]:
                Min = j
        ls[Min], ls[i] = ls[i], ls[Min]
    return ls



# ---------------------INSERTION SORT---------------------

def insertionSort(ls):
    for i in range(len(ls)):
        j = i
        k = i-1
        while ls[k] > ls[j] and k >= 0:
            ls[k], ls[j] = ls[j], ls[k]
            k -= 1
            j -= 1
    return ls



# -------------------------MERGE SORT---------------------------

def join(ls, mid, l, h):
    print('--------------------------')
    print(ls, l, h)
    arr = []
    arrA = ls[l:mid+1]
    arrB = ls[mid+1:h+1]
    i, j = 0, 0
    print(arrA, arrB)
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1
    while i < len(arrA) or j < len(arrB):
        if i < len(arrA):
            arr.append(arrA[i])
            i += 1
        else:
            arr.append(arrB[j])
            j += 1
    print(arr)
    for i in range(l, h+1):
        ls[i] = arr.pop(0)
    return ls


def mergeSort(ls, low, high):
    if low < high:
        mid = (low+high)//2
        mergeSort(ls, low, mid)
        mergeSort(ls, mid+1, high)
        join(ls, mid, low, high)
        return ls
