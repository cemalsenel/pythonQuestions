def multiply(a, b) :
    print(a * b)

multiply(3, 5)
multiply(-1, 2.5)
multiply('amazing ', 3)  # it's really amazing, right?

def motto() :
    print("Don't hesitate to reinvent yourself!")

motto()  # it takes no argument

def multiply_1(a, b) :
    print(a * b)  # it prints something

def multiply_2(a, b) :
    return a * b  # returns any numeric data type value

multiply_1(10, 5)
print(multiply_2(10, 5))

shadow_var = print("It can't be assigned to any variable")
print(shadow_var)  # NoneType value can't be used

"""
Note that, if there are more than one keyword return in a function, 
then the execution of that function will end after the first return
"""

def my_function2(a, b):
    area = a * b
    return area

print(my_function2(3,5))

def my_function1(a, b):
    hypotenuse = (a**2 + b**2)**0.5
    return hypotenuse
  
print(my_function1(5,5))

def longer(a, b):
    if len(a) >= len(b):
        return a
    else:
        return b 

print(longer('Richard', 'John'))


def who1(first, last) :  # 'first' and 'last' are the parameters(or variables)
    print('Your first name is :', first)
    print('Your last name is :', last)

who1('Guido', 'van Rossum')  # 'Guido' and 'van Rossum' are the arguments
print()
who1('Marry', 'Bold')  # 'Marry' and 'Bold' are also the arguments

def pos_args(a, b):
    print(a, 'is the first argument')
    print(b, 'is the second argument')

pos_args(3,4)
print()
pos_args(4,3)

pos_args('first','second')
print()
pos_args('second', 'first')


def who(first, last) :  # same structure as the previous one
    print('Your first name is :', first)
    print('Your last name is :', last)

who(first='Guido', last='van Rossum')  # calling the function is different
# we used kwargs to pass the values into the function => The formula syntax is : kwargs=values.

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
"""
def function(a):
    pass  # actually, 'pass' does nothing. it just moves to the next line of code

function(0, a=0)

=> Traceback (most recent call last):
  File "code.py", line 4, in 
    function(0, a=0)
TypeError: function() got multiple values for argument 'a'
"""

def city(capital, continent='Europe'):
    print(capital, 'in', continent)

city('Athens')  # we don't have to pass any arguments into 'continent'
city('Ulaanbaatar', continent='Asia')  # we can change the default value by kwargs
city('Cape Town', 'Africa')  # we can change the default value by positional args.



#the least frequently used option is to specify that a function can be called with an arbitrary number of arguments.=>The formula syntax is : *args
#If you need to prefer to use arbitrary keyword arguments (**kwargs), you can use it in the same way.=>The formula syntax is : **kwargs.

def fruiterer1(fruit1, fruit2) :
    print('I want to get', fruit1, 'and', fruit2)
        
fruiterer1('orange', 'banana')

def fruiterer(*fruit) :
    print('I want to get :')  
    for i in fruit :
        print('-', i)

fruiterer('orange', 'banana', 'melon', 'ananas')

def animals(**kwargs):
    for key, value in kwargs.items():
        print(value, "are", key)
 
animals(Carnivores="Lions", Omnivores="Bears", Herbivores="Deers", Nomnivores="Human")

"""
Traditionally, people in the world of computer programming use *args for the arbitrary number of positional arguments 
and **kwargs for the arbitrary number of keyword arguments.
"""

def brothers(bro1, bro2, bro3):
    print('Here are the names of brothers :')
    print(bro1, bro2, bro3, sep='\n')

family = ['tom', 'sue', 'tim']
brothers(*family)

def gene(x, y):  # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  # we call the function by a single argument(variable)

def gene1(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_gene1 = {'y' : "Marry", 'x' : "Fred"}
gene1(**dict_gene1) 

# def a_function(pos1, pos2, /, pos_or_kwarg, *, kwarg1, kwarg2, **kwargs) :
"""
Use positional-only if you want the name of the parameters to not be available to the user. 
This is useful when parameter names have no real meaning, 
if you want to enforce the order of the arguments when the function is called or 
if you need to take some positional parameters and arbitrary keywords.
Use keyword-only when names have meaning and 
the function definition is more understandable by being explicit with names or 
you want to prevent users relying on the position of the argument being passed.
Use arbitrary numbers of arguments (*args) when you can't determine how many arguments your function needs. 
*args enables you to have interoperability with a list of positional arguments in your function.
You can use **kwargs, when you don't know the exact number of keyword arguments in your function. 
**kwargs enables you to have interoperability with a dictionary of key-value pairs.
The order of the parameters you use when defining the function is as important as the order of the arguments you pass into when you call the function.
"""

def team_names(*teams) :
    print('The teams in Premier League are :')
    for i in teams :
        print('-', i)

team_names('Liverpool', 'M.United', 'M.City', 'Arsenal')

def make_sentence(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for i in kwargs.values():
        result += i
    return result

print(make_sentence(a="I ", b="love ", c="Clarusway!"))

def team_league(team, league='Premier League'):
    print(team, 'in', league)

team_league('Liverpool')

def my_function111(first, last) : 
    print('Your first name is :', first)
    print('Your last name is :', last)

my_function111(first='Richard', last='Rice') 


my_var = 'outer variable'

def func_var(): 
	my_var= 'inner variable'
	print(my_var) 

func_var() 
print(my_var)

text = "I am the global one"
 
def global_func():
    print(text)  # we can use 'text' in a function
                 # because it's a global variable

global_func()  # 'I am the global one' will be printed
print(text)  # it can also be printed outside of the function
 
text = "The globals are valid everywhere "
 
global_func()  # we changed the value of 'text'
# 'The globals are valid everywhere' will be printed
 
def local_func():
    local_text = "I am the local one"
    print(local_text)  # local_text is a local variable

local_func()  # 'I am the local one' will be printed as expected
 
#print(local_text)  # NameError will be raised
# because we can't use local variable outside of its function

x = 10
def my_function_11(): 
    x = 20 
    print(x)
    
print(x)


variable = "global"

def func_outer():
    variable = "enclosing outer local"
    def func_inner():
        variable = "enclosing inner local"
        def func_local():
            variable = "local"
            print(variable)
        func_local()
    func_inner()
 
func_outer()  # prints 'local' defined in the innermost function
print(variable)  # 'global' level variable holds its value

"""
count = 1

def print_global():
    print(count)
 
print_global()
 
def counter():
    print(count)
    count += 1  # we're trying to change its value
 
print()  # just empty line
counter() 


1

Traceback (most recent call last):
  File "code.py", line 11, in <module>
    counter() 
  File "code.py", line 8, in counter
    print(count)
UnboundLocalError: local variable 'count' referenced before assignment



"""
count = 1

def counter():
    global count  # we've changed its scope
    print(count)  # it's global anymore
    count += 1
 
counter() 
counter()
counter()
counter()

def func_enclosing1():
    x = 'outer variable'
    def func_enclosing2():
        x = 'inner variable'
        print("inner:", x)
    func_enclosing2()
    print("outer:", x)

func_enclosing1() 
#inner: inner variable
#outer: outer variable


def enclosing_func1():
    x = 'outer variable'
    def enclosing_func2():
        nonlocal x  # its inner-value can be used in the outer scope
        x = 'inner variable'
        print("inner:", x)
    enclosing_func2()
    print("outer:", x)

enclosing_func1() 
#inner: inner variable
#outer: inner variable

xq = 10
  
def my_function3(): 
    global xq
    xq += 5
    print(xq)
    
my_function3()  
     
x = 'My name is Richard'
def my_function_1(): 
    x = 'My name is John'
    
print(x)


city1 = "I love Paris!"

def my_function(): 
    city1="I love London!"
    print(city1) 
    
my_function()


def outer():
    x = "previous"
    
    def inner():
        nonlocal x
        x = "later"
        print("inner:", x)
    
    inner()
    print("outer:", x)
    
outer()