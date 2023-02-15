
# offset table
def get_offset_dict(query_string):
    symbols_set = set()
    query_length = len(query_string)
    offset_dict = {}

    for i in range(query_length-2, -1, -1):
        if not query_string[i] in symbols_set:
            offset_dict[query_string[i]] = query_length-i-1
            symbols_set.add(query_string[i])

    if not query_string[query_length - 1] in symbols_set:
        offset_dict[query_string[query_length - 1]] = query_length

    offset_dict['*'] = query_length
    return offset_dict


#print(get_offset_table(query_string))


def bmh_search(string, substring):
    string_length = len(string)
    query_length = len(substring)
    offsets_dict = get_offset_dict(substring)
    if string_length >= query_length:
        i = query_length - 1
        while (i < string_length):
            k = 0
            for j in range(query_length-1, -1, -1):
                if string[i - k] != substring[j]:
                    if j == query_length - 1:
                        offset = offsets_dict[string[i]] if offsets_dict.get(string[i], False) else offsets_dict['*']
                    else:
                        offset = offsets_dict[substring[j]]
                    
                    i += offset
                    break

                k += 1
            if j == 0:
                return i-k+1
    
    else:
        return False

print(bmh_search('titestitat', 'tat'))
