first_dic ={1:"one", "two" : 2, False : [1,2,3], 2.5 : ("one","two"), (1,2) : "clrswy"}
# second_dic = {[1]:"one" , {1:"bir"} : "one"} # TypeError: unhashable type: 'list'
print(first_dic)
# print(second_dic)

xx = dict( bir = "one", iki = "two")
print(xx) # {'bir': 'one', 'iki': 'two'} ==> string olarak return ediyor

sehir ="istanbul"
sehir1 = "ankara"
nufus = 1000
sehirler = {1 : sehir , 2 : sehir1, "nufusum": nufus}
print(sehirler) 
print(sehirler[2],type(sehirler[2])) 
print(sehirler["nufusum"]) 

state_capitals = {'Arkansas': 'Little Rock',
'Colorado': 'Denver',
'California': 'Sacramento',
'Georgia': 'Atlanta'}
state_capitals['Virginia'] = 'Richmond' # adding a new item
print(state_capitals)

state_capitals["California"] = "Istanbul" # updating an item
print(state_capitals)



dict_by_dict = dict(animal = "dog", planet = "neptun", number = 40, is_good = True)
print(dict_by_dict)
print(dict_by_dict.items(),'\n') # dict_items([('animal', 'dog'), ('planet', 'neptun'), ('number', 40), ('is_good', True)]) 
print(dict_by_dict.keys(),'\n') # dict_keys(['animal', 'planet', 'number', 'is_good']) 
print(dict_by_dict.values()) # dict_values(['dog', 'neptun', 40, True])
dict_by_dict.update({'is_bad': False})
print(dict_by_dict) # {'animal': 'dog', 'planet': 'neptun', 'number': 40, 'is_good': True, 'is_bad': False}
del dict_by_dict['animal']
print(dict_by_dict) # {'planet': 'neptun', 'number': 40, 'is_good': True, 'is_bad': False}
print('pi' in dict_by_dict) # False
print('animal' not in dict_by_dict)  # True => remember, we have deleted 'animal'




family= dict(name1 = "ali", name2="hasan", name3= "mehmet")
family1={"name1":"ali","name2":"hasan","name3":"mehmet"}
print(family) # {'name1': 'ali', 'name2': 'hasan', 'name3': 'mehmet'}
family1["name4"]="can"
print(family1) # {'name1': 'ali', 'name2': 'hasan', 'name3': 'mehmet', 'name4': 'can'}

print(list(family1.items())) # [('name1', 'ali'), ('name2', 'hasan'), ('name3', 'mehmet'), ('name4', 'can')]
print(list(family1.keys())) # ['name1', 'name2', 'name3', 'name4']
print(list(family1.values())) # ['ali', 'hasan', 'mehmet', 'can']

family1.update({"name5":"huseyin", "name6" : "salih"})
print(family1) # {'name1': 'ali', 'name2': 'hasan', 'name3': 'mehmet', 'name4': 'can', 'name5': 'huseyin', 'name6': 'salih'}
# family1.update({"name1":33, "c":3}) 
print(family1) #{'name1': 33, 'name2': 'hasan', 'name3': 'mehmet', 'name4': 'can', 'name5': 'huseyin', 'name6': 'salih', 'c': 3}
del family1["name1"], family1["name2"]
print(family1) # {'name3': 'mehmet', 'name4': 'can', 'name5': 'huseyin', 'name6': 'salih'}
print("name4" in family1) # True
print("name7"in family1) # False
print("name7"not in family1) # True
print("bir" in ["bir",1,"clarusway",False]) # True
print("ahmet" in family1.values()) # False
print("Huseyin" in family1.values()) # False => case sensitive

school_records={
    "personal_info":
        {"kid":{"tom": {"class": "intermediate", "age": 10},
                "sue": {"class": "elementary", "age": 8}
               },
         "teen":{"joseph":{"class": "college", "age": 19},
                 "marry":{"class": "high school", "age": 16}
               },
        },
    "grades_info":
        {"kid":{"tom": {"math": 88, "speech": 69},
                "sue": {"math": 90, "speech": 81}
               },
         "teen":{"joseph":{"coding": 80, "math": 89},
                 "marry":{"coding": 70, "math": 96}
               },
        },
}
print(school_records["personal_info"]["teen"]["marry"]["age"]) # 16
print(list(school_records["grades_info"]["teen"]["joseph"].items())) # [('coding', 80), ('math', 89)]
print(school_records["grades_info"]["teen"]["joseph"]) # {'coding': 80, 'math': 89}

friends = {"friend1":{"first":"Sue","last":"Bold"},
           "freind2":{"first":"Steve","last":"Smith"},
           "friend3":{"first":"Sergio","last":"Tatoo"}}
print(friends)

favourite = {"friends":{"friend1":{"first":"Sue","last":"Bold"},
                        "friend2":{"first":"Steve","last":"Smith"},
                        "friend3":{"first":"Sergio","last":"Tatoo"}},
             "family":{"family1":{"first":"Steve","last":"Smith"},
                       "family2":{"first":"Mary","last":"Tisa"},
                       "family3":{"first":"Tom","last":"Happy"}}}
print(favourite)

# SET 
set_1 = {'red', 'blue', 'pink', 'red'}
colors = 'red', 'blue', 'pink', 'red'
set_2 = set(colors)
print(set_1)
print(set_2)

letter = "a b c d e f g g i j k l m n o p r s t u v y z".split()
print(letter)
print(set(letter))

test1={1,"bir",1.0}
print(test1) # {1, 'bir'}
print(len(test1))