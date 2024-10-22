def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_numeral = ""
    for i in range(len(val)):
        while num >= val[i]:
            roman_numeral += syms[i]
            num -= val[i]
    return roman_numeral

def is_palindrome(s):
    return s == s[::-1]

def main():
    number = int(input("Enter an integer to convert to Roman numeral: "))
    roman_numeral = int_to_roman(number)
    print(f"Roman numeral for {number} is: {roman_