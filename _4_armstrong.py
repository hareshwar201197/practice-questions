# Armstrong number or not
# logic--> 153=1*1*1 + 5*5*5 + 3*3*3 = 153
num = int(input("Enter your armstrong number:"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum +=digit ** order
    temp //= 10

if num == sum:
    print("is a Armstrong number ",num)
else:
    print("is not a Armstrong number",num)

