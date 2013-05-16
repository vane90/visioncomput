import pygame, sys
from pygame.locals import *
import time

pygame.init()

ancho_ventana = 400
alto_ventana = 400
ventanaSurface = pygame.display.set_mode((ancho_ventana, alto_ventana), 0, 32)
pygame.display.set_caption('Movimiento')

baja_izq = 1
baja_der = 5
sube_izq = 7
sube_der = 9

mueverect = 4


negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)


b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':rojo, 'dir':sube_der}
b2 = {'rect':pygame.Rect(300, 80, 60, 100), 'color':verde, 'dir':sube_izq}
b3 = {'rect':pygame.Rect(300, 80, 60, 100), 'color':azul, 'dir':baja_izq}
rectans = [b1, b2, b3]
#rectans = [b1]

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    ventanaSurface.fill(negro)

    for b in rectans: #mueve rects
        
        if b['dir'] == baja_izq:
            b['rect'].left -= mueverect
            b['rect'].top += mueverect
        if b['dir'] == baja_der:
            b['rect'].left += mueverect
            b['rect'].top += mueverect
        if b['dir'] == sube_izq:
            b['rect'].left -= mueverect
            b['rect'].top -= mueverect
        if b['dir'] == sube_der:
            b['rect'].left += mueverect
            b['rect'].top -= mueverect

        
        if b['rect'].top < 0: #sube
            
            if b['dir'] == sube_izq:
                b['dir'] = baja_izq
            if b['dir'] == sube_der:
                b['dir'] = baja_der
        if b['rect'].bottom > ancho_ventana:
            # se mueve a lo ancho
            if b['dir'] == baja_izq:
                b['dir'] = sube_izq
            if b['dir'] == baja_der:
                b['dir'] = sube_der
        if b['rect'].left < 0:
            # el bloque se mueve mas a la izq
            if b['dir'] == baja_izq:
                b['dir'] = baja_der
            if b['dir'] == sube_der:
                b['dir'] = sube_der
        if b['rect'].right > alto_ventana:
            # el bloque se mueve mas a la der
            if b['dir'] == baja_der:
                b['dir'] = baja_izq
            if b['dir'] == sube_der:
                b['dir'] = sube_izq


        # draw the block onto the surface
        pygame.draw.rect(ventanaSurface, b['color'], b['rect'])
  pygame.image.save(ventanaSurface,'nuevo.png')
    # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
