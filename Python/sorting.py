# Sorting algorithims

arr = [8, 3, 10, 11, 12, 5, 100, 40, 31]


def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def bubble_sort_desc(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(0, i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


def selection_sort_desc(arr):
    for i in range(0, len(arr)):
        maxIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        selection = i
        while arr[selection] < arr[j] and j > -1:
            arr[selection], arr[j] = arr[j], arr[selection]
            selection -= 1
            j -= 1


def merge(arr_1, arr_2):
    newarr = []
    index_1 = 0
    index_2 = 0
    while index_1 < len(arr_1) and index_2 < len(arr_2):
        if arr_1[index_1] < arr_2[index_2]:
            newarr.append(arr_1[index_1])
            index_1 += 1
        else:
            newarr.append(arr_2[index_2])
            index_2 += 1
    while index_1 < len(arr_1):
        newarr.append(arr_1[index_1])
        index_1 += 1

    while index_2 < len(arr_2):
        newarr.append(arr_2[index_2])
        index_2 += 1

    return newarr


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftarr = mergesort(arr[:mid])
    rightarr = mergesort(arr[mid:])
    return merge(leftarr, rightarr)


arr_1 = [5, 6, 30, 100]
arr_2 = [2, 7, 15]
print(arr)
print(mergesort(arr))
print(arr)
