"""  
estructura de datos
secuencia ordenada mutable
estan entre []

"""

#Hay dos formas de crear una lista
my_list = list()
my_other_list = []

print(len(my_list))
# en un lista puede haber diferentes tipos de datos

my_list = [1,2,3,"kyu"]
print(len(my_list))
print(my_list)

my_second_list = list((7,8,9,10))
print(my_second_list)

#con el negativo inicia del final
print(my_list[3])
print(my_list[-2])


######################################
my_lista = list(("kyu","leon",23))

nombre,last_name,age = my_lista
print(nombre)


#######################################
#une una nueva lista que une todo
print(my_lista + my_list)

#FORMAS DE INGRESAR DATOS

my_lista.append(23) #agrega al final de la lista
print(my_lista)

my_lista.insert(1,"btcy") #inserta con la pocision
print(my_lista)

my_lista.insert(2,"kou")
print(my_lista)

########################################


#FORMAS DE ELIMINAR
my_lista.remove(23) #elimina el valor de la lista
print(my_lista)

#pop() --- colas
#Quita el ultimo elemento de la lista
#Si se le agrega un argumento, entonces elimina el valor que esta en el indice indicado
my_lista.pop()
print(my_lista)

#otra
print(my_lista.pop())
print(my_lista)

my_lista.pop(1)
print(my_lista)

#eliminar por indice 
del my_lista[1]
print(my_lista)

#borrar todo lo que hay en la lista
my_lista.clear()
print(my_lista)

#COPIAR LISTA EN OTRA

my_kyu = list(("btcy", "Milagros","mel", "ross", 12,15,16,2))
my_new_kyu = my_kyu.copy()

print(my_new_kyu)

#DUB LISTAS
print(my_new_kyu[1:3])
print(my_new_kyu[0:5])

#oRDEMA ALREVES 
my_new_kyu.reverse()
print(my_new_kyu)

#ORDENA EN FORMA ORGANIZADA
    #ordena numeros
#my_new_kyu.sort()
#print(my_new_kyu)

