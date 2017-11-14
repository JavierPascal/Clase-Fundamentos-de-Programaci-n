#Javier Pascal
#Encoding: UTF-8
import matplotlib.pyplot as plot
"""def pedir_archivo():
    archivo=open(input("Nombre: "), "r", encoding="UTF-8")
    numero=1
    for linea in archivo:
        print(numero,linea.rstrip())
        numero+=1
    archivo.close()"""

def diccionarioQuijote():
    dLetras = {}
    entrada= open("quijote.txt", "r", encoding="UTF-8")
    contenido = entrada.read().lower()
    entrada.close()

    for character in contenido: #Visits each string character
        if character.isalpha():
            if character in dLetras:
                dLetras[character] += 1
            else:
                dLetras[character] = 1
    print (dLetras)

    listaLetras =[]
    listaFrecuencias =[]
    for t in dLetras.items():
        listaLetras.append(t[0])
        listaFrecuencias.append(t[1])
    x=list(range(len(listaLetras)))
    plot.plot(x,listaFrecuencias)
    plot.xlabel("Letras")
    plot.ylabel("Frecuencia")
    plot.xticks(x,listaLetras,)
    plot.show()

    #Tabla en un archivo
    salida = open("frecuencias.txt", "w", encoding="UTF-8")
    salida.write("Letra\tFrecuencia\n")
    for t in dLetras.items():
        salida.write( t[0]+ "\t" + "="+ "\t" + str(t[1]) + "\n")
    salida.close()

def main():
    diccionarioQuijote()


    #pedir_archivo()
main()