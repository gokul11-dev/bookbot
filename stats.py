def get_text_words(text):
    list_words = text.split()
    return len(list_words)

def get_char_count(text):
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def get_sorted_count(count_dict):
    list_count_dict = []
    for char in count_dict:
        char_dict = {}
        char_dict["char"] = char
        char_dict["count"] = count_dict[char]
        list_count_dict.append(char_dict)
    list_count_dict.sort(reverse=True, key=sort_on)
    return list_count_dict

def sort_on(dict):
    return dict["count"]