""" 
las ecexpciones se manejan para evitar que el programa se pare,
cuando hay un error
"""
"""def evaluaEdad(edad):
    
    if edad < 0:
        raise ZeroDivisionError("No se permiten edades negativasa")
    if edad <20:
        return "eres muy joven"
    elif edad <40:
        return "eres joven"
    elif edad <65:
        return "eres maduro"
    elif edad<100:
        return "cuidadte ..."
print(evaluaEdad(-5))
print("prueba de contnuacion")"""

num1 = 5
num2 = 5
try :#
    print(num1 + num2)
    print("No se a producido un error")
except:
    print("se ha producido un error")
else:  #opcional
    #se ejecuta si no se produce una escepcion
    print("la ejecucion continua correctamente")
finally: #opcional
    #se ejecuta siempre
    print("La ejecucion continua")
 
numero1 = 8
numero2 = 0   
try:
    print(numero1 / numero2)
    print("Se ejecuto correctamente")
except ValueError:
    print("xxxxx")
except TypeError:
    print("Ingrese los datos correctos")
except ZeroDivisionError:
    print("no se puede dividir entre cero")
    
print("Mensaje de continuacion.....") 
#GUARDAR LA EXCEPCION EN UNA VARIABLE
num3 = 10
num4 = "cinco"

try:
    print(num3 + num4)
    print("satisfactriamente se realizo")
except TypeError as error:
    print(error)