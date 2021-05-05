"""
#n = 5, 1 2 3 4 5     The largest number is:  5
#n = 3, 67 85 19      The largest number is:  85
#Write a python code that finds the largest number among the ``n`` numbers given by the user as input.

n = int(input("How many numbers you want to enter"))
a = 0;
c=list()
while a < n:
   c.append(int(input("Enter  multiple values: ")))
   a +=1 
c.sort() 
print("The largest number is : ",c[len(c)-1])

#Given a list of strings, group anagrams together.
#["eat", "tea", "tan", "ate", "nat", "bat"],
#Output:[["ate","eat","tea"],["nat","tan"],["bat"]]

list1=list(input("Enter  multiple values: ").split())
print(list1)
list2=[]
list3=[]
for i in list1:
  if sorted(i) not in list2:
    list2.insert(0,sorted(i))
for a in range(len(list2)):
  list3.insert(0,[i for i in list1 if sorted(i)==list2[a]])
print(list3) 


"""





