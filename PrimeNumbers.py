number = input("Enter a number")

while number.isnumeric==False or int(number) <= 2:
    print("Please enter a valid number")
    number = input("Enter a number")

sum = 0
prime=[]
for i in list(range(2,int(number)+1)):
    for j in list(range(2, int(i))):
          if i % j == 0:
            sum +=1
    if sum > 0:
        sum = 0
    else:
        prime.append(i)    
print(prime)
        
