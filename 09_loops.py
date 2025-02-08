n=1
while n != 10:
    print(n)
    n=n+1
#se puede usar un break y continue
   
while n<5:
    print(n)
    n+=2
else:
    print("n es mayor que 5")
    
#################################
"""
import random
adivina = int(random.random()*100)
print("BIENVENIDO AL JUEGO")
print(adivina)
entrada = int(input("Adivina el numero (entre 1 y 100): "))
i = 1
while entrada != adivina:
    if entrada > adivina:
        print("El numero es menor. ")
        entrada = int(input("Intente de nuevo: "))
    else :
        print("El numero es mayor. ")
        entrada = int(input("Intente de nuevo: "))
    i += 1   
print("¡Felicidades! Adivinaste el número en", i, " intentos.")       
"""
#####################################
print("iniciando for")
#FOR

#LISTAS
my_list = [45,12,15,16,12,13]
#TUPLAS
my_tuple = ("a","b","c") #no modificables
#SETS
my_sets = {"beny","selena","kiara"} #diferente orden
#DICIONARIOS
my_dic = {"name": "kyu", "age":15, "lenguajes":{"kotlin","python","java"}}

for element in my_list:
    print(element)

for index in my_tuple:
    print(index)
    
for elemento in my_sets:
    print(elemento)
for indice in my_dic:
    print(indice)
    
for elemento in my_dic["lenguajes"]:
    print(elemento)
    
for indice in my_dic.values():
    print(indice)
    
