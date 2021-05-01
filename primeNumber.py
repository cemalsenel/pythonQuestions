number = input("Enter a number")

while number.isnumeric==False or int(number) <= 2:
    print("Please enter a valid number")
    number = input("Enter a number")

sum = 0
for i in range(1,int(number)+1):
    if int(number)%i == 0:
        sum +=1
if sum== 2:
    print("prime number")
else:
    print("not prime number")