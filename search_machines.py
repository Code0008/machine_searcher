
import requests
import os
import jsbeautifier


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
        try:
            with open("scraping/bundle.js", "r", encoding='utf8') as bundle:
                count=0
                x = bundle.readlines()
                for verif in x:
                    count+=1
                    if f'name: "{p}"' in verif:
                            return f'\tMAQUINA EXISTE\n{verif}{"".join(x[count:count+10])}'
                else:
                    return "MAQUINA NO EXISTE"
        except Exception as e:
            return f"ocurrio el error ->>> {e}"


    
if __name__ == "__main__":
    print(search("Tentacle"))
    
