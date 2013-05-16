import Image
import numpy as np
import math
from math import *
from sys import argv
import random


def main():
  imagen = color()

def color(): #sacar valorores maximo y minimos de r, g y b  
    im = argv[1]
    img = Image.open(im) 
    pix = img.load()
    ancho,alto = img.size
    lr = list()
    lg = list()
    lb = list()
    
    for i in range(ancho):
	    for j in range(alto):
		    (r,g,b) = img.getpixel((i,j))
		    lr.append(r)
		    lg.append(g)
		    lb.append(b)
    minimor = min(lr)
    maximor = max(lr)
    minimog = min(lg)
    maximog = max(lg)
    minimob = min(lb)
    maximob = max(lb)
    
    print 'minimor',minimor
    print 'maximor',maximor
    print 'minimog',minimog
    print 'maximog',maximog
    print 'minimob',minimob 
    print 'maximob',maximob
    df = image.save('color.png')
    return df 

main()
