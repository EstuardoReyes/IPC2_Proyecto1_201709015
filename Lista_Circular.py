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
        

    def get_Primero(self):
        return self.primero

    def buscar(self, nomb):
        aux = self.primero
        head = self.primero
        salir = False
        if self.Vacia() == True:
            return False
        else: 
            if self.primero == self.ultimo:
                return False
            else:
                salir == False
                while salir == False:
                    if (aux.getDato().getNombre() == nomb):
                        salir = True
                        return True
                    if (aux.siguiente != head):
                        aux = aux.siguiente
                    else:
                        salir = True  
                return False

    
    