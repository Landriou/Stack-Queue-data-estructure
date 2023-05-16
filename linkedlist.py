class LinkedList:
    head=None

class Node:
    value=None
    nextNode=None

#Añade un elemento a la lista
def add(L, element):
    NodeA = Node()
    NodeA.value = element
    NodeA.nextNode = L.head
    L.head = NodeA
#Devuelve la posicion de un elemento pasado por parametros
def search(L, element):
    currentnode = L.head
    posicion = 0    
    while currentnode != None:
        if currentnode.value == element:
            return posicion
        posicion = posicion + 1
        currentnode = currentnode.nextNode
    return None

#Devuelve la cantidad de elementos en la lista
def length(L):
    currentnode = L.head
    cant = 0
    while currentnode != None:
        cant = cant + 1
        currentnode = currentnode.nextNode
    return cant
#Inserta un elemento en la posicion indicada
def insert(L, element,position):
    flag = True
    contador = 0 
    
    if length(L) < position:
        return None
    if position == 0:
        add(L, element)
        return position
    nodoanterior = 0
    nodoposterior = 0
    Nodo = Node()
    Nodo.value = element
    currentnode = L.head
    while flag: #Copio los punteros de los nodos adyacentes
        contador = contador + 1
        if contador == position:
            flag = False
        if contador == 1:
            nodoanterior = currentnode
            nodoposterior = currentnode.nextNode
        else:
            nodoanterior = nodoposterior
            nodoposterior = nodoposterior.nextNode
    nodoanterior.nextNode = Nodo
    Nodo.nextNode = nodoposterior
    return position
#Elimino un elemento de la lista copiando punteros
#De igual forma q en insert
def delete(L, element):
    if search(L, element) == None:
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if search(L,element) == 0:
        for n in range(length(L)-1):
            currentnode.value = currentnode.nextNode.value
            if n != length(L)-2:
                currentnode = currentnode.nextNode
        currentnode.nextNode = None
        return search(L,element)
    while flag:
        contador = contador + 1
        if contador == search(L, element):
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return search(L,element)
#Devuelve el valor de la posicion indicada
def access(L, position):
    flag = True
    contador = 0
    currentnode = L.head
    value = 0
    if length(L) < position:
        return None
    while flag:
        if contador == position:
            flag = False
        value = currentnode.value
        currentnode = currentnode.nextNode
        contador = contador + 1
    return value
#Cambia el valor de la posicion indicada por el elemento indicado
def update(L, element, position):
    flag = True
    contador = 0
    currentnode = L.head
    if position > length(L):
        return None
    
    while flag:
        if contador == position:
            flag = False
            currentnode.value = element
        contador = contador + 1
        currentnode = currentnode.nextNode
    return position

def deleteposition(L, position):
    if position >= length(L):
        return None
    flag = True
    contador = 0 
    nodoanterior = 0
    nodoposterior = 0
    currentnode = L.head
    if position == 0:
        L.head = currentnode.nextNode
        currentnode.nextNode = None
        currentnode = L.head
        return position
    while flag:
        contador = contador + 1
        if contador == position:
            flag = False
        nodoanterior = currentnode
        nodoposterior = currentnode.nextNode.nextNode
        currentnode = currentnode.nextNode
    nodoanterior.nextNode = nodoposterior
    return position

def switch(L,position1,position2):
    currentnode = L.head
    nodo1 = access(L, position1)
    nodo2 = access(L, position2)
    update(L,nodo2,position1)
    update(L, nodo1, position2)

def imprimirlista(L):
    currentnode = L.head
    while currentnode != None:
        print(currentnode.value, end="  ")
        currentnode = currentnode.nextNode