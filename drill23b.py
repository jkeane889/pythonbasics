import sys

script = sys.argv

# Here we create a new function to pass in a text file, an encoding type, and an error type
def main(language_file):

    # Here we read the line of characte rs in the text file that is passed through into our "main" function
    line = language_file.readline()

    # The if statement tests with boolean logic to see that a line is present (or = TRUE)
    if line:
        print(">> there's a line", repr(line))
        # If a line is present, this will run the next function, "print_line"
        print_line(line)
        print(">> calling main again")
        return main(language_file)

# This is a separate function that will intake 3 variables; a "line" of text, the encoding type, and then the error type
def print_line(line):
    next_lang = bytes(line, "utf-8").decode("unicode_escape")
    print(">>>> ", repr(next_lang))
    print(next_lang)

languages = open("blank_languages.txt", mode='r', encoding='utf-8')
print(">>>> ", repr(languages))

main(languages)
