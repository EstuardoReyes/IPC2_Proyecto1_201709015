from Nodo import Nodo

class ListaCircular():
    

    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def Vacia(self):
        return self.primero == None
    
    def Agregar(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else: 
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero
        
    def Recorrer(self):
        aux = self.primero
        while aux.siguiente != self.primero:
            print(aux.dato.nombre)
            print(aux.dato.matriz)
            aux = aux.siguiente 
        print(aux.dato.nombre) 
        print(aux.dato.matriz)

    def get_Primero(self):
        return self.primero
    
    