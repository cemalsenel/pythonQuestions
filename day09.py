number = [1,4,7]
number.insert(2,False)  # insert istenilen sıraya eleman ekliyor
# number.insert(3, [54]) normalde kabul ediyor
print(number)
number.append(5)  # elemeanı sona ekler
print(number)
number.insert(4,5) 
print(number)

x = [True,False]
x.sort()
print(x)

list1= ["one","four","nine"]
list1.sort()
print(list1)
list2=["@","*-","False"]
list2.sort()
print(list2)
list3=[[3],[44],[-12]]
list3.sort()
print(list3)
list4 = [[1,3],[44,-40],[-12,1]]
list4.sort()
print(list4)

y = [[1,"bir"],[-1,"iki"],[3,"üc"]]
y.sort()
print(y)#[[-1, 'iki'], [1, 'bir'], [3, 'üc']]
y.sort(reverse = True) 
print(y)# [[3, 'üc'], [1, 'bir'], [-1, 'iki']]

print(ord("F")) # 70
print(ord("*")) # 42
print(chr(65)) # C


new = ["h","a",1,["p"],True]
print(new[4]) # True
print(type(new[4])) # <class 'bool'>

name = ["ali","veli","can","hasan"]
name1 = []
name1.append(name)
print(name1[0])# ['ali', 'veli', 'can', 'hasan']
print(name1[0][1])#veli
print(name1[0][1][1])#e
print(len(name1)) # 1

aa = list(range(11)[1:11:2])
print(aa)# [1, 3, 5, 7, 9]