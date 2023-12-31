
string1 = 'Hellow World'

vowels = ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']

for vowel in vowels:
    if vowel in string1:
        string1 = string1.replace(vowel, '*')

print(string1)