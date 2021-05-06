# [("mary", "rye"), ("bella", "fred"), ("linda", "roland")]
dict_couple = {"bride": ["mary", "bella", "linda"],
               "groom": ["rye", "fred", "roland"]}
def couples(bride, groom):
    couple_list = []
    for i in zip(bride, groom):
        couple_list.append(i)
    return couple_list
couples(**dict_couple)

def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
# iki önemli nokta. Item sayısı ve key isimleri
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene)  # Dictionary key ve valueları gelir
gene()  # default argümanları getirir
"""
Problem Statement
Write a function that given a string containing just the characters (, ), {, }, [ and ], determines if the input string is valid or not by using following rules.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example for user inputs and respective outputs

Input        Output
--------:    ------:
"()"         True
"()[]{}"     True
"(]"         False
"([)]"       False
"{[]}"       True
""           True
    
"""

def isValid(s):
    while "()" in s or "[]" in s or "{}" in s :
        s = s.replace("()","").replace("[]","").replace("{}","")
    return s==""

x="[]{}[]()"
print(isValid(x))

iterable="Hello World"
reverser = (lambda x : x[::-1])(iterable)
print(reverser)


for i in [1,2,3,4]:
    print(i,":",(lambda x : "odd" if x%2 !=0 else "even")(i))

hipotenüs = lambda x,y: (x**2 + y**2)**0.5
print(hipotenüs(3,4))

letter1 = ['sanma şahım ', 'herkesi sen ', 'sadıkane ', 'yar olur']
letter2 = ['herkesi sen ', 'dost mu sandın ', 'belki ol ', 'ağyar olur']
letter3 = ['sadıkane ', 'belki ol', 'alemde bir ', 'dildar olur']
letter4 = ['yar olur ', 'ağyar olur ', 'dildar olur ', 'serdar olur']
zevol = map(lambda x,y,z,q: x+y+z+q, letter1,letter2,letter3,letter4)
print(*zevol)


         








