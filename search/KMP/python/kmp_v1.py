searching_string = "tatati"


def get_table(query_string):
    table = [0]*len(query_string)
    j = 0
    i = 1

    while i < len(query_string):
        if query_string[j] == query_string[i]:
            table[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                table[i] = 0
                i += 1
            else:
                j = table[j-1]
    return table

def get_table2(query_string):
    table = [0]*len(query_string)
    j = 0
    i = 1

    for i in range(1, len(query_string)):
        if query_string[j] == query_string[i]:
            table[i] = j + 1
            j += 1
        else:
            if j == 0:
                table[i] = 0
            else:
                j = table[j-1]
    return table

# print table
#print(get_table2(searching_string))


def kmp_search(string, substring):
    table = get_table(substring)
    string_length = len(string)
    substring_length = len(substring)
    i = 0
    j = 0

    while i < string_length:
        if string[i] == substring[j]:
            i += 1
            j += 1
            if j == substring_length:
                return True
        else:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
    return False

print(kmp_search('testets', 'etts'))