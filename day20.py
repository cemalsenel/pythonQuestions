print((lambda x,y : (x+y)/2)(5,3))

num1=[9,6,7,4]
num2=[3,6,5,8]
print(list(map(lambda x,y:(x+y)/2, num1,num2)))

words1=["you","much","hard"]
words2=["i","you","he"]
words3=["love","ate","works"]
    
sentence = list(map(lambda x,y,z : (x+" "+y+" "+z),words2,words3,words1))
print(sentence)


first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x:x%2==0, first_ten)
print(list(even))

words = ['apple', 'swim', "clock", "me", "kiwi", "banana"]
for i in filter(lambda x: len(x) < 5 ,words):
      print(i)
    
first_ten=["a","b","c","d","e","f","g","h","i","j"] 
vowel_list=["a","e","i","o","u"]  
vowels =filter(lambda x : True if x in vowel_list else False,first_ten)
print("The vowels are :",list(vowels))

def modular_function(n):
    return lambda x: x ** n
power_of_2 = modular_function(2)  # first sub-function derived from def
power_of_3 = modular_function(3)  # second sub-function derived from def
power_of_4 = modular_function(4)  # third sub-function derived from def
print(power_of_2(2))  # 2 to the power of 2
print(power_of_3(2))  # 2 to the power of 3
print(power_of_4(2))  # 2 to the power of 4


def repeater(n):
    return lambda x: x * n
repeat_2_times = repeater(2)  # repeats 2 times
repeat_3_times = repeater(3)  # repeats 3 times
repeat_4_times = repeater(4)  # repeats 4 times
print(repeat_2_times('alex '))
print(repeat_3_times('lara '))
print(repeat_4_times('linda '))


def functioner(emoji = None):
    return lambda message:print(message,emoji)

print_smile = functioner(":)")
print_smile(66)
print_sad = functioner(":(")
print_sad(65)

def func_generator(func_name):
    return lambda x : func_name(x)

a_max=func_generator(max)
a_sorted=func_generator(sorted)
a_bool = func_generator(bool)
a_print=func_generator(print)

print(a_sorted([1,2,3,4,8,9,6]))



import math  as math
print(dir(math))
from math import pi,log10,factorial
print(factorial(4))
print(log10(154))
print(math.pi)

import string as strr
print(strr.punctuation)
print(strr.octdigits)
print(strr.digits)

