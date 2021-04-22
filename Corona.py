age = input("Are you a cigarette addict older than 75 years old? (Yes or No):  ").title()

while age != "No" and age !="Yes":

    print("Wrong value. Please re-enter!")

    age = input("Are you a cigarette addict older than 75 years old? (Yes or No):  ").title()

    if age == "No" or age == "Yes":

        break

    

chronic = input("Do you have a severe chronic disease? (Yes or No): ").title()

while chronic != "No" and chronic !="Yes":

    print("Wrong value. Please re-enter!")

    chronic = input("Do you have a severe chronic disease? (Yes or No): ").title()

    if chronic == "No" or chronic == "Yes":

        break



immune = input("Is your immune system too weak? (Yes or No): ").title()

while immune != "No" and immune !="Yes":

    print("Wrong value. Please re-enter!")

    immune = input("Is your immune system too weak? (Yes or No): ").title()

    if immune == "No" or immune == "Yes":

        break



list1 = [age, chronic, immune]

i = 0

for i in range(len(list1)):
    if list1[i] == "Yes":
        list1[i] = True

        i += 1

    elif list1[i] == "No":

        list1[i] = False

        i += 1

    else:

        print(f"Wrong answer for {i+1}.question")

        i += 1

 

risk = list1[0] or list1[1] or list1[2]

print(f"Your risk status : {risk}")