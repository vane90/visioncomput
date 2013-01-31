import pygame, sys, os
from pygame.locals import *
from sys import argv
import Image

def pixel():
	 ima= argv[1]
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

	pygame.init()
	screen = pygame.display.set_mode((500, 300))
	pygame.display.set_caption('Escala de Grises')
	imagen=pixel()
	img = pygame.image.load(imagen)
	screen = pygame.display.get_surface()

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			screen.blit(img, (0,0))	
			pygame.display.update()

if __name__ == "__main__":
	main()
