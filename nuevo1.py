import pygame, sys, os # Importe pygame para la creacion de la ventana
#from pygame.locals import * 
from sys import argv # Importe para tabajar con argumentos
import Image #Importe para trabajar con Image (PIL)

#Convierte la imagen en escala de grises
def pixel():
    ima = argv[1] 
    im = Image.open(ima)  
    imagen=im.load()  
    ancho, alto = im.size 
    for i in range(ancho): 
        for j in range(alto):
            (r,g,b)= im.getpixel((i,j))
            pix = (r + g + b)/3
            imagen[i,j]=(pix, pix, pix)
    nueva= 'nueva.png'
    im.save(nueva)

    return nueva

def main():

    pygame.init() # Inicializa pygame
    screen = pygame.display.set_mode((380, 300)) #Crea la ventana con las dimensiones de la imagen
    pygame.display.set_caption('Escala de Grises') #Se define el nombre de la ventana
    imagen = pixel() # La imagen toma los nuevos valores
    img = pygame.image.load(imagen) # Carga nuestra imagen
    screen = pygame.display.get_surface() # Se utiliza para mostrar la imagen en la ventana

    while True: # Ciclo para las acciones en la ventana

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.blit(img, (0,0)) # muestra la posicion de la imagen en x = 0 y y=0
        pygame.display.update()

if __name__ == "__main__":
    main()

