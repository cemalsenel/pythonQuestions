#We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.

def parrot_trouble(talking, hour):
    if (21 >= hour >= 6 ) and talking == True :
        return True
    else:
        return False
print(parrot_trouble(False,6))