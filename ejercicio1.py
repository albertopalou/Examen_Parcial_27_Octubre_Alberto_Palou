class Alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} se ha creado con exito")

    def calificacion(self):
        if self.nota >= 5:
            return(f"{self.nombre} ha aprobado con un {self.valor}.")
        else:
            return(f"{self.nombre} ha suspendido con un {self.valor}.")

alumno1 = Alumno("Manuel García", 8)
alumno2 = Alumno("Jorge Paredes", 4)
alumno3 = Alumno("Mario Fernandez", 5)

print(alumno1.calificacion())
print(alumno3.calificacion())
print(alumno2.calificacion())

