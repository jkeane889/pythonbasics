class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            # for "x" in range (1 // 1,000) <--- 1,000 is the first value in list "val"
            for _ in range(num // val[i]):
                roman_num += syb[i] # <--- add the symbol from list "syb" to the string "roman_num" if the floor division equals  whole number
                num -= val[i] # <--- then, subtract the value from the "val" list from our number
            i += 1 # <--- increase our interator by 1 and continue to run the loop
        return roman_num # <--- once the value of num is less than zero, return numnW


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(2456))
