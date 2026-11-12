from script_Concursantes import obtener_datos, inicio
from script_hash import Corredor_1, Corredor_2, Corredor_3, Corredor_4
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import sys 

def Informacion_1():
    print("/--------------------------------------------/""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/     Informacion importante!                /""\n"
      "/        1- cargar los archivos              /""\n"
      "/                                            /""\n"
      "/   2- Tiene una capacidad de 4 jugadores    /""\n"
      "/                                            /""\n"
      "/    3- El proyecto sigue en fase prueba     /""\n"
      "/                                            /""\n"
      "/                                            /""\n"      
      "/--------------------------------------------/")
    time.sleep(5)

def Informacion_2():
    print("/--------------------------------------------/""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/               !Advertencia                 /""\n"
      "/                                            /""\n"
      "/        El Programa consume Alta RAM        /""\n"
      "/                                            /""\n"
      "/        Puede Caer el Programa o PC         /""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/--------------------------------------------/")


if __name__ == "__main__":
    
    print("/--------------------------------------------/""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/               Bienvenido A                 /""\n"
      "/            GO Hash Go to Goal              /",                                             "(ᓀ‸ᓂ)""\n"
      "/                  By: HK                    /""\n"
      "/                                            /""\n"
      "/                                            /""\n"
      "/--------------------------------------------/")
    
    decision = int(input("Ingresa la opcion \n Salir: 1 | Jugar: 2 \n"))
    if decision == 1:
        sys.exit(0)
        print("Gracias por ejecutar")
    elif decision == 2:
        Informacion_1()
        Informacion_2()














    
    
    print("iniciando...") 
    with ProcessPoolExecutor(max_workers=4) as TPE:
        resultados = obtener_datos()
        listado = resultados.get("Corredor 1")
        listado_2 = resultados.get("Corredor 2")
        listado_3 = resultados.get("Corredor 3")
        listado_4 = resultados.get("Corredor 4")

        tareas = {
        TPE.submit(Corredor_1, listado): "Concursante 1",
        TPE.submit(Corredor_2, listado_2): "Concursante 2",
        TPE.submit(Corredor_3, listado_3): "Concursante 3",
        TPE.submit(Corredor_4, listado_4): "Concursante 4"
        }

        final2 = {}

        for Concursantes in as_completed(tareas):
            datos = Concursantes.result()
            nombre = tareas[Concursantes]
        
    
    
    fin = time.time()
    final = fin - inicio
    print(final)
    print("finalizo...")



