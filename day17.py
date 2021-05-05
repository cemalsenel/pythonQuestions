# Built-in functions
grocery = ['bread', 'water', 'olive']
enum_grocery = enumerate(grocery)
print(type(enum_grocery))
print(list(enum_grocery))
enum_grocery = enumerate(grocery, 10)
print(list(enum_grocery))

number = [-222, 0, 16, 5, 10, 6]
largest_number = max(number)
smallest_number = min(number)
print("The largest number is:", largest_number)
print("The smallest number is:", smallest_number)

ord("a")
ord("t")


numbers = [2.5, 30, 4, -15]
numbers_sum = sum(numbers)
print(numbers_sum)
numbers_sum = sum(numbers, 20)
print(numbers_sum)

# Functions
def multiply(a, b) :
    print(a * b)
multiply(3, 5)
multiply(-1, 2.5)
multiply('amazing ', 3)

def add(a,b):
    print(a+b)
add(4,5)


def calculator(x, y, opr):
    if opr == "+":
        print(x + y)
    elif opr == "-":
        print(x - y)
    elif opr == "*":
        print(x * y)
    elif opr == "/":
        print(x / y)
    else:
        print("Enter a valid operator!")

def myFunction(a, b):
    print(a + " " + b)
text_1 = "is Joseph"
text_2 = "My name"
myFunction("text_2", "text_1")



while True :
    number = input("enter a positive number.")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print(number, "is invalid entry. enter numberic value!")
    elif int(number) >= 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(number, "is an Armstrong Number.")
            break
        else :
            print(number, "is not an Armstrong Number.")
            break

        
n = int(input("Enter a number to check if it is a prime number."))
count = 0
for i in range(1, n+1) :
    if n % i == 0 :
        count += 1
if (n == 0) or (n == 1) or (count >=3) :
    print(n, "is not a prime number.")
else:
    print(n, "is a prime number")