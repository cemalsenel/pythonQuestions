"""
km= float(input("Enter distance in kilometer : "))
mile = (km * 0.62)
print('%.2f Kilometer is equal to : %.2f Miles' %(km,mile))


celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(celsius,"celsius" ," is equal to ",fahrenheit,"fahrenheit")

num1  = float(input("Enter first number : "))
num2  = float(input("Enter second number : "))
num3  = float(input("Enter third number : "))
multi = num1*num2*num3
print("Multiplication is equal to : " , multi)

height = float(input("Enter your height in float : "))
weight = float(input("Enter your weight: "))
bmi = weight/(height ** 2)
print("BMI : " , bmi)


totalMoney = 200
materialPrice = 11
piece = 200 // 11
remainingMoney = totalMoney % piece
print("With your ${}, {} pieces of material you can get for ${} each.  The remaining money is ${}".format(totalMoney, piece, materialPrice, remainingMoney))




x = float(input("Enter a number"))
y = float(input("Enter a number"))
x,y = y,x
print(x,y)

x= 5
y = 4
z  = x ** 2 - y ** 2
print(z ** 0.5)


word = str(input("Enter a word"))
separator = str(input("Enter a seperator"))
repeat = int(input("Enter a repetition number"))
print((word + separator) * (repeat-1 ) + word)

print(True and False and (not True and False) and not (True or False))# ==> False
  #  True and False and  False and not True
   # True and False and  False and False
   # False
print(True and False and not "False" and None and ("None" or None))# ==> False
# True and False and False and None and True
# False

print("clarusway" and 0 and not "" and False and (" " or None)) # ==> 0
 # kendisine dönüyor. değerine değil
 


age = False  # Are you a cigarette addict older than 75 years old??
chronic = True  # Do you have a severe chronic disease?
immune = False  # Is your immune system too weak ?
risk = print(immune or chronic or age)


print('hello', '-how', 'are', '-you')
print('hello', 'how', 'are-', 'you' + '-' * 4)
print('hello-' + 'how-are-you')
print('hello' + '-' + 'how' + '-' + 'are' + 'you')


age= int(input("Enter your age"))
immune = input("Do you have a severe chronic disease? Y/N")
if immune.lower()=="yes":
  immune = True
elif immune.lower() == "no":
      immune =False
chronic=input("Is your immune system too weak? Y/N")
if chronic.lower()=="yes":
      chronic = True
elif chronic.lower() == "no":
      chronic =False

if age<75 :
      age = False
elif age >= 75 :
      age = True  

risk = (age or immune) and (age or chronic) and (immune or chronic)
if risk == True :
      print("You are in risk group") 
elif risk == False :
      print("You are not in risk group but be careful")



year = int(input("Enter a year"))
a = ((year % 4 == 0 and year % 100 == 0) and (year % 400 == 0) and True) 

print(a)

text = list("A B C D E".split())
text2 = text
text2.insert(0,"X")
print(text) # ['X', 'A', 'B', 'C', 'D', 'E']
"""


text = list("A B C D E".split())
text2 = list(text)
text2.insert(0,"X")
print(text) # ['A', 'B', 'C', 'D', 'E']

gender = input("Are you male? (Yes/No) ").title().strip() == "Yes"
print(gender)



      
