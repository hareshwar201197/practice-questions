# Fibonacci series

# number = int(input("Enter your number : "))
#
# # First two terms
# n1 = 0
# n2 = 1
# count = 0
#
# while count <= number:
#     print(count)
#     n1 = n2
#     n2 = count
#     count = n1 + n2

# string1 = 'Hellow World'

# vowels = ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']
#
# for vowel in vowels:
#     if vowel in string1:
#         string1 = string1.replace(vowel, '*')
#
# print(string1)


string1 = 'He1llo2worl3d'
str_num = []
for num in string1:
    if num.isdigit():
        str_num.append(num)

updated_num_list = str_num[::-1]
for num in string1:
    if num.isdigit():
        if updated_num_list:
            for index, number in enumerate(updated_num_list):
                print(index)
                string1 = string1.replace(num, number)
                #print(string1)

print(string1)

