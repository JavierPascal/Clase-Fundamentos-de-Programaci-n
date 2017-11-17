#Javier Pascal Flores
#Jose Antonio Vazquez Gavian
#Encoding: UTF-8
from random import randint
def Juego():

        puntos=0
        estados = {'Aguascalientes':'Aguascalientes','Baja California':'Mexicali','Baja California Sur':'La Paz','Campeche':'Campeche','Coahuila':'Saltillo','Colima':'Colima','Chiapas':'Tuxtla Gutiérrez','Chihuahua':'Chihuahua','Distrito Federal':'Ciudad de México','Durango':'Durango','Guanajuato':'Guanajuato','Guerrero':'Chilpancingo','Hidalgo':'Pachuca','Jalisco':'Guadalajara','México':'Toluca','Michoacán':'Morelia','Morelos':'Cuernavaca','Nayarit':'Tepic','Nuevo León':'Monterrey','Oaxaca':'Oaxaca','Puebla':'Puebla','Querétaro':'Querétaro','Quintana Roo':'Chetumal','San Luis Potosí':'San Luis Potosí','Sinaloa':'Culiacán','Sonora':'Hermosillo','Tabasco':'Villahermosa','Tamaulipas':'Ciudad Victoria','Tlaxcala':'Tlaxcala','Veracruz':'Xalapa','Yucatán':'Mérida','Zacatecas':'Zacatecas'}
        lista=list(estados.keys())
        respuestas=list(estados)

        vidas=3
        print("Tienes tres vidas")

        while vidas != 0:
            pregunta=lista[randint(0,32)]
            print("Dime la capital de: ",pregunta)
            respuesta=input()
            if respuesta in estados[pregunta]:
                print("Correcto")
                puntos+=100
                print("vidas = ",vidas)
                print("Puntos = ",puntos)


            else:
                print("Incorrecto")
                puntos-=50
                vidas-=1
                print ("La respuesta Correcta es ",estados[pregunta])
                print("vidas = ",vidas)
                print("Puntos = ",puntos)

        print("Perdiste")


Juego()