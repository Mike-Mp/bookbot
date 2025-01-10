def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_count = get_char_count(file_contents)
        print(word_count)
        print_char_count(char_count)

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    count = {}
    for char in text:
        if char.lower() not in count and char.isalpha():
            count[char.lower()] = 1
        elif char.isalpha():
            count[char.lower()] += 1

    return count

def print_char_count(count):
    char_list = []
    
    for k,v in count.items():
        new_dict = {"letter": k, "count": v}
        char_list.append(new_dict)

    
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")

def sort_on(dict):
    return dict["count"]


main()
