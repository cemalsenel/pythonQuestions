#while
sentence = input("give me a sentence :")
words = sentence.split()
i = 0
longest = 0
while i < len(words) :
    if len(words[i]) > longest :
        longest = len(words[i])
    i += 1
print("the lengt of the longest word is :", longest)

names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]
prefix = "Hello "
i = 0
a = len(names)
while i < a :
    print(prefix, names[i])
    i += 1

sayılar=[]
for i in range(1,6):
    sayılar.append(i)
print(sayılar)

course ="clarusway"
count = 0
for i in course :
    count+=1
    if count < len(course):
        i = i + "-" 
    else :
        i = i
    print(i , end = "")

word = "clarusway"
a = "-".join(word)
print(a)


user = {"name": "Daniel", "surname": "Smith", "age": 35}
for attribute in user:
    print(attribute)
    

samanlık = ["yumurta","yaba","inek","iğne","saman","tezek","tırmık"]
print(f"iğne {samanlık.index('iğne')} numaralı indexte.")

v=("five",5,True)
(x,y,z) = v
print(x,y,z)