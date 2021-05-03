number = input("Enter a number")

while number.isnumeric==False or int(number) <= 2:
    print("Please enter a valid number")
    number = input("Enter a number")

check = True
prime=[]
for i in list(range(2,int(number)+1)):
    for j in list(range(2, int(i))):
          if i % j == 0:
            check = False
    if check == False:
        check = True
    else:
        prime.append(i)    
print(prime)
        
