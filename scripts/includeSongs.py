import os
from natsort import natsorted


GENERAL_SONGS_FILENAME = "./tex/songslist.tex"
ACLAMACIONES_SONGS_FILENAME = "./tex/worshiplist.tex"

GENERAL_SONGS_SUBFOLDER = "general"
MISA_SONGS_SUBFOLDER = "misa"
ACLAMACIONES_SONGS_SUBFOLDER = "aclamaciones"

def include_songs_of(path):
    pathgeneral = f"{path}/{GENERAL_SONGS_SUBFOLDER}"
    pathmisa = f"{path}/{MISA_SONGS_SUBFOLDER}"
    pathaclamaciones = f"{path}/{ACLAMACIONES_SONGS_SUBFOLDER}"
    try:
        with open(GENERAL_SONGS_FILENAME, "w", encoding="utf-8") as f:
            # Obtener la lista de archivos y ordenarla alfabéticamente
            files = natsorted(os.listdir(pathgeneral), key=str.lower)
            for file in files:
                fullPath = os.path.join(f"{pathgeneral}/", file)
                if os.path.isfile(fullPath):
                    f.write(f'\\input{{{fullPath}}}\n')
                    
        with open(GENERAL_SONGS_FILENAME, "a", encoding="utf-8") as f:
            # Obtener la lista de archivos y ordenarla alfabéticamente
            files = natsorted(os.listdir(pathmisa), key=str.lower)
            for file in files:
                fullPath = os.path.join(f"{pathmisa}/", file)
                if os.path.isfile(fullPath):
                    f.write(f'\\input{{{fullPath}}}\n')
                    
        with open(ACLAMACIONES_SONGS_FILENAME, "w", encoding="utf-8") as f:
            # Obtener la lista de archivos y ordenarla alfabéticamente
            files = natsorted(os.listdir(pathaclamaciones), key=str.lower)
            for file in files:
                fullPath = os.path.join(f"{pathaclamaciones}/", file)
                if os.path.isfile(fullPath):
                    f.write(f'\\input{{{fullPath}}}\n')
    except Exception as e:
        print(f"Error: {e}")

include_songs_of('./canciones/')