#########
def my_function() :
    n = 5 + 1
    return n
print(my_function())
#########
def my_other() :
    print("hola")
    
my_other()
##########
#paso de parametros

def print_name (name,surname):
    print(name + surname)
    print(f"{name} {surname}")
print_name("aly","ema")

#ingresando muchos strings
def print_texts(*texto):
    print(texto)
    
print_texts("hola", "kyu","como estas")

def print_for_texts(*prime):
    for elemento in prime:
        print(elemento.upper())
    print(type(prime))
print_for_texts("python", "c++", "ruby", "java")