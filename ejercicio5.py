class Matriz():
    def __init__(self, filas: list[list[int]]):
        error = TypeError()
        if len(filas) != 0:
            cols = len(filas[0])
            if cols == 0:
                raise error
            for filas in filas:
                if len (filas) != cols:
                    raise error
                for value in filas:
                    if not isinstance(value, (int, float)):
                        raise error
            self.filas = filas
        else:
            self.filas = []

    def columnas(self) -> list[list[int]]:
        return[[filas[i] for filas in self.filas] for i in range(len(self.filas[0]))]

    def num_filas(self) -> int:
        return len(self.filas)
    
    def num_columnas(self) -> int:
        return len (self.filas[0])
    
    def orden(self) -> tuple[int, int]:
        return(self.num_filas, self.num_columnas)

    def cuadrada(self) -> bool:
        return self.orden[0] == self.orden[1]
    
    def identidad(self):
        valores = [
            [0 if columna_num != filas_num else 1 for columna_num in range(self.num_filas)]
            for filas_num in range(self.num_filas)
        ]
        return Matriz(valores)

    def determinante(self) -> int:
        if not self.cuadrada:
            return 0
        if self.orden == (0,0):
            return 1
        if self.orden == (1,1):
            return int(self.filas[0][0])
        if self.orden == (2,2):
            return int(
                (self.filas[0][0] * self.cofactors().filas[0][columna])
                for columna in range(self.num_columnas)
            )

