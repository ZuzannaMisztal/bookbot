from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    counter = Counter(text)
    return counter

def print_report(book_path):
    result = [f"--- Begin report of {book_path} ---\n"]
    text = get_book_text(book_path)
    word_count = count_words(text)
    result.append(f"{word_count} words found in the document\n\n")
    char_count = count_chars(text)
    result.append(char_report(char_count))
    result.append("\n--- End report ---\n")
    print("".join(result))



def char_report(char_count):
    result = []
    for char, times in char_count.most_common():
        if char.isalpha():
            result.append(f"The '{char}' character was found {times} times")
    return '\n'.join(result)

main()