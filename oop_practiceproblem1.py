# OOP Practice problems in Python

# https://www.w3resource.com/python-exercises/class-exercises/

class Roman:

    roman_numerals = {
        'I' : 1,
        'II' : 2,
        'III' : 3,
        'IV' : 4,
        'V' : 5,
        'VI' : 6,
        'VII' : 7,
        'VIII' : 8,
        'IX' : 9,
        'X' : 10,
        'XI' : 11,
        'XII' : 12,
        'XIII' : 13,
        'XIV' : 14,
        'XV' : 15,
        'XVI' : 16,
        'XVII' : 17,
        'XVIII' : 18,
        'XIX' : 19,
        'XX' : 20,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }

    def __init__ (self, new_integer):
        roman_number = ''
        max_key = max(Roman.roman_numerals.keys(), key=(lambda k: Roman.roman_numerals[k]))
        max_value = Roman.roman_numerals[max_key]
        self.new_integer = new_integer
        while new_integer > 0:
            if new_integer - max_value >= 0:
                multiple = new_integer // max_value
                print(">>>> ", repr(multiple))
                new_value = (multiple * [max_key])
                roman_string = ''.join(map(str, new_value))
                print(">>>> romanstring=", repr(roman_string))
                roman_number = roman_number + roman_string
                print(">>>> roman_number=", repr(roman_number))
                new_integer = new_integer - (multiple * max_value)
                print(">>>> ", repr(new_integer))
            else:
                Roman.roman_numerals.pop(max_key)
                max_key = max(Roman.roman_numerals.keys(), key=(lambda k: Roman.roman_numerals[k]))
                max_value = Roman.roman_numerals[max_key]

        print(roman_number)

New_Roman = Roman(2456)
