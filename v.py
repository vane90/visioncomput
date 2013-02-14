#import sys,pygame
import sys, pygame
import Image
from math import*
from time import*
import math
import random


def main():  
    pygame.init() # Inicializa pygame 
    screen = pygame.display.set_mode((600, 600)) 
    pygame.display.set_caption('Ruido') 
    imagen = gruido()
    i_fuera = fueraruido(imagen)
    img = pygame.image.load(imagen) 
    screen = pygame.display.get_surface() 

    while True: # Ciclo para las acciones en la ventana

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(img, (0,0)) # muestra la posicion de la imagen en x = 0 y y=0
        pygame.display.update()


def gruido():
    #tarda = time()
    image = Image.open("dory.jpg")
    imagen = image.load()
    ancho, alto = image.size
    #intenso = 200
    #cont = 0
    for i in range(ancho):
        for j in range(alto):
            (r,g,b)= image.getpixel((i,j)) #obtener pixeles 
            sp = random.randint(0,255) #generar ruido random llenado de toda la imagen
            punto = random.randint(0,6000) # 
            try:
                if (sp < 100): #ciclo compara la intensidad del ruido dentro de imagen
                    imagen[i+punto,j+punto] = (0,0,0) # Agregamos el ruido en color negro simulando la pimienta 
                else:
                    imagen[i+punto,j+punto] = (255,255,255) #agregamos el ruido de color blanco simulando la sal
            except:
                pass
            
            nueva = 'ruido.jpg'
    otra = image.save(nueva)
    #t1 = time()
    #t2 = t1 - tarda
    #print "Tiempo que tardo el procesamiento = "+str(t2)+" segundos"
    return nueva


def fueraruido(imagen):
    #imagen = 'ruido.jpg'
    imagen=Image.open(imagen)
    ima = imagen.load()    
    ancho, alto = imagen.size
    for i in range(ancho):  
         for j in range(alto):
             (r,g,b) = imagen.getpixel((i,j))
               
             try:
                if(pixel[i,j]==(0,0,0) or pixel[i,j]==(255,255,255)):
              
                    pixel[i,j] = pixel[i-1,j]
               
                else:
                    continue
             except:
                 pass
    
    nueva2 = 'elimina.jpg'
    i_fuera = imagen.save(nueva2)
    #tiempo2 = time.time()
    #print "Tiempo de procesamiento filtro"
    return nueva2
     
if __name__ == "__main__":
    main()
