num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
num3 = float(input("Enter the third number"))

if(num1 > num2 ) and (num1 > num3) :
    largest = num1 
elif(num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest=num3
print("The largest number is : ",largest)


num4 = float(input("Enter a number"))
if(num4 > 0) :
    print("Number is bigger than zero")
elif(num4 == 0):
    print("Number is equal to zero")
else:
    print("The number is negative")

score = float(input("Enter your score : "))

if score >= 90 : 
    if score >= 95 :    
        degree = "A+"
    else:
        degree = "A" 
elif score >= 80 :
    if score >= 85 :
        degree = "B+"
    else:
        degree = "B"
else:
    degree = "B-"
print("Your degree is :", degree )

age = input ("Enter your age:")
while True :
    if age.strip().isdigit() :
      print ("You entered valid age :", age)
    elif age.lstrip("+-").isdigit():
      print ("Negative age is imposible:", age)
    else:
      print (age, "is not a number")
    break




