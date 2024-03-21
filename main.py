lower_case_alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def main():    
    number_words()
    character_count()
    print(get_book_text("./books/frankenstein.txt"))

def number_words():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
        print(f'Book has {len(file_content.split())} words!')

def sort_on(list):
    return list[1]

def character_count():
    character_dictionary = {}
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
    words = file_content.split()
    for word in words:
        for char in word.lower():
            if char in lower_case_alpabet and char in character_dictionary:
                character_dictionary[char]+=1
            elif char in lower_case_alpabet:
                character_dictionary[char] = 1
    sorted_values = list(character_dictionary.items())
    sorted_values.sort(reverse = True, key=sort_on)
    for item in sorted_values:
        print(f'The {item[0]} character was found {item[1]} times')
    print("--End report--")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
    





main()