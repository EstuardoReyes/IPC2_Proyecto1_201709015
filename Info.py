class Info():
    def __init__(self,a,b,c,d,f):
        self.n_fila = a
        self.n_columna = b
        self.nombre = c
        self.matriz = d
        self.matriz_entrada = f
    
    def getFila(self):
        return self.n_fila

    def getColumna(self):
        return self.n_columna

    def getNombre(self):
        return self.nombre

    def getMatriz (self):
        return self.matriz

    def getEntrada(self):
        return self.matriz_entrada


    


