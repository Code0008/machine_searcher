
import search_machines as sm
import argparse
def argumens():
    Parser = argparse.ArgumentParser(description="""\n\t LOS ARGUMENTOS DISPONIBLES SON 
        -download : descargar el archivo
        -update   : actualizar el archivo
        -search   : realizar una busqueda
        """)
    Parser.add_argument("-d", "--download", dest="verif_download", help="Instalar archivo bundle.js")
    Parser.add_argument("-u", "--update", dest="verif_actual", help="Si ya tiene el archivo bundle.js lo actualiza $ -u/--update yes ")
    Parser.add_argument("-s", "--search", dest="buscar", help="Realizar busqueda de la maquina $")
    opciones = Parser.parse_args()
    return opciones.verif_download, opciones.verif_actual, opciones.buscar
    
argumentos = argumens()
if argumentos[1]:
    print(sm.update())
if argumentos[2]:
    print(sm.search(argumentos[2]))
if argumentos[0]:
    sm.verif()
    
