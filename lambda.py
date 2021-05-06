lambda x, y: (x+y)/2  # takes two numbers, returns the result
"""
A lambda function can take multiple arguments separated by commas, 
but it must be defined with a single expression. This expression is evaluated and the result is returned
⚠️Avoid:
Note that you do not need to use return statement in lambda functions.

Lambda's most important advantages and uses are:
1.You can use it with its own syntax using parentheses, => The formula syntax is : (lambda parameters : expression)(arguments)
2.You can also assign it to a variable, =>Alternatively, you can assign the lambda function definition to a variable then you can call it :average1 = (lambda x, y: (x+y)/2) /print(average1(3, 5)) 
3.You can use it in several built-in functions,=> The basic formula syntax is : map(function, iterable)
4.It can be useful inside user-defined functions (def).
"""
lambda x: 'odd' if x % 2 != 0 else 'even'#lambda parameters : (first_result) if conditional statement else (second_result)


print((lambda x: x**2)(2))  # squares '2'
print((lambda x, y: (x+y)/2)(3, 5))  # takes two int, returns mean of them

average = (lambda x, y: (x+y)/2)(3, 5) 
print(average)

average1 = lambda x, y: (x+y)/2
print(average1(3, 5))  # we call

iterable = [1, 2, 3, 4, 5]
map(lambda x:x**2, iterable)
result = map(lambda x:x**2, iterable)
print(type(result))  # it's a map type

print(list(result))  # we've converted it to list type to print

print(list(map(lambda x:x**2, iterable)))  # you can print directly

def square(n):   # at least two additional lines of code
    return n**2  
  
iterable = [1, 2, 3, 4, 5]
result = map(square, iterable) 
print(list(result))


letter1 = ['o', 's', 't', 't']
letter2 = ['n', 'i', 'e', 'w']
letter3 = ['e', 'x', 'n', 'o']
numbers = map(lambda x, y, z: x+y+z, letter1, letter2, letter3)

print(list(numbers))

number_list = [1, 2, 3, 4, 5]

result = list(map(lambda x: x*3, number_list))
print(result)

"""
Lambda within filter() function :
filter() filters the given sequence (iterable objects) with the help of a function (lambda) 
that tests each element in the sequence to be true or not.

The basic formula syntax is : filter(function, sequence)
"""
first_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
  
even = filter(lambda x:x%2==0, first_ten) 
print(type(even))  # it's 'filter' type, 
                   # in order to print the result,
                   # we'd better convert it into the list type

print('Even numbers are :', list(even))

vowel_list = ['a', 'e', 'i', 'o', 'u']
first_ten = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  
vowels = filter(lambda x: True if x in vowel_list else False, first_ten) 

print('Vowels are :', list(vowels))


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

def modular_function1(n):
    return lambda x: x ** n

power_of_03 = modular_function1(3)
print(power_of_03(5))

print((lambda x: x**3)(5))


mean = lambda x, y: (x+y)/2
print(mean(8, 10))

multiply = lambda x: x * 4
add = lambda x, y: x + y
print(add(multiply(10), 5))


number_list0 = [1, 2, 3, 4]
result = map(lambda x:x**3, number_list0)
print(list(result)) 


number_list00 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
divisible_list = filter(lambda x:x%3==0, number_list00) 
print(list(divisible_list))

square0 = lambda x : x**2
print(square0(5))

number_list001=[1, 2, 3, 4, 5]

result01= list(map(lambda x : x**2, number_list001))
print(result01)

number_list11=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result11= list(filter(lambda x : True if x%2 ==1 else False, number_list11)) 
print(result11)
