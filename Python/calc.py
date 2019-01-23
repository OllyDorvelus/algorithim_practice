

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y


my_list = [1, 2, 3, 4, 5]
squares = [num*num for num in my_list if num > 3]
print(squares)

my_dict = {"p": 0}
my_dict["p"] += 1
print(my_dict["p"])
print(my_dict.get("p"))
print(my_dict.get("c"))
