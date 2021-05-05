reef=["swordfish ","shark","whale","jellyfish","lobster","squid","octopus"]
print(reef[:-3]) #['swordfish ', 'shark', 'whale', 'jellyfish']
print(reef[::-1]) #['octopus', 'squid', 'lobster', 'jellyfish', 'whale', 'shark', 'swordfish ']
print(reef[::-2]) #['octopus', 'lobster', 'whale', 'swordfish ']

letters=["a","b","c","d","e","f","g","h","i","j"]
print(letters[7:3:-1]) #['h', 'g', 'f', 'e']
print(letters[2:6:-1]) #[]

name= ["mehmet","can","ali","zekeriya"]

print(sorted(name))# ['ali', 'can', 'mehmet', 'zekeriya']

city=["addis baba","istanbul","rio","rome","tokyo"]
print(sorted(city, key=len,reverse = True) )# ['addis baba','istanbul','rio','rome']
print(sorted(city, key=len,) )# ['rio', 'rome', 'tokyo', 'istanbul', 'addis baba']

# TUPLES

a = ["a","b","c","d"]
a_tuple = tuple(a)
print(a_tuple)#('a', 'b', 'c', 'd')

b =("Solar",)
print(b , type(b) , sep = "\n") 
#('Solar',)
#<class 'tuple'>
x=1,2,3
print(x)#(1, 2, 3)

c = "ali",
print(c , type(c)) # ('ali',) <class 'tuple'>

number = tuple(range(1,11))
print(number)

mix_tup1e = ("11", 11, [2, "two", ("six", 6)], (5, "fair"))
str_six = mix_tup1e[2][2]
print(str_six, type(str_six), sep="\n")#('six', 6)  <class 'tuple'>
print(mix_tup1e[[3][-1]])
print(mix_tup1e[[3][1]])
print(mix_tup1e[2].append("clarusway"))
print(mix_tup1e[2].remove("clarusway"))
print(mix_tup1e[2])
mix_tup1e[2][2]=15
print(mix_tup1e)


