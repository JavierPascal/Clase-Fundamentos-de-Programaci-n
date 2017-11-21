#Javier Pascal Flores
import math
import statistics

import matplotlib.pyplot as plot

def archivo(): #Hacer el archivo datosAlumnos
    entrada=open("Alumnos.txt", "r", encoding="UTF-8")#leer datos
    contenido = entrada.readlines()
    contenido.remove(contenido[0])
    entrada.close()
    aprobado=[]
    Matricula_a0=[]
    promedio=[]
    nombres=[]
    for linea in contenido:#hacer listas
        a=linea.split(",")
        Matriculas=a[0].split("A0")
        Matricula_a0.append(Matriculas[1])
        prom=round(((int(a[2])+int(a[3])+int(a[4]))/3),1)
        promedio.append(prom)
        if prom <70:
            aprobado.append("No aprobó")
        else:
            aprobado.append("Aprobó")
        nombres.append(a[1])

    salida = open("datosAlumnos.txt", "w", encoding="UTF-8")
    for i in range(0,len(contenido)-1):
        salida.write(Matricula_a0[i] + ";" + str(promedio[i]) + ";" + aprobado[i] + "\n")#Escribir el archivo
    salida.close()
    return Matricula_a0, promedio, nombres
def grafica(Matricula, promedio):#esta funcion hace la grafica
    valores_x=[]
    valores_y=[]
    for i in range(len(promedio)):
        if float(promedio[i])<70:
            valores_y.append(promedio[i])
            valores_x.append(Matricula[i])
    x=list(range(len(valores_x)))
    plot.plot(x,valores_y)
    plot.xlabel("Matricula")
    plot.ylabel("Promedio")
    plot.xticks(x, valores_x, rotation='vertical')
    plot.show()

def aprobados(promedio, nombres):#Calcula la cantidad de aprobados y la pone en una tabla
    nombre = []
    calif = []
    for i in range(len(promedio)):
        if float(promedio[i]) >=70:
            nombre.append(nombres[i])
            calif.append(promedio[i])
    print("Tabla de Aprobados")
    print("Nombre" + 5*"\t" +"Promedio")
    for t in range(len(nombre)):
        if len(nombre[t]) > 1:
            print(nombre[t] +(25-len(nombre[t]))*"-" + str(calif[t]) + "\n")


def muy_reprobados(promedio, nombres):#Calcula el menor promedio y lo pone en una tabla
    nombre=[]
    calif=[]
    for i in range(len(promedio)):
        if float(promedio[i])==(min(promedio)):
            nombre.append(nombres[i])
            calif.append(promedio[i])
    print("Alumno(s) con menor promedio")
    print("%-20s %s"%("Nombre","Promedio"))
    for t in range(len(nombre)):
        if len(nombre[t]) < 26:
            print(nombre[t] +(25-len(nombre[t]))*"-" + str(calif[t]) + "\n")
def ECOA(): #dice mensaje de ecoa
    print("Ya conteste la ECOA")
def main():
    matricula,promedio, nombres=(archivo())
    aprobados(promedio, nombres)
    muy_reprobados(promedio, nombres)
    ECOA()
    grafica(matricula, promedio)
main()

