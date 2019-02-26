from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# we could do this on one line, how?
with open(from_file) as fp: in_data = fp.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the ouput file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
