from concurrent.futures import ProcessPoolExecutor, as_completed
import time

"""Aqui contiene las listas de los corredores es importente ya tenerle listos los arquivos de lextura (archivo_aleatorio_1.txt) 
cada corredor contendra lo siguiente"""

def Corredor_1():
    #se crea un listado que sera usado en el  siguiente archivo importante script_hash.py 
    #importante para el guardado de contraseñas o palabras y convertirlo a hash
    listado = []

    #Modo abierto del archivo para lectura 
    with open("archivo_aleatorio_1.txt", "r") as i:

        #se hace un limpiado de saltos inesesarios 
        for linea in i:
            contenido = linea.strip()
            #agregarlo a la lista
            listado.append(contenido)
    
    #regreso para compartir con el otro archivo
    return listado




def Corredor_2():
     listado_2 = []
     with open("archivo_aleatorio_2.txt", "r") as i:
         for linea in i:
             contenido_2 = linea.strip()
             listado_2.append(contenido_2)
    
     return listado_2



def Corredor_3():
     listado_3=[]
     with open("archivo_aleatorio_3.txt", "r") as i:

         for linea in i:
             contenido = linea.strip()
             listado_3.append(contenido)

     return listado_3

                

def Corredor_4():
    
    listado_4 = []
    with open("archivo_aleatorio_4.txt", "r") as i:
        
        for linea in i:
            contenido = linea.strip()
            listado_4.append(contenido)

    return listado_4


inicio = time.time() 
def obtener_datos():
  
    with ProcessPoolExecutor(max_workers = 4) as TPE:
       
        Tareas = {TPE.submit(Corredor_1): "Corredor 1",
        TPE.submit(Corredor_2): "Corredor 2",
        TPE.submit(Corredor_3): "Corredor 3",
        TPE.submit(Corredor_4): "Corredor 4"}

        final = {}
        contador = 1
        for Proceso in as_completed(Tareas):
            datos = Proceso.result()
            nombre = Tareas[Proceso] 
            final[nombre] = datos
            #print(nombre)
            #print(datos)
            #print(final)
        return final





if __name__ == "__main__":
    #obtener_datos()
    #print(nombre)
    pass
    """prueba para funcionamiento de este archivo"""
    #lol = obtener_datos()
    #print(lol)