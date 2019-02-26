from sys import argv

script, filename = argv

target = open(filename, 'w+')

print(f"This is the current file that is open: {filename}.")
print(target.read())

print("Now we are going to delete the file.")
target.truncate()

print("Now I'm going to ask you for three lines: ")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("Now let's write these lines to our file...")

target.write(line1 + "\n" + line2 + "\n" + line3)

print("Now let's close our file.")
target.close()
