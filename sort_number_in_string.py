
# Input: He1llo2worl3d
# Output: He3llo2worl1d
a = 'He1llo2worl3d'


def reverse_numbers_in_string(input_string):
    result = ''
    current_num = ''

    for char in input_string:
        if char.isdigit():
            current_num += char
        else:
            result += char[::-1] if current_num else ''
            result += current_num
            current_num = ''

    result += current_num[::-1] if current_num else ''
    return result


input_str = "He1llo2worl3d"
output_str = reverse_numbers_in_string(input_str)
print("Input:", input_str)
print("Output:", output_str)


