# WAP to check given number is prime or not

# To take input from the user
num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag = True
            break
if flag:
    print(num, 'Number is not a prime')
else:
    print(num, 'Number is a prime')