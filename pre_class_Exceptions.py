"""
Exception :These types of errors are detected during the program execution (interpretation) process.
Syntax Error:These types of errors are detected during compiling the program into byte-code.
-------------------------------------------------
print('Here we go!')
print('I will be the second text')
a = '3'
b = 5
print('It is time for an error message :(')
print(a + b)  # it won't be printed
print("Sorry, but I won't be printed")  # it won't be printed

Here we go!
I will be the second text
It is time for an error message :(
Traceback (most recent call last):
  File "code.py", line 6, in <module>
    print(a + b)
TypeError: can only concatenate str (not "int") to str
----------------------------------------------
Q: What are the Errors and Exeptions in Python? 
A:In Python, there are two types of errors: syntax error and exceptions.
Syntax Error: It is also known as parsing errors. 
Errors are issues in a program which may cause it to exit abnormally. 
When an error is detected, the parser repeats the offending line and then displays an arrow which points at the earliest point in the line.
Exceptions: Exceptions take place in a program when the normal flow of the program is interrupted due to the occurrence of an external event. 
Even if the syntax of the program is correct, there are chances of detecting an error during execution, 
this error is nothing but an exception. 
Some of the examples of exceptions are - ZeroDivisionError, TypeError and NameError.
- Interview Q&A
--------------------------------------------------
Common Exceptions
1)ValueError :Raised when an operation or function receives an argument that has the right type but an inappropriate value, 
and the situation is not described by a more precise exception such as IndexError. 
In other words; to encounter a ValueError in Python means that it is a problem with the content of the object you tried to assign the value to. 
This should not be confused with types in Python. => print(int('ten'))
-------------------------------------
2)NameError :This error is usually raised if a variable you use in the code stream is not pre-defined 
or not properly defined. In other words, it is raised when a local or global name is not found. 
This applies only to unqualified names. 
The associated value is an error message that includes the name that could not be found. 
For better understanding, let's take a look at this example . 
=> print(variable) 
   variable = "Don't ever give up!"
Attention :
Note that the NameError often raises due to the lack of attention to these two things: 
case-sensitivity of Python and pre-defines of the variables.
---------------------------------------------
3)TypeError :Raised when an operation or function is applied to an object of inappropriate type. 
The associated value is a string giving details about the type mismatch. Let's examine this example :
for i in range('x'):
    print(i)
------------------------------------------------------------------
Q: Give some examples of standard errors that occour in Python.
A:
TypeError- It occurs when the expected type does not match with the given type of a variable.
ValueError- It occurs when an expected value is not given, suppose you are expecting 6 elements in a list and you gave 2.
NameError- It occurs when you are trying to access an undefined variable or a function.
IOError- It occurs when you are trying to access a file that does not exist.
IndexError- It occurs when you are trying to access an invalid index of a sequence.
KeyError- It occurs when you use an invalid key to access a value in the dictionary.

- Interview Q&A
"""
# EXCEPTIONS
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except:
        print("Something went wrong...Try again.")

#Of course, when do this, we anticipate which exception error we will encounter.       
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")
#Let's reorganize our previous code according to the structure described in the previous lesson. Consider this block of code :
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two  # normal part of the program
    except ZeroDivisionError:
        print("You can't divide by zero! Try again.")  # executes when division by zero
    else:
        print("The result of the division is : ", division)  # executes if there is no exception
    finally:
        print("Thanks for using our mini divison calculator! Come again!")
        break  # exits the while loop
#No matter what exception we encounter, there is a way to see it. Using the keyword Exception.
while True:
    no_one = int(input("The first number please : "))
    no_two = int(input("The second number please : "))
    try:
        division = no_one / no_two
        print("The result of the division is : ", division)
        break
    except Exception as e:
        print("Something went wrong...Try again.")
        print("Probably it is because of '{}' error".format(e))
        break
"""
try :
    a = 10
    b = 2
    print("The result of division is :", c)
except Exception as e:
    print("The error message is : ", e)

    =>The error message is :  name 'c' is not defined
Apart from GeneratorExit, KeyboardInterrupt, SystemExit, the Exception keyword you learned in the previous lesson covers all exceptions.
"""
try:
  print("Hello")
except:
  print("Something is wrong")
else:
  print("Nothing is wrong")

try:
    x = 4 / 1
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')


"""
The try…except block has another optional finally clause. 
The finally clause is always executed, whether an exception has occurred or not. 
Consider the following example of the finally clause :
"""
try:
	x = 3 / 0
except:
	print('Something went wrong')
finally:
	print('Always execute this')


"""
Use finally clause to define clean-up actions that must be executed under all circumstances e.g. closing a file. :

try:
    f = open('myfile.txt')
    print(f.read())
except:
    print("Something went wrong")
finally:
    f. close()
"""
"""
try:
  print(x)
except:
  print("An exception occurred")
"""
try:
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')

"""
Take a look at the first one. 
In this example you can define as many except blocks as you want, to catch and handle specific exceptions :
try:
    x = 2/0
except ZeroDivisionError:
    print('Attempt to divide by zero')
except:
    print('Something else went wrong')
-------------------------------------------------
....
except:
    print("Unknown exception error occured. Tyr again please.")
--------------------------------------------------
....
except ZeroDivisionError:
   print("You can't divide by zero!!")
except ValueError:
   print("You can only enter numbers consisting of digits, not text!!")
-------------------------------------------
....
except (ValueError, TypeError):
    print("You can only enter numbers consisting of digits, not text!!")
-------------------------------------------------------------------
....
except ArithmeticError:
    print("I will also catch OverflowError, FloatingPointError and ZeroDivisionError")

"""




