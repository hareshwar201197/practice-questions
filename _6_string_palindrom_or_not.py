# given string is palindrom or not 

str1 = input("Enter your string : ")
str2 = reversed(str1)

if (list(str1) == list(str2)):
    print("Given string is palindrom ")
else:
    print("Given string is not palindrom ")

    