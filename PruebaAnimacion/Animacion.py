# encoding: UTF-8
# Autor:Javier Pascal Flores
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
width = 800
tall = 900
# Colores
white = (255,255,255)  # R,G,B en el rango [0,255]
green = (0, 122, 0)
red = (255, 0, 0)
black = (0,0,0)

num_images = 8
num_coins = 10
time_in_frames = .1
total_time= num_images*time_in_frames


def createSpriteslist():
    lista = []
    for i in range(num_images):
        name = "imagenes/anima-"+ str(i)+".png"
        image = pygame.image.load(name)
        Animation_spr= pygame.sprite.Sprite()
        Animation_spr.image= image
        Animation_spr.rect = image.get_rect()
        Animation_spr.rect.left =  width //2 - Animation_spr.rect.width//2
        Animation_spr.rect.top =450
        lista.append(Animation_spr)
    return lista
def createSpriteslist_2():
    lista = []
    for i in range(num_coins):
        name = "imagenes/coin-"+ str(i)+".png"
        image = pygame.image.load(name)
        Animation_spr= pygame.sprite.Sprite()
        Animation_spr.image= image
        Animation_spr.rect = image.get_rect()
        Animation_spr.rect.left =  width //2 - Animation_spr.rect.width//2 -50
        Animation_spr.rect.top =tall//2- Animation_spr.rect.height//2 -65
        lista.append(Animation_spr)
    return lista


def getFrame(Animation_Timer, Spriteslist):
    index = int(Animation_Timer/time_in_frames)
    return Spriteslist[index]


def draw():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((width, tall))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución

    #Animation of Puma
    Spriteslist = createSpriteslist()
    Animation_Timer = 0

    #fondo

    image_back= pygame.image.load("imagenes/back.png")
    x = 0


    while not termina:
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(white)
        ventana.blit(image_back, (x,0))

        ventana.blit(image_back, (width+x,0))
        x -= 5
        if x <= -width:
            x=0

        # Dibujar, aquí haces todos los trazos que requieras
        current_frame = getFrame(Animation_Timer, Spriteslist)
        ventana.blit(current_frame.image,current_frame.rect)

        pygame.display.flip()   # Actualiza trazos
        Animation_Timer += reloj.tick(40)/1000        # 40 fps
        if Animation_Timer >= total_time:
            Animation_Timer =0
    pygame.quit()   # termina pygame


def main():
    draw()


main()