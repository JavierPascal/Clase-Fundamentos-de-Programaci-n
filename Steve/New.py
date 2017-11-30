# encoding: UTF-8
# Autor:Javier Pascal Flores
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
width = 1280
tall = 720
# Colores
white = (255,255,255)  # R,G,B en el rango [0,255]
green = (0, 122, 0)
red = (255, 0, 0)
black = (0,0,0)

num_images = 3
num_coins = 10
time_in_frames = .1
total_time= num_images*time_in_frames


def drawMenu(ventana, playButton):
    ventana.blit(playButton.image, playButton.rect)



def createSpriteslist():
    lista = []
    for i in range(num_images):
        name = "Images/Bogo/Bogo-"+str(i)+".png"
        image = pygame.image.load(name)
        Animation_spr= pygame.sprite.Sprite()
        Animation_spr.image= image
        Animation_spr.rect = image.get_rect()
        Animation_spr.rect.left =  width //2 - Animation_spr.rect.width//2
        Animation_spr.rect.top =650-137
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
    state = "menu"
    # Image Button
    imgButPlay = pygame.image.load("images/button_jugar.png")
    # Sprite it
    playButton = pygame.sprite.Sprite()
    playButton.image = imgButPlay
    playButton.rect = imgButPlay.get_rect()
    playButton.rect.left = width // 2 - playButton.rect.width // 2
    playButton.rect.top = tall // 2 - playButton.rect.height // 2
    #Animation of Puma
    Spriteslist = createSpriteslist()
    Animation_Timer = 0

    #fondo

    image_back= pygame.image.load("images/Back/01.png")
    x = 0
    #Puntos
    points=0


    while not termina:
        # Procesa los eventos que recibe
        xm, ym = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if state == "menu":
                    xb, yb, anchoB, altoB =playButton.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb + altoB:
                            #Switch Window
                            state = "jugando"
        # Borrar pantalla
        ventana.fill(black)


                    # Dibujar, aquí haces todos los trazos que requieras

        image = pygame.image.load("Images/Bogo/Bogo-0.png")
        Animation_spr = pygame.sprite.Sprite()
        Animation_spr.image = image
        Animation_spr.rect = image.get_rect()
        Animation_spr.rect.left = width // 2 - Animation_spr.rect.width // 2
        Animation_spr.rect.top = 650 - 137
        #current_frame = getFrame(Animation_Timer, Spriteslist)


        if state == "menu":
            drawMenu(ventana, playButton)
        elif state == "jugando":
            ventana.blit(image_back, (+x, 0))

            ventana.blit(image_back, (width + x, 0))
            x -= 9
            if x <= -12748:
                x = 0

            current_frame = getFrame(Animation_Timer, Spriteslist)
            ventana.blit(current_frame.image, current_frame.rect)
            current_frame.rect.top +=9.81//2
            pygame.draw.rect(ventana, (white),(0, (650-137), 1280, 1))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_frame = getFrame(Animation_Timer, Spriteslist)
                current_frame.rect.top -=10
                ventana.blit(current_frame.image, current_frame.rect)
                if current_frame.rect.top ==650-137:
                    current_frame.rect.top-=9.81//2




            pygame.display.flip()   # Actualiza trazos
            Animation_Timer += reloj.tick(40)/1000        # 40 fps
            if Animation_Timer >= total_time:
                Animation_Timer =0
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()   # termina pygame


def main():
    draw()


main()