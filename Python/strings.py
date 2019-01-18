# String Algorithims

# returning count of substring (hacker-rank)


def count_substring(string, substring):
    count = 0
    string = string.lower()
    substring = substring.lower()
    for index in range(0, len(string)):
        if string[index:index + len(substring)] == substring:
            count = count + 1
    return count


def split_and_join(line):
    strings = line.split(" ")
    joined_string = ("-").join(strings)
    return joined_string


def mutate_string(string, position, characters):
    list_string = list(string)
    list_string[position: position + len(characters)] = characters
    final_string = ("".join(list_string))
    return final_string


def string_properties(string):
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for char in string:
        if char.isalnum():
            isalnum = True
        if char.isalpha():
            isalpha = True
        if char.isdigit():
            isdigit = True
        if char.islower():
            islower = True
        if char.isupper():
            isupper = True

    print("True") if isalnum else print("False")
    print("True") if isalpha else print("False")
    print("True") if isdigit else print("False")
    print("True") if islower else print("False")
    print("True") if isupper else print("False")


def capitalize(s):
    string_list = s.split(" ")
    for index, string in enumerate(string_list):
        if string.isalpha():
            string_list[index] = string.title()
    final_string = (" ").join(string_list)
    return final_string


def print_formatted(number):
    width = len(f"{number:{0}b}")
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


def word_order():
    pass


def minion_game(string):
    kevin_points = 0
    stuart_points = 0
    vowels = ('A', 'E', 'I', 'O', 'U')

    for index, char in enumerate(string):
        if(char in vowels):
            points_from_char = len(string) - index
            kevin_points += points_from_char
        else:
            points_from_char = len(string) - index
            stuart_points += points_from_char

    if(stuart_points > kevin_points):
        print(f'Stuart {stuart_points}')
    elif(stuart_points < kevin_points):
        print(f'Kevin {kevin_points}')
    else:
        print('Draw')


print(count_substring("ABCDCDC", "CDC"))
print(split_and_join("this is a string"))
print(mutate_string("abracadabra", 5, "k"))
string_properties("qA2")
print(capitalize("chris alan"))
# print_formatted(17)
ex = 'BANANA'

minion_game(ex)
