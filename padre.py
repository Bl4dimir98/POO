#Herencia en Python
class persona1:
        nombre   = str
        apellido = str
        
        def __init__(self, nombre, apellido):
            self.nombre   = nombre
            self.apellido = apellido
        
        def imprimir(self):
            print(self.nombre, self.apellido)

x = persona1("Alexander", "Flores")
x.imprimir()

class estudiante:
    pass

y = estudiante("Jeremy", "Cañizares")
y.imprimir()


class estudiante(persona1):
    edad = int
    
    def __init__(self, nombre, apellido, edad):
        persona1.__init__(self, nombre, apellido, edad)
        self.edad = edad
estudiante1 = estudiante("Carlos", "Dell", 30)
estudiante1.imprimir()

#Agregar metodos a una herencia
class student1(persona1):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
    
    def bienvenido(self):
        print("Bienvenido " + self.apellido + "al " + self.semestre + " ingresa a los " + str(self.edad) + " años de edad") #str(init) para poder cambiar el formato del dato

p5 = student1("Diego", "Yanez", 29, "segundo")

