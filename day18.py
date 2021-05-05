def filterVowels(letter):
    vowels=["a","e","i","o","u"]
    if letter.lower() in vowels:
        return True
    else:
        return False
sentence="The clarusway is the best"

filtered_Vowels = filter(filterVowels,sentence)
print(* filtered_Vowels)



def absolute_value(number):
    """
This function returns the absolute value of the entered number
    """
    if number <0:
        return -number
    else:
        return number

print(absolute_value(0))
print(absolute_value.__doc__)

"""
def fn (a, b, c = 1):          # a/b required, c optional.
    return a * b + c

print fn (1, 2)                # returns 3, positional and default.
print fn (1, 2, 3)             # returns 5, positional.
print fn (c = 5, b = 2, a = 2) # returns 9, named.
print fn (b = 2, a = 2)        # returns 5, named and default.
print fn (5, c = 2, b = 1)     # returns 7, positional and named.
print fn (8, b = 0)            # returns 1, positional, named and default.
"""

def pos_args(a, b):
    print(a, 'is the first argument')
    print(b, 'is the second argument')
pos_args(3,4)
print()
pos_args(4,3)


def texter(x,y,z):
    return f"{z} {x} {y}"

c="i"
a="love"
b="you"
print(texter(x="love",y="you",z="i"))

def default(q="ali",w = 33):
    print(q,"is",w,"years old")

default()
default("selvi")
default(w=55)
default(q="mehmet",w=25)

def default1(e,q="ali",w = 33):
    print(q,"and",e,"is",w,"years old")

default1("gonca")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

"""
parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
"""

def argu(a, c, b = "Dünya", d = "Saturn"):
    print(a, b, c, d, sep="\n")
    pass
argu("Uranüs", "Jupiter")


def city(capital, continent='Europe'):
    print(capital, 'in', continent)
city('Athens') # we don't have to pass any arguments into 'continent'
city('Ulaanbaatar', continent='Asia') # we can change the default value by kwargs
city('Cape Town', 'Africa') # we can change the default value by positional args.

def fruiterer(fruit1, fruit2) :
    print("I want to get", fruit1, 'and', fruit2)
fruiterer('orange', 'banana')

def fruiterer1(*fruit) :
    print("I want to get :")
    for i in fruit :
        print('-', i)
fruiterer1('orange', 'banana', 'melon', 'ananas')


def slicer(* numbers):
    even=[]
    odd=[]
    for i in numbers:
        if i%2==0:
            even.append(i)
           
        else:
            odd.append(i)
    print(odd)
    print(even)

slicer(1,2,3,4,5,6,7,8,9)


def slicer1( * num):
    print("evens :",[i for i in num if i%2 == 0])
    print("odds :",[i for i in num if i%2 == 1])

slicer1(1,2,3,4,5,6,7,8,9)


def animals(**kwargs):
    for key, value in kwargs.items():
        print(value, "are", key)
animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")


def sözlük (** a):
    for key,value in a.items():
        print(key,value)

sözlük(ahmet="C++",mehmet="Python",can="Java",ali="C")

def organizer(** names):
    name=[]
    age=[]
    for key,value in names.items():
        name.append(key)
        age.append(value)
    print(name) 
    print(age)  
organizer(Beth=26,Oscar=42,Justin=18,Frank=33)

def organizer1(** isim):
    print("names :",[key for key in  isim.keys() ])
    print("ages :",[values for values in  isim.values()])
organizer1(Beth=26,Oscar=42,Justin=18,Frank=33)

def defa(**x) :
    for t, z in x.items():
        print(t, "is", z, "years old.")
defa(ali = 33, veli = 44, deli = 100, ayşe = 22, nazan = 77)