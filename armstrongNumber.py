
number = input("Enter a number")
while number.isnumeric()==False :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
    number = input("Enter a number")
    
num_set = list(number)
print(num_set)
sum = 0
for i in number :
    i = int(i)
    a = i**len(number)
    sum += a
    
print(sum)
if sum == int(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

