country = ["USA", "Brasil", "UK", "Germany", "Turkey", "New Zeland"]
print(country)

string_1 ="I quit smoking"
new_list_1 = list(string_1)  # we created multi element list
print(new_list_1)

new_list_2 = [string_1]  # this is a single element list
print(new_list_2)

mixed_list= [11, "Joseph", False, 3.14, None, [1, 2, 3]]
print(mixed_list)

warning = 'You must quit smoking!'

print(len(list(warning)))

empty_list = []
empty_list2= list()
empty_list.append(24)
empty_list.append("merhaba")
empty_list.append(3.14)
print(empty_list)
print(empty_list2)

city = ['New York', "London",'Istanbul', "Seoul", "Sydney"]
city.append('Ankara')
city.insert(0,"Trabzon")
city.insert(1,"Samsun")
city.remove("London")  # we have deleted "London"
city.sort()  # lists the items in alphabetical order
city[0] = "München"
print(city)
print(city.pop(0))
del(city[4])
print(city.index("Trabzon"))
print(len(city))
print(city)

my_list = [1, 3, 5, 7]
print(my_list*3)  # [1, 3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7]

city_list=[]
city_list.append(city)
print(city_list)  # [['Istanbul', 'New York', 'Samsun', 'Seoul', 'Trabzon']]
print(city_list[0])  # ['Istanbul', 'New York', 'Samsun', 'Seoul', 'Trabzon']
print(city_list[0][2])  # Samsun
print(city_list[0][2][0])  # S

number = [1,2,3,4,6,9,8,7,4,5,3]
print(number[2:5])  # [3, 4, 6] ==>  we get the elements from index = 2 to index = 5 (5 is not included)

count= list(range(11))
print(count)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count[0:11:2])  # [0, 2, 4, 6, 8, 10]

animals = ["elephant", "bear", "fox", "wolf", "rabbit", "deer", "giraffe"]
print(animals[:])  # ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
print(animals[3:])  # ['wolf', 'rabbit', 'deer', 'giraffe']
print(animals[:5])  # ['elephant', 'bear', 'fox', 'wolf', 'rabbit']
print(animals[::2])  # ['elephant', 'fox', 'rabbit', 'giraffe']
print(animals[-4])  # wolf
print(animals[-3:])  # ['rabbit', 'deer', 'giraffe']
print(animals[:-3])  # ['elephant', 'bear', 'fox', 'wolf']
print(animals[::-1])  # ['giraffe', 'deer', 'rabbit', 'wolf', 'fox', 'bear', 'elephant'] ==> we have produced the reverse of the list
print(animals[::-2])  # ['giraffe', 'rabbit', 'fox', 'elephant']
print(animals[2:6:-2])  # []
print(animals[6:2:-1])  # ['giraffe', 'deer', 'rabbit', 'wolf']
# If you choose negative step with the start and end indexes together, those should be used accordingly, that is, the end index should be less than the start index.
print(len([[12, 34, 56]][0]))

# TUPLES ARE LISTS WHICH ARE IMMUTABLE. WE CANNOT USE "INSERT,APPEND" METHODS. TUPLES ARE FASTER THAN LISTS . LISTS CAN BE CHANGED BUT TUPLES CAN NOT.
mix_value = (10, False, 'fruit', 1.618)
# mix_value.append(['vegetable', 2+3j])
print(len(mix_value))

a = list(range(1,11))
a.sort()
a.reverse()
print(a)

grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
print(grocer[1][1][1::2])

flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
colors = ["red", ("blue", ["yellow", "green"]), "pink"]
a = flowers[0][2]
b = flowers[0][1][1]
c = colors[1][0]
d = colors[1][1][1]
text = "My two favorite flowers are {0} and {1}, two favorite colors are {2} and {3}.".format(a,b,c,d)
print(text)

escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]
a=escapes[0]
b=escapes[2][1]
sentence = "I am 40 years old.{0}I have two children.{1}Data Science is my IT domain.".format(a,b)

print(sentence)

# SET
a ={'carnation', 'orchid', 'rose', 'violet'} 
b={'rose', 'orchid', 'rose', 'violet', 'carnation'}
print(a) # {'violet', 'carnation', 'orchid', 'rose'}
print(b) # {'violet', 'carnation', 'rose', 'orchid'}

#x= set([[1,2],[3,4],[4,5]]) ==> The iterable argument given for the set must be used in a correct way.
y=set([1,2,2,3,4,5])
z= {1,2,3,4}
q= set((1,2,3,4))
#print(type(x))
print(type(y))
print(type(z))
print(type(q))

word1= set("hayat devam ediyor")
word2= set("hayat nasil gidiyor")
print(word1.difference(word2)) # {'v', 'm', 'e'}
print(word1-word2) # {'v', 'm', 'e'}

print(word1.intersection(word2)) # {'o', 't', 'd', 'i', 'y', 'r', ' ', 'h', 'a'}
print(word1 & word2) # {'o', 't', 'd', 'i', 'y', 'r', ' ', 'h', 'a'}

print(word1.union(word2)) # {'o', 't', 'm', 's', 'i', 'y', 'r', 'n', 'e', 'l', 'd', ' ', 'h', 'g', 'v', 'a'}
print(word1 | word2) # {'o', 't', 'm', 's', 'i', 'y', 'r', 'n', 'e', 'l', 'd', ' ', 'h', 'g', 'v', 'a'}

word1.remove("a") # => removed 'a' from list
word1.add("c") # => added 'c' in the list
print(word1) # {'r', 'm', 'i', 'c', 'v', 'o', ' ', 'h', 'e', 'd', 't', 'y'}
print(len(set(word1))) 
print( "c" in word1) # True
print("a" not in word1) # True
print("c" not in word1) # False

print(len(set('listen to the voice of enlisted')))


people = []
people.append({
    "first":"Hans", "second":"muller"
})
print(people,type(people)) # [{'first': 'Hans', 'second': 'muller'}] <class 'list'>

numbers = {}
numbers['x'] = 12
numbers['y'] = 4
numbers.update({'z': 3})

print(numbers['x'] + numbers['y'] + numbers['z']**2)

letters = ['a', 'b', 'c', 'd', 'f']
letters.insert(4, 'e')
print(letters)

numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]
numbers_10.insert(1,20)
print(numbers_10)

fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]
print(fruits_vegetables[3][0])

family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
family1 = tuple(family_members)
print(type(family1))