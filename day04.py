"""

print(print(False and {0} or []))

logic = True and False or not False or False
print(logic)

print([] and "Hello World!")

öncelik sıralaması
1.not
2.and
3.or


text = "clarusway"[5]
print(text)

a = 'merhaba jimmy'
print(a[2:10:])
print(a[2:])
print(a[::-1])
print(a[2:10:2])

fruit = 'Orange'

print('Word                   : ' , fruit)
print('First letter           : ' , fruit[0])
print('Second letter          : ' , fruit[1])
print("3rd to 5th letters     : " , fruit[2:5])
print("Letter all after 3rd   : " , fruit[2:])

city = 'Phoenix'

print(city[1:])  # starts from index 1 to the end
print(city[:6])  # starts from zero to 5th index
print(city[::2])  # starts from zero to end by 2 step
print(city[1::2])  # starts from index 1 to the end by 2 step
print(city[-3:])  # starts from index -3 to the end
print(city[::-1])  # negative step starts from the end to zero

number = input("enter a number")  # <class 'str'>
print(type(number))  # input komutu girdiyi "str" olarak alır. 
                    #iput kullanılırken veri tipi değiştirilmeli
number1 = int(input("enter a number"))
print(type(number1))  # <class 'int'>


name = str(input("What is your name"))
print("Hello " + name)
age = int(input("How old are you?"))
if age >= 70 :
    print("You are aged perfection")
else :
    print("You are a spring chicken!")
 """   
   
for i in range(1,23,1):
    print(i , end = " ") 
    