def get_contents(file_path):
    retval = None
    with open(file_path) as f:
        retval = f.read()
    return retval
   
def count_words(input_str):
    retval = len(input_str.split())
    return retval

def count_chars(input_str):
    lower_contents = input_str.lower()
    retval = {}
    for char in lower_contents:
        if not char.isalpha():
            pass
        elif char in retval:
            retval[char] += 1
        else:
            retval[char] = 1
    return retval

def sort_on(dict):
    return dict["count"]

def generate_report(file_path):
    # if file = None, error out.
    # should try/catch this.
    contents = get_contents(file_path)
    
    retval = "--- Begin report of " + file_path + " ---\n"
    word_count = count_words(contents)
    retval += f"{word_count} words found in the document\n\n"
    char_count = count_chars(contents)
    all_char_counts = []
    for char in char_count:
        entry = {"char":char, "count":char_count[char]}
        all_char_counts.append(entry)
    all_char_counts.sort(reverse=True, key=sort_on)
    for kvp in all_char_counts:
        retval += f"The '{kvp["char"]}' character was found {kvp["count"]} times\n"
    retval += "--- End Report ---\n"
    return retval

def main():
    book_path = "books/frankenstein.txt"
    # contents = get_contents(book_path)
    report = generate_report(book_path)
    print(report)
    

main()