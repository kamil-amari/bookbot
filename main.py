from stats import count_characters, count_words


def get_book_text(book_path: str) -> str:
    with open(book_path, 'r') as book:
        return book.read()

def print_record(word_count: int, character_count: dict) -> str:
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for k, v in character_count:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    
    print("--- End of the report ---")


if __name__ == "__main__":
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)

    print_record(word_count, character_count)