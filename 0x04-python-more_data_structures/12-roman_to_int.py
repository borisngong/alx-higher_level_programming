#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    digit_values = [roman_values[digit] for digit in roman_string] + [0]
    total = 0

    for i in range(len(digit_values) - 1):
        current_value = digit_values[i]
        next_value = digit_values[i+1]

        if current_value >= next_value:
            total += current_value
        else:
            total -= current_value

    return total
