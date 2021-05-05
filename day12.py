# SET 
a = set("philadelphia")
print(a)
b = set("dolphin")
print(a - b)  # same as ‘.difference()’ method
print(a.difference(b)) # a difference from b
print(a | b)  # same as ‘.union()’ method
print(a.union(b)) # unification of a with b
print(a & b)  # same as ‘.intersection()’ method
print(a.intersection(b)) # intersection of a and b
a.remove("p") # we delete ‘p’ from the set
print(a)
a.add("p") # we add ‘p’ again into the set
print(a)

date ="04/14/2021"
y = list("04/14/2021")
print(y) # ['0', '4', '/', '1', '4', '/', '2', '0', '2', '1']
print(set(date)) # {'1', '0', '4', '/', '2'}

x={"04/14/2021"}
print(x,type(x)) # {'04/14/2021'} <class 'set'>

given_list = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5]
print(set(given_list)) # {1, 2, 3, 4, 5}

a1 = set("Washington")
b1 = set("Wellington")
print(a1) # {'i', 'n', 'g', 'h', 'o', 's', 'a', 'W', 't'}
print(b1) # {'i', 'n', 'g', 'o', 'l', 'e', 'W', 't'}
print(a1.intersection(b1)) # {'i', 'g', 'W', 't', 'o', 'n'}
print(b1.intersection(a1)) # {'n', 't', 'g', 'W', 'i', 'o'} =>  " & "
print(a1.union(b1)) # {'i', 'a', 'g', 'W', 'e', 's', 't', 'o', 'n', 'l', 'h'}
print(b1.union(a1)) # {'n', 't', 'g', 'e', 'a', 'W', 'h', 'l', 'i', 's', 'o'} => " | "
print(a1.difference(b1)) # {'a', 'h', 's'}
print(b1.difference(a1)) # {'l', 'e'} => " - "


# Conditional Flow
if True :
    print("it is true")

if 1 : # None, 0 , {} , (), [] (boş collectionlar vb. falsy oluyor), 1 ise truthy oluyor
    print("ben") # kod çalışır
    
print("You entered :",input("Enter Yes or No :").title().strip()=="Yes")

num = int(input("Enter a number"))

if(num %2 == 0) :
    print(num ," is even")
else:
    print(num," is odd")

num = float(input("Enter a number"))
if(num>0):
    print("positive")
else:
    print("negative number")


num1 = float(input("Enter a number"))
num2 = float(input("Enter a number"))
if(num1>num2):
    print(num1," is greater")
else:
    print(num2 , " is greater")





