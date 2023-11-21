
# Factorial of a number
no = int(input("Enter the input: "))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)

fact = 1

while no > 0:
    fact = fact * no
    no = no - 1
print(fact)

for i in range(1, no+1):
    fact = fact * i

print('factorial is ', fact)