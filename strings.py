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


print(count_substring("ABCDCDC", "CDC"))
print(split_and_join("this is a string"))
print(mutate_string("abracadabra", 5, "k"))
