my_string = "mi cadena"
my_other_string = "mi otra cadena"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
print(my_string, my_other_string)

#string con salto de linea
my_string_new_line = "primera cadena \nsegunda cadena in new line"
print(my_string_new_line)
my_string_tabulado = "\thola kyu"
print(my_string_tabulado)

#cuando usamos \\ anula el \n y \t

name, age = "kyu", 22
#%s -- string
#%d -- entero
#%f -- flotante
print("Mi nombre es {} y mi edad es {} ".format(name, age)) 
print("Mi nombre es %s y mi edad es %d " %(name, age))
print(f"Mi nombre es {name} y mi edad es {age}")

# Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(e)

#FUNCIONES

print(language.capitalize()) #mayuscula en la primera palabra
print(language.upper()) #mayuscula todo
print(language.count("t")) #cuenta la cantidad de veces que se repite algo
print(language.isnumeric()) #determina si es numero
#lower() -- convierte en minuscula
print(language.lower().isupper())
#isupper() -- verifica si todo es mayucula  (T or F)
print(language.startswith("py")) # comprueba si una cadena de texto comienza con otra
print("Py" == "py") #no es lo mismo