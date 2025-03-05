import os

INCLUDE_SONGS_FILENAME = "./tex/songslist.tex"

def include_songs_of(path):
    try:
        with open(INCLUDE_SONGS_FILENAME, "w", encoding="utf-8") as f:
            # Obtener la lista de archivos y ordenarla alfabéticamente
            files = sorted(os.listdir(path))
            for file in files:
                fullPath = os.path.join(path, file)
                if os.path.isfile(fullPath):
                    f.write(f'\\input{{{fullPath}}}\n')
    except Exception as e:
        print(f"Error: {e}")

include_songs_of('./canciones/')