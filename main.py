print("Hola mundo"):

class persona:
    nombre = str
    edad = int
    
def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad
 
def saluda (self, otra_persona):
    return f'hola {otra_persona.nombre'}, me llamo, {self}
    
if __name__ =="__main__":
    persona1 = persona("Bladimir",24)
    persona2 = persona("Elena", 25)
    
print(persona1.saluda(persona2))

class MiClase:
    nombre = "Bladimir"
    edad = "24"

p1 = MiClase()
print(p1.nombre)

#La funcion __init__()
class persona2:
    nombre = str
    edad = int
    genero = str
    
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad = edad
        self.genero = genero

p2 = persona2.nombre("Bladimir", 24, "masculino")

print(p2.nombre)
print(p2.edad)
print(p2.genero) #la funcion init e usa solamente para ....

#La funcion __str__()

class persona3:
    nombre  = str
    edad = int
    genero = str
    estatura: int
    
    def__init__(self, nombre, edad, genero, estatura):
        self.nombre = nombre
        self.edad = edad = edad
        self.genero = genero
        self.estatura = nombre
    def __str__(self):
        return f'Hola me llamo' {self.nombre, tengo {self.edad}: estatura: {self.estatura}}

p3 = persona3("Juan, 24, "Masculino", 189)
print(p3)

#Metodos dentro de Objetos

class persona4:
    nombre  = str
    semetre = str
    
    def__init__(self, nombre, semetre):
    self.nombre  = nombre
    self.semetre = semetre
    
    def saludo(self):
        print("Bienvenido" + self.nombre + "al " + self.semestre)

p4 = persona4("Antonio", "Segundo Semestre")
p4.saluda()

p4.nombre = "Jonathan"

p4.saludo()

del p4.semetre
p4.saludo()

del p4
p4.saludo()






