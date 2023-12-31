
# palindrome number
def palindrome5(n):
    temp = n
    rev_n = 0
    while temp>0:
        digit = temp % 10
        
        rev_n = rev_n * 10 + digit
        temp = temp // 10
    if n == rev_n:
        return True
    else:
        return False
p = palindrome5(121)
print(p)

# def palindrome1(number):
#     n = len(number)
#     for i in range(n):
#         if number[i] != number[n-i-1]:
#             return False
#         return True
# p = '212'
# print(palindrome1(p))

# def palindrome3(number):
#     temp = ''.join(reversed(number))
#     if number == temp:
#         return True
#     else:
#         return False
# p = '454'
# print(palindrome3(p))

def palindrome4(number):
    n = len(number)
    first = 0
    last = n-1
    while first<last:
        if number[first] == number[last]:
            first += 1
            last -= 1
        else:
            return False
    return True

c = '232'
print(palindrome4(c))



# def palindrome(number):
#     temp = number[::-1]
#     if number==temp:
#         print("Yes! it is palindrome number" )
#     else:
#         print("NO its not palindrome number")
#
# number = "121"
# palindrome(number)


