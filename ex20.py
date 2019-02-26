from sys import argv

# importing file into program
script, input_file = argv

# creating a new function called "print_all" to read the contents of variable "f"
def print_all(f):
    print(f.read())

# new function called rewind to take variable "f" and seek starting character in text file.
def rewind(f):
    f.seek(0)

# Here we are creaing a new function that requires two variables, "line_count" and "f", f will be passed in as a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# here we define our variable, "current_file", and opens the input_file we passed into the argv command at the start of our program
current_file = open(input_file)

print("First let's print the whole file:\n")

# Here we read our "current_file" variable and print it to the console
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Here we find the first (0) character in our file.
rewind(current_file)

# Here we define our new variable, "current_line", and pass it into our new function "print_a_line", which will then
#  output to the console whatever is on the line by using "readline"
current_line = 1
print_a_line(current_line, current_file)

# Here we increase our "current_line" by one and then redefine our variable's value.
current_line += 1
print_a_line(current_line, current_file)

# Here we increase our "current_line" by one and then redefine our variable's value.
current_line += 1
print_a_line(current_line, current_file)
