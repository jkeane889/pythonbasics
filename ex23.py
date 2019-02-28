import sys
script, input_encoding, error = sys.argv

# Here we create a new function to pass in a text file, an encoding type, and an error type
def main(language_file, encoding, errors):


    print(">>>> main", repr(language_file), encoding, errors)
    # Here we read the line of characte rs in the text file that is passed through into our "main" function
    line = language_file.readline()

    # The if statement tests with boolean logic to see that a line is present (or = TRUE)
    if line:
        print(">> there's a line", repr(line))
        # If a line is present, this will run the next function, "print_line"
        print_line(line, encoding, errors)
        print(">> calling main again")
        return main(language_file, encoding, errors)
    print("<<<< exit main")

# This is a separate function that will intake 3 variables; a "line" of text, the encoding type, and then the error type
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
