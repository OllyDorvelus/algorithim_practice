class HashMap:
    def __init__(self):
        self.size = 64
        self.map = [None] * 64

    def hash_function(self, key):
        index = len(key)
        return index

    def add(self, key, value):
        keyValue = [key, value]
        index = self.hash_function(key)
        if self.map[index]:
            for pair in self.map[index]:
                if(pair[0] == key):
                    pair[1] = value
                    return
            self.map[index].append(keyValue)
            return
        self.map[index] = list([keyValue])

    def get(self, key):
        index = self.hash_function(key)
        if self.map[index]:
            for pair in self.map[index]:
                if pair[0] == key:
                    value = pair[1]
                    return value
        return None


my_hash = HashMap()
my_hash.add("apple", 4)
my_hash.add("orange", 6)
my_hash.add("orange", 10)
my_hash.add("123456", 30)
print(my_hash.hash_function("123456"))
print(my_hash.hash_function("orange"))
print(my_hash.get("123456"))
print(my_hash.get("orange"))
print(my_hash.get("apple"))
# arr = [0, 1]
# arr[0] = keyValue
# arr[0] = list([keyValue])
# print(arr[0])
# # arr = [[["pear", 1.75], ["apple", 2.00]], [2, 3, 4, 5]]
# # arr[0].append(["cabbage", 10.00])
# # for i in arr[0]:
# #     print(i[1])

# # 'beannn'

arr2 = []
arr2.append(3000)
print(arr2[0])
