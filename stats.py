def get_book_words_count(book_text):
    num_words = 0
    for word in book_text.split():
        num_words += 1
    return num_words

def count_characters(book_text):
    char_counts = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(char_counts):
    return char_counts["num"]

def sort_char_counts(char_counts_dictionary):
    char_counts_list = []
    for character, count in char_counts_dictionary.items():
        small_dict={"char": character, "num": count}
        char_counts_list.append(small_dict)
    char_counts_list.sort(reverse=True, key=sort_on)
    return char_counts_list