def by_2(val):
    val = val * 2


def by_2_obj(obj):
    obj.val *= 2


def changeFirst(arrVal):
    arrVal = arrVal * 10


arr = [3, 6, 10]


class sample:
    def __init__(self):
        self.val = 100


x = 100
print(x)
by_2(x)
print(x)
my_s = sample()
print(my_s.val)
by_2(my_s.val)
print(my_s.val)
print(arr[0])
changeFirst(arr[0])
print(arr[0])
