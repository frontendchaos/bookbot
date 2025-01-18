def get_contents(file_path):
    retval = None
    with open(file_path) as f:
        retval = f.read()
    return retval
   
def count_words(file_path):
    contents = get_contents(file_path)
    retval = len(contents.split())
    # print(f"{retval} words in file {file_path}")
    return retval

def count_chars(file_path):
    contents = get_contents(file_path)
    lower_contents = contents.lower()
    retval = {}
    for char in lower_contents:
        if char in retval:
            retval[char] += 1
        else:
            retval[char] = 1
    return retval

def main():
    book_path = "books/frankenstein.txt"
    # chars = count_chars(book_path)
    print(count_chars(book_path))
    

main()