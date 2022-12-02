from padre import persona

class Docente(persona):
    titulo                 = str
    edad                   = int
    experienciaProfesional = int
    experienciaDocente     = int
    
    def __init__(self, nombre, apellido, titulo, edad, experienciaProfesional, experienciaDocente):
        super().__init__(nombre, apellido)
        self.titulo = titulo
        self.edad = edad
        self.experienciaProfesional = experienciaProfesional
        self.experienciaDocente = experienciaDocente
    
    def BienvenidoDocente(self):
        print("Estimado docente: " + self.nombre, self.apellido + ". Le damos la Bienvenida al IST Yavirac" + "agradecemos contar con sus " + str(self.experienciaProfesional + self.experienciaDocente) + "años de experiencia")

docente1 = Docente("Dayana", "Tafur", "Desarrollador de SF", 24, 2, 1)
docente1.BienvenidoDocente()