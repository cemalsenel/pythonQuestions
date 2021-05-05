text = ['one','two','three','four','five']
numbers = [1, 2, 3, 4, 5]
city=["Los Angeles", "Beirut", "Tokyo","rome","Istanbul"]
for x, y in zip(text, numbers):
    print(x, '=', y)
    
print(* zip(text, numbers,city)) # ('one', 1, 'Los Angeles') ('two', 2, 'Beirut') ('three', 3, 'Tokyo') ('four', 4, 'rome') ('five', 5, 'Istanbul')
print(list(zip(text, numbers,city))) # [('one', 1, 'Los Angeles'), ('two', 2, 'Beirut'), ('three', 3, 'Tokyo'), ('four', 4, 'rome'), ('five', 5, 'Istanbul')]


odd=[]
even = []

for i in range(1,11) :
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print(odd)
print(even)


example =[0,0,1,5,45,11,2,24,61,48,33,3]
evens=0
odds=0
for i in example:
    if  i % 2 ==0 :
        evens +=1
    else:
        odds +=1
print(f"The number of even numbers : {evens}")
print(f"The number of odd numbers : {odds}")


for i in range(1,10):
    print(i*str(i))

sum=0
for i in range(1,75):
    sum=sum+i
print(sum)


who = ["I am ","You are "]
mood = ["happy","confident"]

for i in who:
    for j in mood:
        print(i + j)


names = ["susan", "tom", "edward"] 
mood = ["happy", "sad"]
for i in names:
    for j in mood:
        print(i,j)

nums=[1,2,3,4,5,6,7,8,9]
print([i**2 for i in nums if i %2 ==1])

total = 0
[total := total + x for x in nums]
print(total)

total1 = 1
[total1 := total* x for x in nums if x %2 ==1]
print(total1)


line = 10
print()
for i in range(line):
    print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
for i in range(line*2-7):
    print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
for i in range(5):
    print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)








