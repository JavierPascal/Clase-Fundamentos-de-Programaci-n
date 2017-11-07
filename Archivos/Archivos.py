#Javier Pascal
#Encoding: UTF-8
def pedir_archivo():
    archivo=open(input("Nombre: "), "r", encoding="UTF-8")
    numero=1
    for linea in archivo:
        print(numero,linea.rstrip())
        numero+=1
    archivo.close()
pedir_archivo()