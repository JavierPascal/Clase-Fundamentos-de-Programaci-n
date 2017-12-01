#Highscore

def highscore():
    highscores = {}
    with open("highscores.txt", "r") as entrada:
        contenido = entrada.readlines()
        for linea in contenido:  # hacer listas
            a = linea.split(",")
        for i in range(len(a)+1):
            highscores[username] = str(highscore)
    print(highscores)




    username=input("Username:")
    highscore=int(input("Give me highscore"))
    if username in highscores:
        if highscore >= highscores[username]:
            highscores[username] = str(highscore)
    else:
        highscores[username] = str(highscore)
    print (highscores)
    with open("highscores.txt", "w") as text_file:
        text_file.write(username+","+highscores[username])




highscore()