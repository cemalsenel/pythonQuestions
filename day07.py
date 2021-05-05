text = "Merhaba yeni dunya sana da"
print(text.replace("e", "eee").upper())
print(text.swapcase())
print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("a","bbbbbb",1))
print(text.replace("a","bbbbbb",-1))

text1 = "Ali ata bak"
print(text1.strip("Ak"))
text2="  Ali  "
print(text2.lstrip())
print(text2.rstrip())
text3= "Merhaba"
print(text3.lstrip("Me"))
print(text3.rstrip("ba"))
print(text3.strip("Ma"))

a = "In God wee Trust"
print(a.replace("e","",1))