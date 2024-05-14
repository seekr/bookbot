def main():
    book_path = "books/frankenstein.txt" # take file
    text = get_book_text(book_path) # use func defined below on file and store it as var

    word_count = count_words(text)
    letter_count = count_letters(text)

    print_report(book_path, word_count, letter_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    char_count = {}
    lowercase = text.lower()
    for char in lowercase:
      if char.isalpha():
        if char in char_count:
          char_count[char] += 1
        else:
          char_count[char] = 1

    # Sort dict
    sorted_char_count = {}
    max_value = max(char_count.values())
    for value in range(max_value, 0, -1):
      for key in list(char_count.keys()):
        if char_count[key] == value:
          sorted_char_count[key] = value
          del char_count[key]

    return sorted_char_count

def get_book_text(path):
    with open(path) as f:
      return f.read()

def print_report(book_path, word_count, letter_count):
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print(f" ")
  for k, v in letter_count.items():
    print(f"The '{k}' character was found {v} times")
  print(f"--- End report ---")

main()
