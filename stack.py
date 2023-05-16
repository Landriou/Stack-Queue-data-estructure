from linkedlist import *
from algo1 import *

def push(S, element):
    add(S, element)

def pop(S):
    if length(S) == 0:
        return None
    element = access(S,0)
    deleteposition(S, 0)
    return element
