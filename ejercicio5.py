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
            