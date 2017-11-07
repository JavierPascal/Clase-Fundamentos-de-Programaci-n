#Javier Pascal Flores
#Encoding: UTF-8

from gtts import gTTS
import os
def traducirEspanol():

    traductor={}
    traductor["Hola"]="Hello"
    traductor["Fresa"]="Strawberry"
    traductor["Cartera"]="Wallet"
    traductor["Celular"]="Cell-Phone"
    traductor["Espinaca"]="Spinach"
    traductor["Mundo"]="World"
    traductor["Casa"]="House"
    traductor["Papaya"]="Papaya"
    traductor["Canica"]="Marble"
    palabra=input("Teclea tu palabra en español: ")
    if palabra in traductor:
        print("En español:", traductor[palabra])

        tts = gTTS(traductor[palabra],"en")
        tts.save("good.mp3")
        os.system("start good.mp3")
    else:
        print("Esta palabra no esta en el diccionario")
def menu():
    print("En que modelo quieres traducir? \n1 = Traducir Inglés-Español")
    print("2 = Traducir Español-Ingles")
    print("0 = Salir")
    respuesta = int(input("Dame tu opcion: "))
    return respuesta

def main():
    print("Bienvenido al traductor español-inglés ")
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            traducirIngles()
        elif opcion==2:
            traducirEspanol()
        opcion=menu()
main()