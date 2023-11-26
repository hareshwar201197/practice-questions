# Fibonacci series

number = int(input("Enter your number : "))
  
# First two terms  
n1 = 0  
n2 = 1  
count = 0  
  
while count <= number:
    print(count)
    n1 = n2
    n2 = count
    count = n1 + n2