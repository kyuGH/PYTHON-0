#
my_dict = dict()
my_other_dic = {}

print(type(my_dict))

my_other_dic = {"Nombre: ":"kyu", "Apelido: ": "leon", "Edad: ":23, 1:"python"}

my_dic = {
    "Nombre: ":"kyu", 
    "Apelido: ": "leon", 
    "Edad: ":23, 
    "lenguajes": {"c++","python","kotlin"},
    1:1.177
    }
print(my_other_dic)
print(my_dic)

#visualizar datos
print(my_dic["Apelido: "])

#agregar  mas campos

my_dic["calle "] = "los postes"
print(my_dic)

#Elinar datos

del my_dic["calle "]
print(my_dic)

print(my_dic["lenguajes"])

#verifcar si hay  un elemento / busca pot campo

print("Apelido: " in my_dic)

print(my_dic.items()) #muestra la lista de todo
print(my_dic.keys()) #muestra solo las calves
print(my_dic.values()) #muestra solo los valores