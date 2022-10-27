class Nodo():
    def __init__(self, informacion, siguiente):
        self.informacion = informacion 
        self.siguiente = siguiente
        informacion,siguiente = None, None

class DatoPolinomio():
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino

class Polinomio():

    def __init__(self):
        self.termino_mayor=None
        self.grado = -1
    
    def crear_termino(polinomio, valor, termino):
        polinomio.termino_mayor=None
        aux = Nodo()
        aux.informacion=DatoPolinomio(valor, termino)
        if(termino > polinomio.grado):
            aux.siguiente = polinomio.termino_mayor
            polinomio.termino_mayor = aux
            polinomio.grado = termino 
        else:
            actual = aux
            while(actual.siguiente is not None and termino <  actual.siguiente.informacion.termino):
                actual = actual.siguiente
                aux.siguiente = actual.siguiente
                actual.siguiente = aux
    
    def obterner_valor(polinomio, termino):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.informacion.termino > termino):
            aux = aux.siguiente
        if(aux is not None and aux.informacion.termino == termino):
            return aux.informacion.valor