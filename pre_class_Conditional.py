"""
empty_seat = 14
if empty_seat >3:
   print("There is still seat to sit")
   
x = 6
y = 9
print ("is x equal to y?                 :" , x == y)
print ("is x not equal to y?             :" , x != y)
print ("is x less than y?                :" , x < y)
print ("is x greater than y?             :" , x > y)
print ("is x less than or equal to y?    :" , x <= y)
print ("is x greater than or equal to y? :" , x >= y)

course = 'clarusway'

if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")

number = 5
if number <= 3:    
    print("Number is smaller than or equal to 3") 
else:  # Optional clause (you can only have one else)
    print("Number is bigger than 3")
    
weight = 80

if weight > 100:
    print("That's too heavy!")
elif weight > 75:
    print("I can lift that!")
else:
    print("That's too light!")
    
audience = "baby"

if audience == "kid":
    print("it is free to go to cinema")
elif audience == "teen":
    print("discounted price!")
elif audience == "adult":
    print("normal price")
else:
    print("No such audience, stay at your home!")
    

answer = int(input(print("Enter a number")))
if answer >= 15 :
    print("it is great")
elif answer >=5 :
    print("one more time")
else :
    print("try again")

audience_group = 'kid', 'teen', 'adult'

audience = "teen"

if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")
    
score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
else:
    Score_letter="below B"

print ("Your degree: %s" % Score_letter)

city = "samsun"

if city == "samsun" \
    or city == "trabzon" :
        print("Wooowww!!!")
elif city == "izmir":
    print("Whattt!")
else :
    print("Whatever")

city = "antalya"
if city in ("samsun", "trabzon","izmir"):
    tax = 100
elif city == "antalya":
    tax = 75
else:
    tax =0
print(tax)

# LOOPS

number = 0

while number < 6:
    print(number)
    number += 1
print('now, number is bigger or equal to 6')

my_list=["a", "b", "c", "d", "e"]
a = 0
while a < len(my_list):
    print('square of {} is : {}'.format(a, a**2))
    a+=1

answer = 28
question = 'What number am I thinking of?  '
print ("Let's play the guessing game!")

while True:
    guess = int(input(question))

    if guess < answer:
        print('Little higher')
    elif guess > answer:
        print('Little lower')
    else:  # guess == answer
        print('Are you a MINDREADER!!!')
        break

flowers = ['Rose', 'Orchid', 'Tulip']
count1 = len(flowers)
count2 = 0

while count1>0 :
    print(flowers[count2],end="\n")
    count1 -= 1
    count2 += 1

for i in [1, 2, 3, 4, 5] :
    print(i)
    
seasons = ['spring', 'summer', 'autumn', 'winter']

for season in seasons :
    print(season)

for i in {'n1' : 'one', 'n2' : 'two'} : print(i)

iterable = [1, 2, 3, 4]
for i in iterable : print((i**2),end="\n")

course = 'clarusway'
for i in course :
    print(i)

times = int(input("How many times should I say 'I love you'"))
for i in range(times):
    print('I love you')


n = int(input('enter a number between 1-10'))
for i in range(11):
    print('{}x{} = '.format(n, i), n*i) # ==> % ile print() i yeniden yaz
    
c = tuple(range(11))
print(c)

a = set(range(0,10))
print(a)

b = list(range(11))
print(b)

print(range(5))  # it will not print the numbers in sequence => range(0, 5)

print(*range(5))  # '*' separates its elements => 0 1 2 3 4

print(*range(5,25,2)) # 5 7 9 11 13 15 17 19 21 23
print(*('separate')) # s e p a r a t e
print(*range(10,0,-2)) # 10 8 6 4 2

text = ['one','two','three','four','five']
numbers = [1, 2, 3, 4, 5]
for x, y in zip(text, numbers): # zip() function make an iterator that aggregates elements from each of the iterables.
    print(x, ':', y)

a = 3
while a**2 < 299:
    print('I will stop smoking')
    a += 3

total = 149
country = "FR"

if country == "FR":
    if total <= 50:
        print("Shipping Cost is  €30")
    elif total <= 100:
        print("Shipping Cost is €15")
    elif total <= 150:
        print("Shipping Costs €10")
    else:
        print("Free Shipping")
if country == "DE": 
    if total <= 50:
        print("Shipping Cost is  €25")
    else:
        print("Free Shipping")

saved_amount = int(input('Please enter your saved amount: '))
ps4_price = 150

if saved_amount > ps4_price:
     print("Yippee! You can buy your PS4")
elif saved_amount > ps4_price/2 :
     print("You saved more than half, keep saving!")
elif saved_amount <= ps4_price/2 :
     print("You must save more, keep saving!")
     


math_mark = int(input('Please enter the mark: '))
if math_mark>=85 :
    print("A (Excellent)")
elif math_mark >= 70:
    print("B (Good)")
elif math_mark >= 60 :
    print("C (Medium)") 
elif math_mark >= 45 :
    print("D (Not Bad)")
elif math_mark >=0 :
    print("F (Failed)")
a = 998
if a >= 999 :
    print(a ** 0)  

else :
    print(a * 2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in range(len(weekdays)):
    print('Day', day+1, ':', weekdays[day])

month = "April"
spring = "September, April, January"
autumn = "March, October, July"
if (month in spring) or (month in autumn):
    if month in autumn:
        print("This is a spring month")
    else:
        print("This is an autumn month")
else:
    print("This month is not categorized")
  
number = int(input('Please enter a number: '))
i = 0;
while i < number:
    print(i**2)
    i = i+1
 
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
    print("The type of",i,"is",type(i))
""" 





         
