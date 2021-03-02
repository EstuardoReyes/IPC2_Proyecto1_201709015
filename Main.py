from tkinter import Tk     
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from Lista_Circular import ListaCircular
from Info import Info
from xml.etree import ElementTree
from graphviz import Digraph
import os

listaCircular = ListaCircular()



salida = False
listaAlpha = []
archivo_Seleccionado = False
procesar = False

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

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
    if archivo_Seleccionado == False:
        print("Archivo de datos de entrada no seleccionado previamente")
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
            for i in range (1,a):   # crea una lista con los valores de 1 - numero de filasas
                lista.append(i)     
             
            while len(lista) > 0: 
                lista_coincidencia.clear()  # mientras haya elementos en la lista seguira recorriendo lista
                lis_1 = matriz_binaria[lista[0]]    # crea una copia del valor de la lista[0]
                g = lista[0]        # g va a ser el valor de la fila 
                lista_coincidencia.append(matriz_valores[g])  #se agrega este valor a la lista de coincidencia 
                lista.pop(0)       # se elimina el primer valor de la lista
                if len(lista) > 1: # mientras en la lista hayan mas de 1 elemnto
                    for h in lista: # recorre los numeros que quedan en la lista
                        coincide = True  
                        lis_2 = matriz_binaria[h]  
                        for i in range(b):
                            if lis_1[i] != lis_2[i]:     #de momento creo que esto va bien
                                coincide = False
                        if coincide == True:
                            print("coincidio encontrada")
                            lista_coincidencia.append(matriz_valores[h])
                            lista.remove(h)
                    # sumar todos los elementos
                listafinal = []
                listafinal.clear()
                listafinal = [0]*(b)
                li = []
                listafinal[0] = g
                for q in range(len(lista_coincidencia)):
                    li = lista_coincidencia[q]
                    for w in range (b):
                        listafinal[w] = listafinal[w] + li[w]
                    listafinal.append(len(lista_coincidencia))                   
                matriz_reducida.append(listafinal)
                    #agregar la fila restante al listado
            mat = Info(n_matriz,m_matriz,nombre_Matriz,matriz_reducida,matriz_valores)
            listaCircular.Agregar(mat)
                          
def escribir():
    if archivo_Seleccionado == False:
        print("Archivo de datos de entrada no seleccionado previamente")
    if procesar == False:
        print("Proceso de archivo de entrada no realizado previamente")
    
    else:
        root = Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        rutadeldirectorio=askdirectory()
        root.update()
        root.destroy() 
        nombre_archivo = input("Ingrese nombre del archivo (sin .xml): ")
        archivo = rutadeldirectorio+"/"+nombre_archivo+".xml"
        aux = listaCircular.get_Primero()
        head = listaCircular.get_Primero()
        salir = False
        listaNodo = []
        while salir == False:
            listaNodo.append(aux) 
            if (aux.siguiente != head):
                aux = aux.siguiente
            else:
                salir = True  
        matrices = Element("matrices")
        for data in listaNodo:
            d = len(data.getDato().getMatriz())
            h = len(data.getDato().getMatriz()[0])
            matriz = SubElement(matrices,'matriz', nombre=data.getDato().getNombre() ,n=str(d) ,m=str(h-3),g=str(d))
            for i in range(int(data.getDato().getFila())-1):
                for j in range(1,int(data.getDato().getColumna())+1):
                    ma = data.getDato().getMatriz()
                    dato = SubElement(matriz,'Dato',x=str(i+1),y=str(j))
                    dato.text = str(ma[i][j])
            for t in range(int(data.getDato().getFila())-1):
                ma = data.getDato().getMatriz()
                frecuencia = SubElement(matriz, 'frecuencia', g=str(ma[t][0]))
                frecuencia.text = str(ma[t][int(data.getDato().getColumna())+1])
        archiv = open(archivo,'w')
        archiv.write(prettify(matrices))

def estudiante():
    print("Edwin Estuardo Reyes Reyes")
    print("201709015")
    print("Introduccion a la Programacion y Computacion Seccion 'B' ")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")

def graphi():
    if archivo_Seleccionado == False:
        print("Archivo de datos de entrada no seleccionado previamente")
    if procesar == False:
        print("Proceso de archivo de entrada no realizado previamente")
    else:
        print('Matrices Almacenadas')
        aux = listaCircular.get_Primero()
        head = listaCircular.get_Primero()
        salir = False
        salir2 = False
        listaNodo = []
        i=1
        while salir2 == False:
            while salir == False:
                print(str(i)+". "+aux.getDato().getNombre())
                i = i+1
                listaNodo.append(aux) 
                if (aux.siguiente != head):
                    aux = aux.siguiente
                else:
                    salir = True
            a = input("Seleccione 1 matriz: ")
            if int(a)<=i-1 and int(a)>=1:
                nodoUsar = listaNodo[int(a)-1]
                break
                salir2 = True
            else:
                print("Seleccione una matriz entre las opciones")
        nom = nodoUsar.getDato().getNombre()
        g = Digraph('unix', filename='Reporte',node_attr={'color': 'lightblue2', 'style': 'filled'})
        g.edge('Matrices', nom)
        g.edge(nom, 'n='+nodoUsar.getDato().getFila())
        g.edge(nom, 'm='+nodoUsar.getDato().getColumna())
        matrizUsar = nodoUsar.getDato().getEntrada()
        for i in range(1,len(matrizUsar[0])):
            listaNumeros = []
            for j in range(1,len(matrizUsar)):
                listaNumeros.append(matrizUsar[j][i])
            print(listaNumeros)
            g.edge(nom,"["+str(1)+","+str(i)+"] = "+str(listaNumeros[0]))
            for q in range(1,len(listaNumeros)):
                g.edge("["+str(q)+","+str(i)+"] = "+str(listaNumeros[q-1]),"["+str(q+1)+","+str(i)+"] = "+str(listaNumeros[q]))
        g.view()


                    
                    
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
        escribir()
        a = input()
    elif (a == '4'):
        estudiante()
        a = input()
    elif (a == '5'):
        graphi()
        a = input()
    elif (a == '6'):
        a=input()
        salida = True
    else:
        print("Opcion "+a+" no se encuentra entre las opciones")


