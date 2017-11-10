# encoding: UTF-8
#Javier Pascal Flores

import pygame

# Dimensiones de la pantalla
ancho = 800
alto = 800
# Colores
blanco = (255,255,255)  # R,G,B en el rango [0,255]
verde_bandera = (0, 122, 0)
rojo = (255, 0, 0)
negro=(0,0,0)


def drawMenu(ventana, playButton):
    ventana.blit(playButton.image, playButton.rect)


def drawGame(ventana, enemiesList, bulletList):
    for enemy in enemiesList:
        ventana.blit(enemy.image, enemy.rect)
    for bullet in bulletList:
        ventana.blit(bullet.image, bullet.rect)

def actualizarBalas(bulletlist, enemiesList):
    for bullet in bulletlist: #BO NOT MODIFY CONNECTION
        bullet.rect.top -= 15
        for k in range(len(enemiesList)-1,-1,-1):
            enemy= enemiesList[k]
            if bullet.rect.colliderect(enemy):
                enemiesList.remove(enemy)

def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()   # Inicializa pygame
    ventana = pygame.display.set_mode((ancho, alto))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock() # Para limitar los fps
    termina = False # Bandera para saber si termina la ejecución
    state="menu" #playing, end

    #Load images
    imgButPlay = pygame.image.load("button_jugar.png")
    #Sprite
    playButton = pygame.sprite.Sprite()
    playButton.image = imgButPlay
    playButton.rect = imgButPlay.get_rect()
    playButton.rect.left = ancho//2 - playButton.rect.width//2
    playButton.rect.top = alto//2 - playButton.rect.height//2

    #Enemies
    enemiesList=[]
    imgEnemy = pygame.image.load("ALien.png")

    #Balas
    bulletList=[]
    imgBullet = pygame.image.load("Bullet.png")


    while not termina:
        # Procesa los eventos que recibe
        xm, ym = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN: #Mouse Clicked

                if state == "menu":
                    xb, yb, anchoB, altoB =playButton.rect
                    if xm>=xb and xm<=xb+anchoB:
                        if ym>=yb and ym<=yb + altoB:
                            #Switch Window
                            state = "jugando"
                elif state == "jugando":
                    enemy = pygame.sprite.Sprite()
                    enemy.image = imgEnemy
                    enemy.rect = imgEnemy.get_rect()
                    enemy.rect.left = xm - enemy.rect.width//2
                    enemy.rect.top = ym - enemy.rect.height//2
                    enemiesList.append(enemy)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bullet = pygame.sprite.Sprite()
                    bullet.image =imgBullet
                    bullet.rect = imgBullet.get_rect()
                    bullet.rect.left = xm
                    bullet.rect.top = alto - bullet.rect.height
                    bulletList.append(bullet)


        # Borrar pantalla
        ventana.fill(negro)

        # Dibujar, aquí haces todos los trazos que requieras
        if state == "menu":
            drawMenu(ventana, playButton)
        elif state == "jugando":
            actualizarBalas(bulletList, enemiesList)
            drawGame(ventana, enemiesList, bulletList)



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()