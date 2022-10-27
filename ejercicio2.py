class Alumno():

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno es: {self.nombre}")

    def __str__(self):
        return f"El alumno {self.nombre}, ha sacado un {self.nota}."

    def calificacion(self):
        if self.nota >= 5:
            return(f"{self.nombre} ha aprobado con un {self.nota}.")
        else:
            return(f"{self.nombre} ha suspendido con un {self.nota}.")

alumno1 = Alumno("Manuel García", 8)
alumno2 = Alumno("Jorge Paredes", 4)
alumno3 = Alumno("Mario Fernandez", 5)