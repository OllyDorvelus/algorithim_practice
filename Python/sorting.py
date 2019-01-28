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


def partition(arr, start_index, end_index):
    pivot = start_index
    border_index = start_index
    for i in range(start_index, end_index + 1):
        if arr[i] < arr[pivot]:
            border_index += 1
            arr[i], arr[border_index] = arr[border_index], arr[i]
    print(arr[border_index])
    arr[pivot], arr[border_index] = arr[border_index], arr[pivot]
    return border_index


def quicksort(arr, start_index, end_index):
    if start_index < end_index:
        pivot = partition(arr, start_index, end_index)
        quicksort(arr, start_index, pivot - 1)
        quicksort(arr, pivot + 1, end_index)


def linearSearch(arr, searchItem):
    for item in arr:
        if item == searchItem:
            return item
    return False


def binarySearch(arr, searchItem):
    lowIndex = 0
    highIndex = len(arr) - 1
    while(lowIndex <= highIndex):
        middleIndex = (highIndex + lowIndex) // 2
        if arr[middleIndex] > searchItem:
            highIndex = middleIndex - 1
        elif arr[middleIndex] < searchItem:
            lowIndex = middleIndex + 1
        else:
            return arr[middleIndex]
    return False


arr_1 = [5, 6, 30, 100]
arr_2 = [2, 7, 15]
print(arr)
print(mergesort(arr))
print(arr)
arr_3 = [n*5 for n in range(1, 11)]
arr_4 = [n*10 for n in arr_3]
print(arr_3)
print(arr_4)
print(binarySearch(arr_3, 50))

arr_5 = [17, 41, 5, 22, 54, 6, 29, 3, 13]
quicksort(arr_5, 0, len(arr_5) - 1)
print(arr_5)
# partition(arr_5, 0, len(arr_5) - 1)
# print(arr_5)
# partition(arr_5, 0, 3)
# print(arr_5)
# partition(arr_5, 0, 2)
# print(arr_5)
# partition(arr_5, 0, 1)
# print(arr_5)
# partition(arr_5, 0, 0)
# print(arr_5)
# partition(arr_5, 5, 8)
# print(arr_5)
# partition(arr_5, 6, 8)
# print(arr_5)
# partition(arr_5, 7, 8)
# print(arr_5)
# partition(arr_5, 8, 8)
# print(arr_5)
