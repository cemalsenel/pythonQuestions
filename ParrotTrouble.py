#We have a loud talking parrot. We are in trouble if the parrot is talking and the hour is before 6 or after 21.

def parrot_trouble(talking, hour):
    if hour > 21 or hour <6 :
        if talking == True:
            return True
        else:
            return False
      
    else:
        return False
print(parrot_trouble(True,5))