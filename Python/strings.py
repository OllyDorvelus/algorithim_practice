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


def reverse(string):
    char_arr = list(string)
    start = 0
    end = len(char_arr) - 1
    print(char_arr)
    while(start < end):
        char_arr[start], char_arr[end] = char_arr[end], char_arr[start]
        end -= 1
        start += 1
    return "".join(char_arr)


print(reverse("below"), "below")


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


def longest_sub_string(s):
    hash_map = {}
    max = 0
    count = 0
    clash_index = 0
    for i in range(0, len(s)):
        if s[i] in hash_map:
            if clash_index < hash_map[s[i]]:
                clash_index = hash_map[s[i]]
            count = i - clash_index
            hash_map[s[i]] = i
        else:
            hash_map[s[i]] = i
            count += 1
        if count > max:
            max = count
    return max


def is_palindrome(s):
    start_index = 0
    end_index = len(s) - 1
    while(start_index <= end_index):
        if(s[start_index] != s[end_index]):
            return False
        start_index += 1
        end_index -= 1
    return True


def pop(stack):
    if stack:
        return stack.pop()
    return None


def balance_parentheses(s):
    stack_arr = []
    for char in s:
        if char in ['(', '{', '[']:
            stack_arr.append(char)
        if char == ')' and pop(stack_arr) != '(':
            return False
        elif char == '}' and pop(stack_arr) != '{':
            return False
        elif char == ']' and pop(stack_arr) != '[':
            return False

    if stack_arr:
        return False
    return True


ones_arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens_arr = ['', '', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundreds_arr = ['', 'one-hundred', 'two-hundred',
                'three-hundred', 'four-hundred', 'five-hundred', 'six-hundred', 'seven-hundred', 'eight-hundred', 'nine-hundred']


def number_to_word(n):
    empty_string = ''
    space_stirng = ' '
    if 0 <= n < 20:
        return ones_arr[n]
    elif 20 <= n < 100:
        return f'{tens_arr[n // 10]}{space_stirng + ones_arr[n % 10] if n % 10 != 0 else empty_string}'
    elif 100 <= n < 1000:
        return f'{hundreds_arr[n // 100]}{space_stirng + tens_arr[n % 100 // 10] if n % 100 != 0 else empty_string}{space_stirng + ones_arr[n % 100 % 10] if n % 100 % 10 != 0 else empty_string}'


print(balance_parentheses(')))'), 'balance')
print(len("") - 1)
print(is_palindrome(""), 'palindrome')
print(longest_sub_string('abcdaf'))
print(longest_sub_string('abcc'))
print('\n')
print(longest_sub_string('abba'))
print(longest_sub_string('abcabcbb'))
for i in range(0, 1000):
    print(number_to_word(i))
# print(number_to_word(17))
# print(number_to_word(20))
# print(number_to_word(999))
