#Write a program that 
#Takes the first name from the user and compares it to yours,
#Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
#If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

name = input("Enter you name please").title()
if name == "Cemal" :
    print("Hello,",name, "The password is : W@12")
else :
    print("Hello, ",name, "See you later.")
 