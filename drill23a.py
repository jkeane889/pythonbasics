import sys

# Here we create a new function to pass in a text file, an encoding type, and an error type
def main(language_file, error):

    # checking inputs to main
    print(">>>> ", repr(language_file))

    def write_bytes(from_file, to_file, error):
        print(">>>> ", repr(from_file), repr(to_file))
        # Here we read the line of characte rs in the text file that is passed through into our "main" function
        line = from_file.readline()

        # The if statement tests with boolean logic to see that a line is present (or = TRUE)
        if line:
            print_line(from_file, to_file, line, error)
            return write_bytes(from_file, to_file, error)

    # This is a separate function that will intake 3 variables; a "line" of text, the encoding type, and then the error type
    def print_line(from_file, to_file, line, error):
        next_lang = line.strip()
        raw_bytes = next_lang.encode('utf-8', errors=error)
        write_byte = repr(raw_bytes)
        to_file.write(write_byte)
        to_file.write("\n")

    # Creating confirmation function to determine if the file is the correct file the user wants to open.
    def confirmation_of_file(input_file, output_file, error):
        print(">>>> ", repr(input_file), repr(output_file))
        print(f"Is {output_file} the correct file you want to write data to? (Enter Y/N)")
        confirm = input()
        if confirm == "Y":
            print("Thank you. Writing to file...\n")
            write_bytes(input_file, output_file, error)
        elif confirm == "N":
            extraction_file()
        else:
            print("That is not a value, please enter a correct value.")
            confirmation_of_file(input_file, output_file, error)
        print(f"{output_file} is now prepared.\n")

    print("What is the file you would like to write the data to?")
    file_name = input()
    target_file = open(file_name, mode = 'w')

    confirmation_of_file(language_file, target_file, error)

def choose_encode(aList):
    # here we are asking what kind of decoding that would prefer
    print("""What type of input coding are you looking to use?
    \nOption 1 (enter #1): UTF-8
    \nOption 2 (enter #2): UTF_16
    \nOption 3 (enter #3): UTF-32
    \nOption 4 (enter #4): Big5")\n""")
    print("> ")
    encoding_type = int(input())

    # Here we pass the value of the list "aList" into our while loop; if the value of the "aList" is equal to zero, we begin the while loop
    while len(aList) == 0:
        # here we say if the encoding type equals 1, we then add that to our list in position "0"
        if encoding_type == 1:
            print("You have selected UTF-8.\n")
            aList.append("utf-8")
            return aList
        # here we say if the encoding type equals 2, we then add that to our list in position "0"
        elif encoding_type == 2:
            print("You have selected UTF-16.\n")
            aList.append("utf-16")
            return aList
        # here we say if the encoding type equals 3, we then add that to our list in position "0"
        elif encoding_type == 3:
            print("You have selected UTF-32.\n")
            aList.append("utf-32")
            return aList
        # here we say if the encoding type equals 4, we then add that to our list in position "0"
        elif encoding_type == 4:
            print("You have selected Big5.\n")
            aList.append("big5")
            return aList
        # here we say if the encoding does not equal 1 through 4, we then begin our while loop again
        else:
            print("Please select an option between 1 and 4.\n")
            choose_encode(aList)

def extraction_file():
    # first we are asking the user for the languages file to extract our bytes from
    print("What file do you want to extract from?")
    new_file = input()
    selected_encoding = []
    error = "strict"

    choose_encode(selected_encoding)
    new_encoding = selected_encoding[0]

    print(f"""{new_file} is where you are extracting data from, {selected_encoding[0]} is the encoding you have selected, and {error} is the error type\n.""")

    extract_file = open(new_file, encoding=new_encoding)
    main(extract_file, error)

extraction_file()
