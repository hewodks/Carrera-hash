from script_Concursantes import obtener_datos
import hashlib
from concurrent.futures import ProcessPoolExecutor
import time


"""En este archivo se importara la lista que contienen el texto de archivo_aleatorio aqui se busca leer esa lista 
combertirla a hash escribiendolo en el archivo y volviendo leer para luego la comparacion||"""

hash_C1 = "n"#input("Ingresa la primer clave del corredor 1 : ")
HashC1 = hashlib.sha256(hash_C1.encode("utf-8")).hexdigest()

def Corredor_1(listado):
    AS1 = listado
    contador = 0

    with open("Archivo_Hash1.txt", "w") as WAS1:
        
        for Linea in AS1:    
            for letra in Linea:
                Hash_letra = hashlib.sha256(letra.encode("utf-8")).hexdigest()
                WAS1.write(str(Hash_letra) + "\n")
               

    """Comparacion"""

    with open("Archivo_Hash1.txt", "r") as RAS1:
        for letra in RAS1:
            contenido = letra.strip()
            if contenido == HashC1:
                print(f"Concursante 1: si esta {contenido}")
    

def Corredor_2(listado_2):
    AS2 = listado_2

    with open("Archivo_Hash2.txt", "w") as WAS2:
        for linea in AS2:
            for letra in linea:
                Hash_Letra = hashlib.sha256(letra.encode("utf-8")).hexdigest()
                WAS2.write(Hash_Letra + "\n")
    
    with open("Archivo_Hash2.txt", "r") as RAS2:
        for linea in RAS2:
            contenido = linea.strip()
            if contenido == HashC1:
                print(f"Concursante 2: si esta {contenido}")

def Corredor_3(listado_3):
    AS3 = listado_3

    with open("Archivo_Hash3.txt", "w") as WAS3:
        for linea in AS3:
            for letra in linea:
                Hash_Letra = hashlib.sha256(letra.encode("utf-8")).hexdigest()
                WAS3.write(Hash_Letra + "\n")

    with open("Archivo_Hash3.txt", "r") as RAS3:
        for linea in RAS3:
            contenido = linea.strip()
            if contenido == HashC1:
                print(f"Concursante 3: si esta {contenido}")

def Corredor_4(listado_4):
    AS4 = listado_4

    with open("Archivo_Hash4.txt", "w") as WAS4:
        for linea in AS4:
            for letra in linea:
                Hash_Letra = hashlib.sha256(letra.encode("utf-8")).hexdigest()
                WAS4.write(Hash_Letra + "\n")

    with open("Archivo_Hash4.txt", "r") as RAS4:
        for linea in RAS4:
            contenido = linea.strip()
            if contenido == HashC1:
                print(f"Concursante 4: si esta {contenido}")


