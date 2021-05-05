my_list = ['Joseph', 'Clarusway', 2020]
new_list1 = list(my_list)  
new_list2 = [my_list]  
print(new_list1)
print(len(new_list1)) 
print(new_list2)
print(len(new_list2))

a = ["ali","selma"]
b = [a]
print(b)
print(len(b))  # 1

print(len([1]))  # 1

x= [[1],[2,3,4,5,6,"clarusway"]]  # 2
print(len(x))

a = "2020's hard"
print(len(a))  # 11
print(len([a]))  # 1

# [] ve list() ==> liste oluşturmak için kullanılır

number = [4,5,6]
number.append(9)
# number.append('9')
print(number)

cc = []
cc.append("11")
cc.append(False)
cc.append(15)
cc.append([0])

print(cc)  # ['11', False, 15, [0]]

empty = []
empty.append(1)
empty.append(2)
empty.append(3)
empty.append(4)
print(empty)

city = ["Los Angeles", "Beirut", "Tokyo"]
city[1] = "Istanbul"
print(city)  # ['Los Angeles', 'Istanbul', 'Tokyo']
city[1:] ="Seoul"
print(city)  # ['Los Angeles', 'S', 'e', 'o', 'u', 'l']

city1 = ["Los Angeles", "Beirut", "Tokyo"]
# city1[0] = True
city1[1:] = "clarusway"
print(city1)  # [True, 'c', 'l', 'a', 'r', 'u', 's', 'w', 'a', 'y']
city1[1:]= "istanbul", "seul"
print(city1)  # [True, 'istanbul', 'seul']
city1[1:]= "22"
print(city1)  # [True, '2', '2']

city2 = ["istanbul","yozgat","erzurum","ankara"]
city2[0:2] = ["a","b"]
print(city2)  # ['a', 'b', 'erzurum', 'ankara']
city2[0:2] = ["a","b","c","d"]
print(city2)  # ['a', 'b', 'c', 'd', 'erzurum', 'ankara']
city2[0:2] =["a"]
print(city2)  # ['a', 'c', 'd', 'erzurum', 'ankara']

# \\ çıktı almak için ne yapmalı
print("\\\\")
print("\\"+"\\")
a= 3
b=4
print("{} + {} 'ün toplamı {}'dir .".format(a,b, a+b)) # 3 + 4 'ün toplamı 7'dir .

text = "{:.2f},{:.3f},{:.4f}".format(3.1463, 5.367, 7.324567) # 3.15,5.367,7.3246
print(text)

text1 = "{:.2s} - {:.3s} - {:.4s}".format("3.1463", "5.367", "7.324567")
print(text1) # 3. - 5.3 - 7.32

text3 = "{:>20}".format("clarusway")
print(text3) #           clarusway => 20 karakterin en sağına yasladı
text4 = "{:<20}".format("clarusway")
print(text4) #clarusway            => 20 karakterin en soluna yasladı
text5 = "formatlama {:>10} formatlama".format("test")
print(text5) # formatlama       test formatlama => formatlamalar arasında 10 karakterin soluna yasladı
text6 = "{:<10} formatlama".format("test")
print(text6)#test       formatlama 
text7 = "{:^20}".format("test")
print(text7)#        test        => 20 karakterin tam ortasına koydu
text8 = "formatlama {:^20} formatlama".format("test")
print(text8)#formatlama         test         formatlama
text9= "{:.5}".format("hippopotamus")
print(text9)#hippo  => en baştan 5 karakter aldı
text10 = "{:10.3}".format("hippopotamus")
print(text10)#hip           => 10 karakterlik alanda kelimenin 3 karakterini aldı
text11 = "{:>10.3}".format("hippopotamus")
print(text11)#       hip  => 10 karakterlik alanda ilk 3 karakteri sağa yasla
text12 = "{:.5}".format(3.141592653589793)
print(text12)#3.1416  => f yok ise bir eksiği kadarı alıyor(virgülden sonra 4 hane aldı)
text13 = "{:.5}".format("3.141592653589793")
print(text13)#3.141 => String'in beş karakterini aldı

