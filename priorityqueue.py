from linkedlist import *
class PriorityQueue:
    head=None

class PriorityNode:
	value=None
	nextNode=None
	priority=None

def cambiopriori(nodo1, nodo2):
    priori1 = nodo1.priority
    priori2 = nodo2.priority
    nodo2.priority = priori1
    nodo1.priority = priori2

def enqueue_priority(Q,element, priority):
    NodeA = PriorityNode()
    NodeA.value = element
    NodeA.priority = priority
    NodeA.nextNode = Q.head
    Q.head = NodeA
    currentnode = Q.head #Añado el elemento al final de la cola
    position1 = 0
    position2 = 1
    if currentnode.nextNode != None:
        siguiente = currentnode.nextNode
        for n in range(length(Q)-1): #Recorro la cola 
            if currentnode.nextNode != None:
                if currentnode.priority > siguiente.priority: #Voy comparando las prioridades
                    cambiopriori(currentnode,siguiente) #Cambio las prioridades
                    switch(Q,position1,position2) #Cambio el valor de los nodos
            position1 = position1 + 1
            position2 = position2 + 1
            currentnode = currentnode.nextNode
            if currentnode.nextNode != None:
                siguiente = currentnode.nextNode
    return position1


def dequeue_priority(Q):
    if length(Q) == 0:
        return None
    element = access(Q,length(Q)-1)
    deleteposition(Q, length(Q)-1)
    return element

