
# Factorial of a number
no = int(input("Enter the input: "))

fact = 1

while no > 0:
    fact = fact * no
    no = no - 1
print(fact)