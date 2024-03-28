#Codeado un 27/03/2024 a las 10 am wazaaa
#_alexape in discord (soy hombre:v)
import requests
import os
import jsbeautifier
import sys
def verif():
    if os.path.exists("scraping/bundle.js"):
        print("Archivo existe")
    else:   
        print("Creando archivo")
        rq = requests.get("https://htbmachines.github.io/bundle.js")
        texte = rq.text
        res = jsbeautifier.beautify(texte)
        with open("scraping/bundle.js", "w", encoding='utf8') as bundle:
            bundle.write(res)
            print("Archivo generado con exito")

def update(): 
        print("Actualizando archivo!...")
        rq = requests.get("https://htbmachines.github.io/bundle.js")
        texte = rq.text
        res = jsbeautifier.beautify(texte)
        with open("scraping/bundle.js", "w", encoding='utf8') as bundle:
            bundle.write(res)
            return "Archivo actualizado!"
        
def search(p):
        with open("scraping/bundle.js", "r", encoding='utf8') as bundle:
            count=0
            x = bundle.readlines()
            for verif in x:
                count+=1
                if f'name: "{p}"' in verif:
                        return f'\tMAQUINA EXISTE\n{verif}{"".join(x[count:count+10])}'
            else:
                 return "MAQUINA NO EXISTE"
if __name__ == '__main__':

    args = ['-download', '-update', '-search']
    x = sys.argv
    if args[0] in x:
            verif()
    elif args[1] in x:
         print(update())
    elif args[2] in x:
        print(search(x[2]))
    else:
        pantalla="""\n\t LOS ARGUMENTOS DISPONIBLES SON 
        -download : descargar el archivo
        -update   : actualizar el archivo
        -search   : realizar una busqueda
        """
        print(pantalla)