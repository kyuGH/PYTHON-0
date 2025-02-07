#tipo de dato
#almacena carios elementos / no elementos duplicados
#accesos diferente
#esta guardao de foma desordenada

my_set = set()
my_other_set = {} #por el momenbto es un dicc

print(type(my_set))
my_other_set = {"kyu", "btdy", 15} # ya es un set

#insertar
my_other_set.add("holi")
print(my_other_set)

#busqueda en el set
print("kyu" in my_other_set)

#eliminar
my_other_set.remove("holi")
print(my_other_set)

#vaciar todo
my_other_set.clear()
print(my_other_set.clear())