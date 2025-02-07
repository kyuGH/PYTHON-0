#concjunto de valores / no modificables (no mutable)

my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (1.1,1.2,1.3)

my_tuple = (35, 15, "kyu")
print(type(my_tuple))
print(my_tuple)

print(my_tuple.count(2))
print(my_tuple.index(15)) #retorna el incice del valor

#puedo unir tuplas

print(my_other_tuple + my_tuple)
print(my_tuple[1:3])

#convertir una tupla en lista

my_tuple = list(my_tuple)
my_tuple.insert(1,"azul")
print(my_tuple)
my_tuple = tuple(my_tuple)
print(type(my_tuple))

#eliminar tupla

del my_tuple