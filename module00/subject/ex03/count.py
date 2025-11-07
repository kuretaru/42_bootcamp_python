import re
import sys
import string

def text_analyzer_old_ver(text=""):
    if text is None:
        text = input("What is the text to analyze?\n>> ")
    try:
        text_length = len(text)
        count_of_upper_letters = len(re.findall(r'[A-Z]', text))
        count_of_lower_letters = len(re.findall(r'[a-z]', text))
        count_of_punctuation_marks = len(re.findall(r'[^\w\s]', text))
        count_of_separators = len(re.findall(r'[\s]', text))
        print(f"""- {count_of_upper_letters} upper letter(s)\n
- {count_of_lower_letters} lower letter(s)\n
- {count_of_punctuation_marks} punctuation mark(s)\n
- {count_of_separators} space(s)\n""")
    except:
        AssertionError("argument is not a string")

def text_analyzer(text=None):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if text is None:
        text = input("What is the text to analyze?\n>> ")
    if not type(text)==str:
        raise AssertionError("argument is not a string")
    text_length = len(text)
    count_of_upper_letters = sum(1 for char in text if "A" <= char <= "Z")
    count_of_lower_letters = sum(1 for char in text if "a" <= char <= "z")
    count_of_punctuation_marks = sum(1 for char in text if char in string.punctuation)
    count_of_separators = sum(1 for char in text if char.isspace())
    print(f"""- {count_of_upper_letters} upper letter(s)\n
- {count_of_lower_letters} lower letter(s)\n
- {count_of_punctuation_marks} punctuation mark(s)\n
- {count_of_separators} space(s)\n""")

if __name__=="__main__":
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()