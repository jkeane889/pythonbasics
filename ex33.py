i = 0
numbers = []
increment = 2

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + increment
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
