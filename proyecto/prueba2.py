import cv
import Image
import numpy as np
import math
from math import *

def detect_painting(image):
    image = filtro(image)
    img = mascara(image)


def mascara(image):
    sobelx = ([-1,0,1],[-2,0,2],[-1,0,1]) #gradiente horizontal
    sobely = ([1,2,1],[0,0,0],[-1,-2,-1]) # gradiente vertical    
    image,gx,gy,minimo,maximo,conv=convolucion(sobelx,sobely,image)

  
def convolucion(h1,h2,image):
    pixels = image.load()
    ancho,alto = image.size 
    a=len(h1[0])
    conv = np.empty((ancho, alto))
    gx=np.empty((ancho, alto))
    gy=np.empty((ancho, alto))
    minimo = 255
    maximo = 0
    for x in range(ancho):
        for y in range(alto):
            sumax = 0.0
            sumay = 0.0
            for i in range(a): 
                for j in range(a): 
                    try:
                        sumax +=(pixels[x+i,y+j][0]*h1[i][j])
                        sumay +=(pixels[x+i,y+j][0]*h2[i][j])

                    except:
                        pass
            gradiente = math.sqrt(pow(sumax,2)+pow(sumay,2))
            conv[x,y]=gradiente
            gx[x,y]=sumax
            gy[x,y]=sumay
            gradiente = int(gradiente)
            pixels[x,y] = (gradiente,gradiente,gradiente)
            p = gradiente
            if p <minimo:
                minimo = p
            if  p > maximo:
                maximo = p
    image.save('MASCARA.png')
    return image,gx,gy,minimo,maximo,conv

    def normalizar(image):
        #inicio=time()
        pixels = image.load()
        r = maximo-minimo
        prop = 255.0/r
        ancho,alto = image.size
        for i in range(ancho):
            for j in range(alto):
                p =int(floor((conv[i,j]-minimo)*prop))
                pixels[i,j]=(p,p,p);
       # print 'TERMINO'
        #fin = time()
        #tiempo_t = fin - inicio
       # print "Tiempo que tardo en ejecutarse normalizar = "+str(tiempo_t)+" segundos"

        return image

def binarizar(img):
        #inicio = time()
    pixels = img.load()
    ancho,alto = img.size
    minimo = int(argv[2])
    for i in range(ancho):
        for j in range(alto):
            if pixels[i,j][1] < minimo:
                p=0
            else:
                p= 255
            pixels[i,j]=(p,p,p)
        #fin  =time()
        #tiempo_t = fin - inicio
       # print "Tiempo que tardo en ejecutarse binzarizar = "+str(tiempo_t)+" segundos"

    return img

def filtro(image):
    image,matriz = escala_grises(image)
    pixels = image.load()
    ancho, alto =image.size
    lista = [-1,0,1]
    for i in range(ancho):
        for j in range(alto):
            promedio = vecindad(i,j,lista,matriz)
            pixels[i,j] = (promedio,promedio,promedio)
    image.save('FILTRO.png')
    return image

def escala_grises(image):
    image = Image.open(image) 
    pixels = image.load()
    ancho,alto = image.size
    matriz = np.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = image.getpixel((i,j))
            escala = (r+g+b)/3
            pixels[i,j] = (escala,escala,escala)
            matriz[i,j] = int(escala)
    df = image.save('escala.png')
    return image,matriz 

    
def vecindad(i,j,lista,matriz):
    promedio = 0
    indice  = 0
    for x in lista:
        for y in lista:
            a = i+x
            b = j+y
            try:
                if matriz[a,b] and (x!=a and y!=b):
                    promedio += matriz[a,b] 
                    indice +=1            
            except IndexError:
                pass
            try:
                promedio=int(promedio/indice)
                return promedio
            except ZeroDivisionError:
                return 0
  

def main():
    cam=cv.CaptureFromCAM(0)
    while True:
        im =cv.QueryFrame(cam)
        snapshot = im
        image_size = cv.GetSize(snapshot)
        cv.SaveImage("test.png",im)
        imagen=cv.CreateImage(image_size,cv.IPL_DEPTH_8U,3)
        detect_painting("test.png")
        cv.ShowImage('Camara', snapshot)
        if cv.WaitKey(30)==27:
            break
main()
