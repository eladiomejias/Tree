# -*- coding: utf-8 -*-
"""          Arbol Binario de Busqueda - Eladio Mejias CI:/ Manuel Perez      """
"""               Arbol de Busqueda Binario: Hijo derecho siempre debe ser mayor a la base o nodo padre            """



""" Clase Base: En esta clase definimos el valor insertado """
class Base:
    """
        Constructor de la clase, se definen las variables der, izq correspondiente a que es un nodo simple al inicio.
        El valor del nodo es el mismo valor pasado por parametro.
    """
    def __init__(self, valor):

        self.der = None
        self.izq = None
        self.valor = valor

""""

    Metodo agregar. Se pasa como parametros dos valores de Base
    (Que serian dos nodos simples donde se escogeran su sitio)
    El primer valor que se ingresa se convierte en el nodo padre.
    Se compara  si el dato ingresado es mayor a su nodo padre,
    dependiendo de este resultado se ubica en izq o der.

"""
def agregar(raiz, nodo):

    if raiz == None:
        raiz = nodo
    else:
        if raiz.valor > nodo.valor:
             if raiz.izq == None:
                raiz.izq = nodo
             else:
              agregar(raiz.izq, nodo)
        elif raiz.valor < nodo.valor:
            if raiz.der == None:
               raiz.der = nodo
            else:
                 agregar(raiz.der, nodo)


""" InOrden     -    Izq // Padre // Der """
""" Parametros que se pasan en la funcion: Base(Cada valor que pudiera existir en el arbol), lista(para almacenarlo) """
def InOrden(base, lista):
        """
        Cuando el valor dado no existe se retorna None y se sigue el procedimientos que se ejecuto antes
        de llamar esta funcion.
        """
        if not base:
            return None

        InOrden(base.izq, lista)

        """

        Itera en todo el arbol hasta encontrar el ultimo izq
        Cuando encuentra el ult izq SIEMPRE quedará null por ser una rama el ultimo.
        Para que esto no afecte retornamos None y la función sigue su procedimiento

        """

        lista.append(base.valor)
        """ Se queda en el ultimo hijo (el que es antes del null), su valor es agregado a la lista """

        InOrden(base.der, lista)

        """ Se cambia al nodo derecho del cual es hijo o padre. """



""" PreOrden     -    Padre // Izq // Der """
""" Parametros que se pasan en la funcion: Base(Cada valor que pudiera existir en el arbol), lista(para almacenarlo) """
def preOrden(base, lista):
    """ Cuando el valor dado no existe se retorna None y se sigue el procedimientos que se ejecuto antes
        de llamar esta funcion """
    if not base:
        return None
    
    """ Se almacena en la lista """
    lista.append(base.valor)
    """ Se cambia el valor del nodo que se evaluara """ 
    preOrden(base.izq , lista)
    """ Se cambia el valor del nodo que se evaluara""" 
    preOrden(base.der, lista)



""" PostOrden     -    Izq // Der // Padre """
""" Parametros que se pasan en la funcion: Base(Cada valor que pudiera existir en el arbol), lista(para almacenarlo) """
def postOrden(base, lista):
    """ Si existe el valor del nodo, se trata de calcular su hijo izq, en dado caso que su hijo izq no se puede conseguir
    la funcion calculara su hijo derecho automaticamente.
    """
    if base is not None:
        postOrden(base.izq, lista)
        postOrden(base.der, lista)
        lista.append(base.valor)

""" ------------------- Impresión y Ordenamiento del Arbol ------------------------ """

resp = "S"
arbol = []

""" Llenado de la lista arbol por cada valor pasado en los metodos de recorrido """
def llenarArbol(arbol, resp):

    if resp.upper() == "N":
        print "Los datos ingresados son: ", arbol
    else:
        valor = input("Ingrese el valor: ")
        arbol.append(valor)
        resp = raw_input("Desea ingresar otro valor? (S/N): ")
        llenarArbol(arbol, resp)

"""  Ordenando el arbol """
def ordenar(arbol, raiz, x):

    if x >= len(arbol):
        print "Tipos de recorridos: "
    else:
        agregar(raiz, Base(arbol[x]))
        x += 1
        ordenar(arbol, raiz, x)


"""  Iniciando el menu del llenado. """
llenarArbol(arbol, resp)
""" Se inicializa el nodo padre con el primer valor ingresado. """
prin = Base(arbol[0])
""" Se ordenan los valores ingresados. """
ordenar(arbol, prin, 1)
""" Inicializando las listas vacias de cada recorrido. """
ino, pre, post = [], [], []

""" Llamada e Impresion de cada Metodo. """
InOrden(prin, ino)
print "InOrden: ", ino
preOrden(prin, pre)
print "PreOrden: ", pre
postOrden(prin, post)
print "PostOrden: ", post
raw_input()
