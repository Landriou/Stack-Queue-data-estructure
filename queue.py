from linkedlist import *
from algo1 import *

def enqueue(Q, element):
    add(Q,element)

def dequeue(Q):
    position = length(Q)
    if position == 0:
        return None
    element = access(Q,position-1)
    deleteposition(Q, position-1)
    return element
