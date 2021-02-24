from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from Lista_Circular import ListaCircular
 
lista = ListaCircular()



salida = False
listaAlpha = []
archivo_Seleccionado = False
def cls():
    r=0
    while r<10:
        print("")
        r=r+1 

def carga():
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    filename = askopenfilename(initialdir="D:\Galeria\Escritorio",filetypes =(("Archivo XML", "*.xml"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()   

def procesar():
    if archivo_Seleccionado == True:
        print("Archivo de datos no seleccionado previamente")
    else:
        doc = minidom.parse("Ejemplo1.xml")
        for matriz in doc.getElementsByTagName('matriz'):
            lista_Elementos = []
            error = False
            matriz_valores = []
            matriz_binaria = []
            matriz_reducida = []
            nombre_Matriz = matriz.getAttribute('nombre')
            n_matriz = matriz.getAttribute('n')
            m_matriz = matriz.getAttribute('m')    
            items = matriz.getElementsByTagName('dato') 
            a = int(n_matriz)+1
            b = int(m_matriz)+1
            for i in range(a):
                matriz_valores.append([])
                for j in range(b):
                    matriz_valores[i].append(0)
            for elem in items:
                x_dato = elem.getAttribute('x')
                y_dato = elem.getAttribute('y')
                valor = int(elem.firstChild.data)
                
                if x_dato > n_matriz or y_dato > m_matriz:
                    print("Error asignacion de valor excede al valor creacion de matriz")    
                    error = True
                else:
                    fila = matriz_valores[int(x_dato)]
                    fila[int(y_dato)] = valor
            for i in range(a):
                matriz_binaria.append([])
                for j in range(b):
                    if matriz_valores[i][j] == 0:
                        matriz_binaria[i].append(0)
                    else:
                        matriz_binaria[i].append(1)
            lista_coincidencia = []
            lista = []
            for i in range (1,a):
                lista.append(i)      
            while len(lista) > 0:
                lis_1 = matriz_binaria[lista[0]]
                g = lista[0]
                lista_coincidencia.append(matriz_valores[g])
                lista.pop(0)
                if len(lista) > 1:
                    for h in lista:
                        coincide = True
                        lis_2 = matriz_binaria[h]
                        for i in range(b):
                            if lis_1[i] != lis_2[i]:     #de momento creo que esto va bien
                                coincide = False
                        if coincide == True:
                            print("coincidio encontrada")
                            lista_coincidencia.append(matriz_valores[i])
                            lista.remove(h)
                else:
                    print("oksov")
                    #agregar la fila restante al listado
                print(lista_coincidencia)
                        
                




                    
                        


while salida == False:
    cls()
    print("Menu principal:")
    print("    1. Cargar archivo")
    print("    2. Procesar archivo")
    print("    3. Escribir archivo salida")
    print("    4. Mostrar datos del estudiante")
    print("    5. Generar grafica")
    print("    6. Salida")
    a = input("Seleccione una opcion: ")
    if (a == '1'):
        carga()
        archivo_Seleccionado = True
        print("Archivo Cargado correctamente")
        a = input()
    elif (a == '2'):
        procesar()
        a = input()
    elif (a == '3'):
        a = input()
    elif (a == '4'):
        a = input()
    elif (a == '5'):
        a = input()
    elif (a == '6'):
        a=input()
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")


