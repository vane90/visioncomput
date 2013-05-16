#si
import pygame, sys, time
from pygame.locals import *
import Image
import numpy as np
import math
from sys import argv
from math import *

ima='nuevo.png'
ancho=300
alto=400

a_ventana=None
def open_i(): #imagenconmovimiento
    imagen=Image.open('nuevo.png')
    pixels=imagen.load()
    return pixels
    
def detect_movi(p1,p2): #detecta_movi
    global img,ancho,alto
    pixt=[p1,p2]
    for p in pixt:
        print 'FORMA'
        formas(p)
    return            

def deteccion(ima,im):
    imagen,masa,centros=c_color(ima,im)
    return masa,imagen,centros


def formas(pixt): #toma_formas
    image = filtrar(pixt)
    print 'salio de filtro'
    raw_input()
    image_cent,minimo,maximo,gx,gy,con = mascara(image)
    pix_nor=normalizar(image_cent,minimo,maximo,con)
    pix_bin= binar(pix_nor)
    deteccion(pix_bin)



def c_color(im,imag): #aplica bfs
    pixels=im
    global ancho,alto
    porcentaje=[]
    fondos=[]
    centro_m=[]
    masa=[]
    ancho,alto=im.size
    t_pixels=ancho*alto
    c=0
    pinta=[]
    f=0
    m=[]
    for i in range(ancho):
        for j in range(alto):
            pixn = pixels[i,j]
            r,g,b= random.randint(0,255),random.randint(0,255), random.randint(0,255)
            fondo=(r,g,b)
            if (pixn==(0,0,0)):
                
                c +=1
                origen=(i,j)
                num_pixels,ab,od,puntos=bfs(pixn,origen,imag,fondo)
                p=(num_pixels/float(t_pixels))*100
                if p>.3:
                    centro=(sum(ab)/float(num_pixels),sum(od)/float(num_pixels))
                      
                    masa.append(num_pixels)
                    #v=detectar_elipse(num_pixels,im,centro,puntos,fondo)
                    porcentaje.append(p)
                    
                    fondos.append(fondo)
                    centro_m.append(centro)
    print centro
    imprimir_porcentajes(porcentaje)
    return im,m,centro_m

def bfs(pix,origen,im,fondo):
    pixels=pix
    cola=list()
    l=[-1,0,1]
    ab=[]
    od=[]
    puntos=[]
    cola.append(origen)
    original = pixels[origen]
    num=1
    while len(cola) > 0:
        (i,j)=cola.pop(0)
        actual = pixels[i,j]
        if actual == original or actual==fondo:
            for x in lista:
                for y in l:
                    a= i+x
                    b = j+y 
                    try:
                        if pixels[a,b]:
                            contenido = pixels[a,b]
                            if contenido == original:
                                pixels[a,b] = fondo
                                ab.append(a)
                                od.append(b)
                                num +=1
                                cola.append((a,b))
                                puntos.append((a,b))
                    except IndexError:
                        pass
    return num,ab,od,puntos

def normalizar(image,minimo,maximo,con):
    pixels=image.load()
    global anocho,alto
    r = maximo-minimo
    prop = 255.0/r
    for i in range(ancho):
        for j in range(alto):
            p =int(floor((con[i,j]-minimo)*prop))
            pixels[i,j]=(p,p,p);
    image.save('normaliza.png')
    return image

def binar(ima):
    global anocho,alto
    pixels=img.load()
    img.save('binarizada.png')
    minimo = int(argv[1])
    for i in range(ancho):
        for j in range(alto):
            print pixels[i,j][0]
            if pixels[i,j][0] < minimo:
                p=0
                #print 'entro al if'
                #raw_input()
            else:
                p= 255
            pixels[i,j]=(p,p,p)
    img.save('binarizada.png')
    return img

def mascara(image):
#Mascara Sobel
    masc_x = ([-1,0,1],[-2,0,2],[-1,0,1]) #gradiente horizontal
    masc_y = ([1,2,1],[0,0,0],[-1,-2,-1]) # gradiente vertical    
    pixels,minimo,maximo,gx,gy,con=conv(masc_x,masc_y,image)
    return pixels,minimo,maximo,gx,gy,con

    
def conv(h1,h2,image): #Deteccion de bordes
    global ancho,alto
    pixels=image.load()
    a=len(h1[0])
    con = np.empty((ancho, alto))
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
            con[x,y]=gradiente
            gx[x,y]=sumax
            gy[x,y]=sumay
            gradiente = int(gradiente)
            pixels[x,y] = (gradiente,gradiente,gradiente)
            p = gradiente
            if p <minimo:
                minimo = p
            if  p >maximo:
                maximo = p
                image.save('convolucion.png')
    return image,minimo,maximo,gx,gy,con

def filtrar(pix):
    global ancho,alto
    imagen = Image.new('RGB', (ancho, alto), (255, 255, 255))
    image=escala_g(pix,imagen)
    print 'toma grises'
    print 'hace a filtro'
    pixels=image.load()
    lista = [-1,0,1]
    for i in range(ancho):
        for j in range(alto):
            promedio = vecindad(i,j,lista,image)
            pixels[i,j] = (promedio,promedio,promedio)
    image.save('filtrado.png')
    return image

def vecindad(i,j,lista,image):
    pixels=image.load()
    promedio = 0
    indice  = 0
    for x in lista:
        for y in lista:
            a = i+x
            b = j+y
            try:
                if pixels[a,b] and (x!=a and y!=b):
                   # print 'entro al if'
                    promedio += pixels[a,b][0] 
                    indice +=1            
            except IndexError:
                pass
    try:
        promedio=int(promedio/indice)
        return promedio
    except ZeroDivisionError:
        return 0

def escala_g(pix,image):
    p=image.load()
    global ancho,alto
    pixels = pix
    matriz = np.empty((ancho, alto))
    for i in range(ancho):
        for j in range(alto):
            (r,g,b) = pixels[i,j]
            escala = (r+g+b)/3
            pixels[i,j] = (escala,escala,escala)
            p[i,j]=(escala,escala,escala)
    image.save('escala.png')
    return image


def main():

    anterior=None
    siguiente=None
    global img,ventanan
    pygame.init()
    ancho = 400
    alto = 400
    ventanan= pygame.display.set_mode((ancho, alto), 0, 32)
    pygame.display.set_caption('Deteccion de Movimiento')

    bajaizq = 1
    bajader = 3
    subeizq = 7
    subeder = 9
    
    mueverect = 4
    rojo = (25, 120, 0)
    verde = (0, 255, 0)
    azul = (0, 0, 255)
    

    br = {'rect':pygame.Rect(300, 80, 60, 100), 'color':azul, 'dir':subeizq}

    recta = [br]
    

    while True:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    
        ventanan.fill((255,255,255))
        
        for b in recta:
            
            if b['dir'] == bajaizq:
                b['rect'].left -=mueverect 
                b['rect'].top += mueverect
            if b['dir'] == bajader:
                b['rect'].left += mueverect
                b['rect'].top += mueverect
            if b['dir'] == subeizq:
                b['rect'].left -= mueverect
                b['rect'].top -= mueverect
            if b['dir'] == subeder:
                b['rect'].left += mueverect
                b['rect'].top -= mueverect

        
            if b['rect'].top < 0:
                
                if b['dir'] == subeizq:
                    b['dir'] = bajaizq
                if b['dir'] == subeder:
                    b['dir'] = bajader
            if b['rect'].bottom > ancho:
                # block has moved past the bottom
                if b['dir'] == bajaizq:
                    b['dir'] = subeder
                if b['dir'] == bajader:
                    b['dir'] = subeder
            if b['rect'].left < 0:
            # block has moved past the left side
                if b['dir'] == bajaizq:
                    b['dir'] = bajader
                if b['dir'] == subeizq:
                    b['dir'] = subeder
            if b['rect'].right > alto:
                # block has moved past the right side
                if b['dir'] == bajader:
                    b['dir'] = subeizq
                if b['dir'] == subeder:
                    b['dir'] = subeizq

        # draw the block onto the surface
        #if anterior==None:
        #    anterior=imagen
        pygame.draw.rect(ventanan, b['color'], b['rect'])
        im='nuevo.png'
        pygame.image.save(ventanan,ima)
        #img='nuevo.png'
        if anterior==None:
            pix_a=open_i()
            anterior=pix_a
            print 'anterior',anterior
        else:
            pix_s=open_i()
            siguiente=pix_s
            print 'siguiente'
            detect_movi(pix_a,pix_s)
            anterior=siguiente            
            print 'detect'
        
        pygame.display.update()
        #anterior=siguiente
        time.sleep(0.02)
        
main()
