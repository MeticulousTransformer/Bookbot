alphabet = "abcdefghijklmnopqrstuvwxyz"

def main():
    book_path = "Books/frankenstein.txt"
    book = read_book(book_path)
    word_count = get_words_count(book)
    char_count = char_counter(book)
    dict_list = list_of_dicts(char_count)
    print(f'da and {word_count} is word count of frankenstein book')
    for dict in dict_list:
        for key, value in dict.items():
            print(f'The {key} character was found {value} times')
    print("--- End report ---")





def read_book(book_path):
    with open(book_path) as f:
        return f.read()


def get_words_count(book):
    words = book.split()
    return len(words)


def char_counter(string):
    char_dict = { }
    for char in string.lower():
        if char in alphabet and char in char_dict:
            char_dict[char] += 1
        else:
            if char in alphabet:
               char_dict[char] = 1
    return char_dict


def sort_on(dict):
    for i in dict.keys():
        return dict[i]

def list_of_dicts(bigdict):
    dict_list = []
    for key,value in bigdict.items():
        dict_list.append({key: value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


main()