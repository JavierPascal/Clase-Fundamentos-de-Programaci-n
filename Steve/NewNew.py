# encoding: UTF-8
# Javier Pascal Flores

import pygame
from random import randint

# Dimensiones de la pantalla
ancho = 800
alto = 600
# Colores
blanco = (255, 255, 255)  # R,G,B en el rango [0,255]
verde_bandera = (0, 122, 0)
rojo = (255, 0, 0)
negro = (0, 0, 0)


def drawMenu(ventana, playButton, Logo, high):
    ventana.blit(playButton.image, playButton.rect)
    ventana.blit(Logo.image, Logo.rect)
    ventana.blit(high.image, high.rect)



def drawGame(ventana, enemiesList, bulletList):
    for enemy in enemiesList:
        ventana.blit(enemy.image, enemy.rect)
    for bullet in bulletList:
        ventana.blit(bullet.image, bullet.rect)


def refreshBullets(bulletlist, enemiesList,puntos):

    for bullet in bulletlist:  # DO NOT MODIFY CONNECTION
        bullet.rect.top -= 15
        if bullet.rect.top < -15:
            bulletlist.remove(bullet)
            continue
        delBullet = False
        for k in range(len(enemiesList) - 1, -1, -1):
            enemy = enemiesList[k]
            if bullet.rect.colliderect(enemy):
                enemiesList.remove(enemy)
                delBullet = True
                puntos+=50
                break
        if delBullet == True:
            bulletlist.remove(bullet)
    return puntos
def refreshEnemies(enemiesList):
    for enemy in enemiesList:  # DO NOT MODIFY CONNECTION
        enemy.rect.top += 2




def spawnEnemies(enemiesList, imgEnemy):
    for x in range(5):
        for y in range(2):
            # X,Y coordenates
            cx = 50 + x * 150
            cy = 50 + y * 150
            enemy = pygame.sprite.Sprite()
            enemy.image = imgEnemy
            enemy.rect = imgEnemy.get_rect()
            enemy.rect.left = cx - enemy.rect.width // 2
            enemy.rect.top = cy - enemy.rect.height // 2
            enemiesList.append(enemy)




def randomEnemies(enemiesList, imgEnemy, imgEnemy_69,img_Comet):
    enemy = pygame.sprite.Sprite()
    enemy.image = imgEnemy
    enemy.rect = imgEnemy.get_rect()
    cx = randint(10, ancho - enemy.rect.width)
    cy = -enemy.rect.height
    enemy.rect.left = cx
    enemy.rect.top =cy
    fail = pygame.sprite.Sprite()
    fail.image = imgEnemy_69
    fail.rect = imgEnemy_69.get_rect()
    fail.rect.left = randint(10, ancho - fail.rect.width)
    fail.rect.top = -fail.rect.height
    comet = pygame.sprite.Sprite()
    comet.image = img_Comet
    comet.rect = img_Comet.get_rect()
    comet.rect.left = randint(10, ancho - comet.rect.width)
    comet.rect.top = -comet.rect.height


    enemiesList.append(enemy)
    enemiesList.append((fail))
    enemiesList.append((comet))


def drawHighscores(ventana, Logo):
    ventana.blit(Logo.image, Logo.rect)


def dibujar():
    # Ejemplo del uso de pygame
    pygame.init()  # Inicializa pygame
    ventana = pygame.display.set_mode((ancho, alto))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución
    state = "menu"  # playing, end

    # Load images
    imgButPlay = pygame.image.load("Images/button_jugar.png")
    # Sprite
    playButton = pygame.sprite.Sprite()
    playButton.image = imgButPlay
    playButton.rect = imgButPlay.get_rect()
    playButton.rect.left = ancho // 2 - playButton.rect.width // 2
    playButton.rect.top = alto // 2 - playButton.rect.height // 2
    # Load images
    imgLogo = pygame.image.load("Images/Logo.png")
    # Sprite
    Logo = pygame.sprite.Sprite()
    Logo.image = imgLogo
    Logo.rect = imgLogo.get_rect()
    Logo.rect.left = ancho // 2 - Logo.rect.width // 2
    Logo.rect.top = playButton.rect.top - 200
    #Loadd Images
    imgButHigh = pygame.image.load("Images/button_highscores.png")
    # Sprite
    highButton = pygame.sprite.Sprite()
    highButton.image = imgButHigh
    highButton.rect = imgButHigh.get_rect()
    highButton.rect.left = (ancho // 2 - highButton.rect.width // 2)
    highButton.rect.top = (alto // 2 - highButton.rect.height // 2)+150


    #Fondo de Menu
    imgSpace = pygame.image.load("images/Back/Space.png")



    #Imagen Fondo
    image_back = pygame.image.load("images/Back/FondoSpace.png")
    y = 0
    #
    enemiesList = []
    imgEnemy = pygame.image.load("Images/DA.png")
    imgEnemy_69=pygame.image.load("Images/69.png")
    img_Comet = pygame.image.load("Images/Comet.png")

    spawnEnemies(enemiesList, imgEnemy)

    # Balas
    bulletList = []
    imgBullet = pygame.image.load("Images/Bogo/Bogo-0.png")

    timer = 0
    puntos = 0

    # Music


    while not termina:
        # Procesa los eventos que recibe
        xm, ym = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Mouse Clicked

                if state == "menu":
                    xb, yb, anchoB, altoB = playButton.rect
                    xh, yh, anchoH, altoH = highButton.rect
                    if xm >= xb and xm <= xb + anchoB:
                        if ym >= yb and ym <= yb + altoB:
                            state = "jugando"
                            # Switch Window
                    elif xm >= xh and xm <= xh + anchoH:
                        if ym >= yh and ym <= yh + altoH:
                            state = "highscore"
                elif state == "jugando":
                    enemy = pygame.sprite.Sprite()
                    enemy.image = imgEnemy
                    enemy.rect = imgEnemy.get_rect()
                    enemy.rect.left = xm - enemy.rect.width // 2
                    enemy.rect.top = ym - enemy.rect.height // 2
                    enemiesList.append(enemy)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    bullet = pygame.sprite.Sprite()
                    bullet.image = imgBullet
                    bullet.rect = imgBullet.get_rect()
                    bullet.rect.left = xm
                    bullet.rect.top = alto + bullet.rect.height
                    bulletList.append(bullet)

        # Borrar pantalla

        ventana.fill(negro)


        # Enemies every 2 sec

        timer += 1 / 40
        if timer >= 2:
            timer = 0
            randomEnemies(enemiesList, imgEnemy, imgEnemy_69, img_Comet)

        # Dibujar, aquí haces todos los trazos que requieras
        if state == "menu":
            ventana.blit(imgSpace, (0, 0))
            drawMenu(ventana, playButton,Logo,highButton)
        elif state == "highscore":
            ventana.fill(negro)
            drawHighscores(ventana, Logo)

        elif state == "jugando":
            ventana.blit(image_back, (0, y))

            ventana.blit(image_back, (0, y))
            y -= 9
            if y <= -10000:
                y = 0
            refreshBullets(bulletList, enemiesList,0)
            refreshEnemies(enemiesList)
            drawGame(ventana, enemiesList, bulletList)
            puntos = refreshBullets(bulletList, enemiesList,0)
            font = pygame.font.SysFont("monospace", 18)
            text = font.render("Puntos:" + str(round(puntos, 3)), 1, blanco)
            ventana.blit(text, (10, 10))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


def main():
    dibujar()

main()
