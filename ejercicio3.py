class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print(f"El constructor {self.nombre} se ha creado con exito")

    def __str__(self):
        return (f"El producto {self.nombre}, con código {self.codigo}, tiene un precio de {self.precio} y es {self.tipo}")
    
    def modificar(self):
        pass

producto1 = Producto("45124", "Leche", 3, "Envase")
producto2 = Producto("74852", "Platano", 1, "Fruta")
producto3 = Producto("04373", "Cereales", 4, "Caja")

print(producto1)


