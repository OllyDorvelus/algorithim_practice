# warmup


def simpleArraySum(ar):
    total = 0
    for num in ar:
        total = total + num
    return total


def compareTriplets(a, b):
    alicePoints = 0
    bobPoints = 0
    for i in range(0, 3):
        if a[i] > b[i]:
            alicePoints += 1
        if a[i] < b[i]:
            bobPoints += 1
    return [alicePoints, bobPoints]


def miniMaxSum(arr):
    min = arr[0]
    max = arr[0]
    minSum = 0
    maxSum = 0
    totalSum = 0
    for num in arr:
        totalSum += num
        if num > max:
            max = num
        if num < min:
            min = num
    minSum = totalSum - max
    maxSum = totalSum - min
    print(f'{minSum} {maxSum}')


def extraLongFactorials(n):
    arr = [0] * n
    arr[0] = 1
    for i in range(1, n):
        arr[i] = (i + 1) * arr[i-1]
    return arr[n-1]
