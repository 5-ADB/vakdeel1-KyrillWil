# elke oefening in een appart bestand

#ai gebruikt voor controle

#integer
nummer = 1
#string
naam = "Kyrill"
#bool
isWaar = True
#tupple
tupple1 = (1, 2, 3)
#list
list1 = ["melk", "boter", "appel"]
#toevoegen list
list1.append("eieren")
#verwijderen list
list1.remove("boter")
#lengte list
print(len(list1))
#beperkte lengte list
print(list1[1:4])
#set
set1 = {1,2,3}
#set toevoegen
set1.add(4)
#set verwijderen
set1.remove(1)
#sets vergelijken
set2 = {1,3,4}
print(set1 & set2)
print(set1|set2)
print(set1 - set2)
print(set1 ^ set2)
#dict
woordenboek = {"naam": "Kyrill", "leeftijd": 17}
#dict waarde veranderen
woordenboek["leeftijd"] = 18
#dict keys zien
key = dict.keys()
print(key)
#dict waarde zien
value = dict.values()
print(value)

#type zien
print(type(list1))

print(type(tupple1))