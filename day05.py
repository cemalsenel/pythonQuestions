text = "orange"
print(text[-6:-5:])
print(text[:1:])
print(text[-5:-2:])
print(text[::-1])
print(text[::])
print(text[-2:-5:-1])
print(text[-3:-6:-1])
print(text[4:1:-1])

a = "hippopotamus life"
print(a[1:])
print(a[:6])
print(a[::2])
print(a[1:7:2])
print(a[-3:])
print(a[::-1])
print(* a)
print(3*a)
print(3*"cat")
print(* a*3)
print(* a*2, sep='/')

str1 = "can"
str1 +="dan"
str1 *=3
print(str1)

state = "California"
country = "USA"
adjective="crowded"

print("{0} is the most {2} state of the {1}".format(state,country,adjective))
print("{} is the most {} state of the {}".format(state,adjective,country))
print("{state1} is the most {adjective1} state of the {country1}".format(state1 = "California",country1 = "USA",adjective1="crowded"))

print("{}-{}".format("mehmet","ahmet"))
print("{} is the most {adjective} state of the {country}".format("California", country = "USA", adjective= "crowded"))
print("{} is the most {adjective} state of the {}".format( "USA","California", adjective= "crowded")) # Positional ("USA"i "California") olan değişkenler her zaman önce olmalı
print("{x}-{}-{}-{y}".format("b","c",y ="d",x="a")) # Positional argument follows keyword argument
print("{y}-{1}-{x}-{0}".format(1,"d",y =5,x="b"))