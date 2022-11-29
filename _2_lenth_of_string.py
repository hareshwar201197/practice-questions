# WAP to find length of the string

# using len function
# str = input("Enter your string : ")
# print(len(str))


# using for loop
# str = input("Enter your string :")
# def findLen(str):
#     counter = 0
#     for i in str:
#         counter += 1
#     return counter
# print(findLen(str))

# ussing while loop

# str = input("Enter the string :")
# def findlen(str):
#     counter = 0
#     while str[counter:]:
#         counter +=1
#     return counter
# print(findlen(str))


# using Reduce Method

import functools
string = input("Enetr your string : ")
def findlen(string):
    return functools.reduce(lambda x,y: x+1,string,0)
print(findlen(string))

