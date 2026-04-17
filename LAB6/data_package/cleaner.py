def remove_duplicates(data_list):
    return list(dict.fromkeys(data_list))

def strip_whitespaces(string_list):
    return [item.strip() for item in string_list]