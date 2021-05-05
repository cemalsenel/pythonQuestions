"""
print(chr(ord('b')+1))

print(format("Welcome", "10s"), end = '#')
print(format(111, "4d"), end = '#')
print(format(924.656, "3.3f"))

example = "snow world"
print("%s" % example[4:7])

print('*', "abcdef".center(10), '*')

print("xyyzxyzxzxyy".count('yy', 1))

print("xyyzxyzxzxyy".endswith("xyy", 0, 2))

name  = str(input("İsiminiz ?"))
yas = int(input("yaşınız?"))
print("Benim adım {1} ve yaşım {0}".format(yas ,name))
print(f"Benim adım {name} ve yaşım {yas}")
print("Benim adım {ad} ve yaşım {yas}".format(ad = "abdullah", yas = 32))


print("hello world", end = "/")
print("merhaba yeni dunya", end = ".")
print()
print("merhaba","yeni","dunya",sep = "/")


# According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
year = int(input("Enter a year"))
a = ((year % 4 == 0 and year % 100 == 0) and (year % 400 == 0) and True) 

print(a)

print("a"+"bc")



print(int(0b10))
print(int(0o12))
print(int(0x19))

print(bin(2))
print(bin(0o12))
print(bin(0x19))

print(oct(12))
print(oct(0b11010))
print(oct(0x19))


print(hex(12))
print(hex(0b11010))
print(hex(0o17))

print(0xA + 0xB + 0xC)
print("abcd"[2:])

str1 = "hello"
str2 = ","
str3 = "world"
print(str1[-1:])
str1 = "world"

print(r"\nhello")
print("new" "line")

#print("new" "line" "end" 3)
print("new" "line" "end", 3)

str1 = "clarsuway"

print(str1[::-1])

=======================
Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as : numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3,6,6,6,6]
frqt=max(numbers,key=numbers.count)
cnt1 = numbers.count(frqt)
print("the most frequent number is " ,  frqt , "and it was ",cnt1, "times repeated")

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
} 
print(round((sales["sell_value"]-sales["cost_value"] )*sales["inventory"]))

a =3
b=29.99
c = 4.1
print("${:.2f}\n${:.2f}\n${:.2f}".format(3,29.99,4.1))

strs =["eat", "tea", "tan", "ate", "nat", "bat"] # output => [["ate","eat","tea"],["nat","tan"],["bat"]]


def groupAnagrams(word_list):
    allResults=[]
    results=[]

    for idx,s in enumerate(word_list):
        if s == None:
            pass
        else:
            results = [s] # word s is added to anagram list

            # you were generating only 1 anagram like for tan --> ant but in word_list only nat was present
            for i in range(1,len(s),1):
                temp = s[i:]+s[:i] #anagram 
                    # for s = 'tan' it generates only 'ant and 'nta'
                    # when it should generate all six tna ant nta _nat_ atn tan

                if temp in word_list:
                  results.append(temp)
                  word_list[word_list.index(temp)] = None

            allResults.append(results) 

    return allResults

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [['eat', 'ate', 'tea'], ['tan'], ['nat'], ['bat']]
 
a=[1,2,3,4]
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print(b) # [1, 3, 6, 10]

L1 = []
L1.append([1, [2, 3], 4]) # append elemanları tek bir eleman olarak ekliyor
L1.extend([7, 8, 9]) # extend elemanların hepsini tek tek ekliyor. listenin uzunluğu append den farklı olur
print(L1[0][1][1] + L1[2]) # 11

T = (1, 2, 3, 4, 5, 6, 7, 8)
print(T[T.index(5)], end = " ")
print(T[T[T[6]-3]-6]) # 5 8

D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
D['1'] = 2
print(D[D[D[str(D[1])]]]) # 3

set1 = {1, 2, 3}
set2 = set1.copy()
set2.add(4)
print(set1) # {1, 2, 3}
     
#Write a program that 
#Takes the first name from the user and compares it to yours,
#Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
#If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

name = input("Enter you name please").title()
if name == "Cemal" :
    print("Hello,",name, "The password is : W@12")
else :
    print("Hello, ",name, "See you later.")
 
liste=["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_list=[]
sonuc=[]
for i in liste:
  if sorted(i) not in sorted_list:
    sorted_list.append(sorted(i))
    print(sorted_list)
for a in range(len(sorted_list)):
  sonuc.append([i for i in liste if sorted(i)==sorted_list[a]])
  print(sonuc)
print(sonuc) 

#n = 5, 1 2 3 4 5     The largest number is:  5
#n = 3, 67 85 19      The largest number is:  85
#Write a python code that finds the largest number among the ``n`` numbers given by the user as input.
x = list(map(int, input("Enter  multiple values: ").split()))
print("Numbers you entered: ", x)
x.sort()
print("The largest number is : ",x[len(x)-1])

     
for x in set('pqr'):
    print(x*2)    
 
d = {"john":40, "peter":45}
print(d["john"])
 
d = {"john":40, "peter":45}
print(list(d.keys()))
 
a={}
a['a']=1
a['b']=[2,3,4]
print(a) 
 
z=set('abc')
z.add('san')
z.update(set(['p', 'q']))
print(z)
 
num_people = 5
if num_people > 10:
      print("There is a lot of people in the pool.")
elif num_people > 4:
      print("There are some people in the pool.")
elif num_people > 0:
      print("There are a few people in the pool.")
else:
      print("There is no one in the pool.")
 


college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
print(list(enumerate(college_years, 2019)))

fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}
fruit_names = [x for x in fruits.keys()]
print(fruit_names)
 
i = 5
while True:
 if i%0O11 == 0:
     break
 print(i)
 i += 1
 
x = 'abcd'
for i in range(len(x)):
    x[i].upper()
print(x)
 
k = [2,3,4]
print(* reversed(k))

def sum_double(x, y):
    if x != y:
     return x+y
    else:
     return 2*x

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

"""
        
