
#plantila de un ojeto con atributos y metodos
#no se le ingreso nada
class Person:
    pass 

class Humano:
    #para ingresar parametros
    #self guarda la referencia
    def __init__(self):
        print("soy un humano")
    
    def hablar(self,mensaje):
        print(mensaje)
    

pedro = Humano()

pedro.hablar("hola")

#INGRESANDO ATRIBUTOS
class Humano:
    
    def __init__(self):
        self.edad = 25
        print("soy un humano")
    
    def hablar(self,mensaje):
        print(mensaje)
    

pedro = Humano()
print("soy pedro y tengo" + str(pedro.edad))
print(f"Soy pedro y tengo : {pedro.edad}")
pedro.hablar("hola")

#########################
#ejemplo personaje

class Personaje:
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def atributos(self): #muestra los datos actuales
        print("\n",self.nombre, ": ")
        print(".Fuerza: ", self.fuerza)
        print(".Inteligencia: ", self.inteligencia)
        print(".defensa: ", self.defensa)
        print(".vida: ", self.vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza 
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida = 0
        print(self.nombre, " esta muerto")
    ####  el daño que relaiza nuestro personaje a otro  
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    #calcula el daño y modificar la vidad del enemigo con ese daño
    def atacar(self, enemigo):
        daño = self.daño(enemigo) 
        enemigo.vida = enemigo.vida - daño 
        print(self.nombre, " ha realizado ", daño, " puntos de daño a ", enemigo.nombre)  
        if enemigo.esta_vivo():
            print("la vida del enemigo ",enemigo.nombre, "es :", enemigo.vida )
        else: 
            enemigo.morir()
        
    def get_fuerza(self):
        return self.fuerza
    
    def set_fuerza(self,fuerza):
        if fuerza < 0 :
            print("ERROR!!.Ingrese un numero positivo")
        else:
            self.fuerza = fuerza
                      
persona1 = Personaje("Goku",10,6,9,10)
enemigo1 = Personaje("Vegeta",9,7,2,5)
#print(persona1.vida)
persona1.atributos()
enemigo1.atributos()
#persona1.subir_nivel(5,2,3)
#persona1.atributos()
#print(persona1.esta_vivo())
#print(persona1.daño(enemigo1))
#persona1.atacar(enemigo1)
persona1.atacar(enemigo1)
enemigo1.atributos()
print(persona1.defensa)
"""para realizar encapsulamiento debo agregar __ antes de cada atibuto o metodo
. Una vez encapsuado ya no se podra usarlo fuera de la clase, pero
si queremos usarlo debemos crear get y set de c/u
    *get --> acceder
    *set --> modificar
"""
#print(persona1.get_fuerza())
#persona1.set_fuerza(-5)
#persona1.atributos()

#HERENCIA

class Gerreo(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    def atributos(self):
        super().atributos()
        print(".espada: ", self.espada)
    def cambiar_arma(self):
        opcion = int(input("\nElije un arma:\n\t (1) Acero Valyrio, daño 8.\n\t (2) Mata dragones, daño 10 : "))  
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")
        #daño = fuerza * espada - defensa del enmigo
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
gerrero = Gerreo("Alfa",20,10,10,100,5)
gerrero.atributos()
#print(gerrero.espada) 
gerrero.cambiar_arma()   
gerrero.atributos()

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    def atributos(self):
        super().atributos()
        print(".libro: ", self.libro)
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa
        
mago1 = Mago("Odette",20,15,16,10,8)
mago1.atributos()

#POLIMORFISMO
""" 
Permite que diferentes clases usen el mismo metodo, pero con 
implemetaciones distintas
"""
class Cafe():
    def que_soy(self):
        print("soy un cafe")
class Te():
    def que_soy(self):
        print("soy un te")
def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Cafe())

combatiente1 = Gerreo("Sun", 10,5,8,10,8)
combatiente2 = Mago("Kadita", 8, 10,8,10,10)

def combate(jugador1, jugador2):
    turno = 0
    while jugador1.esta_vivo() and jugador2.esta_vivo():
        print("\nTurno", turno)
        print(">>>Accion de ", jugador1.nombre, ":", sep="")
        jugador1.atacar(jugador2)
        print(">>>Accion de ", jugador2.nombre, ":", sep="")
        jugador2.atacar(jugador1)
    if jugador1.esta_vivo():
        print("\nHa ganado",jugador1.nombre)
    elif jugador2.esta_vivo():
        print("\nHa ganado",jugador2.nombre)
    else:
        print("\nEmpate")
combate(combatiente1,combatiente2)