# encoding: UTF-8
#Javier Pascal Flores

import pygame
from random import randint
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

def refreshBullets(bulletlist, enemiesList):
    for bullet in bulletlist: #DO NOT MODIFY CONNECTION
        bullet.rect.top -= 15
        if bullet.rect.top < -15:
            bulletlist.remove(bullet)
            continue
        delBullet= False
        for k in range(len(enemiesList)-1,-1,-1):
            enemy= enemiesList[k]
            if bullet.rect.colliderect(enemy):
                enemiesList.remove(enemy)
                delBullet= True
                break
        if delBullet == True:
            bulletlist.remove(bullet)


def spawnEnemies(enemiesList, imgEnemy):
    for x in range(5):
        for y in range(4):
            #X,Y coordenates
            cx = 50  + x*150
            cy = 50 + y*150
            enemy = pygame.sprite.Sprite()
            enemy.image = imgEnemy
            enemy.rect = imgEnemy.get_rect()
            enemy.rect.left = cx - enemy.rect.width//2
            enemy.rect.top = cy - enemy.rect.height//2
            enemiesList.append(enemy)
    for enemy in enemiesList:
        enemy.rect.top -= 15



def randomEnemies(enemiesList, imgEnemy):

    enemy = pygame.sprite.Sprite()
    enemy.image = imgEnemy
    enemy.rect = imgEnemy.get_rect()
    cx = randint(10, ancho-enemy.rect.width)
    cy = randint(10, alto-enemy.rect.top)
    enemy.rect.left = cx
    enemy.rect.top = cy
    enemiesList.append(enemy)

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
    spawnEnemies(enemiesList, imgEnemy)

    #Balas
    bulletList=[]
    imgBullet = pygame.image.load("Bullet.png")

    timer = 0
    puntos = 0

    #Music


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
                    bullet.rect.top = alto + bullet.rect.height
                    bulletList.append(bullet)


        # Borrar pantalla
        ventana.fill(negro)
        puntos+=.2
        font = pygame.font.SysFont("monospace", 18)
        text = font.render("Puntos:" + str(round(puntos,3)), 1, blanco)
        ventana.blit(text, (10, 10))

        #Enemies every 2 sec

        timer += 1/40
        if timer >=2:
            timer = 0
            randomEnemies(enemiesList, imgEnemy)


        # Dibujar, aquí haces todos los trazos que requieras
        if state == "menu":
            drawMenu(ventana, playButton)
        elif state == "jugando":

            refreshBullets(bulletList, enemiesList)
            drawGame(ventana, enemiesList, bulletList)



        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    dibujar()


main()