from manim import *
import random 
from copy import deepcopy
SCALE = 1 


class Element:
    def __init__(self,val):
        self.val = val
        self.square = Square (side_length= 1 * SCALE,color=BLUE) 
        self.text = Tex(str(self.val), color=WHITE)
        self.text.scale(SCALE)

def swap_mobjects(c1 : Mobject, c2 :Mobject):
    c1_copy, c2_copy = deepcopy(c1), deepcopy(c2)        
    c1_copy.move_to(c2.get_center())
    c2_copy.move_to(c1.get_center())
    return [
        CounterclockwiseTransform(c1, c1_copy),
        CounterclockwiseTransform(c2,c2_copy)
    ]

def swap_elements(e1 : Element, e2 : Element):    
    return [*swap_mobjects(e1.text, e2.text) , *swap_mobjects(e1.square, e2.square)]
