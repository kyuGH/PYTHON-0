import random


def sum(num1,num2,num3):
    print(num1+num2+num3)
    
def tabla_multiplicar(num):
    for ind in range(1,13):
        print(f"{num} x {ind} = {num*ind}")
    
if __name__ == "__main__":
    tabla_multiplicar(8)

"""opciones = ["rojo", "verde", "azul"]
color = random.choice(opciones)  # Selecciona un color aleatorio
print(color)"""