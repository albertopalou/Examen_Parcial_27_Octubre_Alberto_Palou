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
    
    def order(self) -> tuple[int, int]:
        return(self.num_filas, self.num_columnas)
        