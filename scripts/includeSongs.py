import os

INCLUDE_SONGS_FILENAME = "../tex/writeSongs.tex"

def include_songs_of(path):
    try:
        with open(INCLUDE_SONGS_FILENAME, "w", encoding="utf-8") as f:
            for file in os.listdir(path):
                fullPath = os.path.join(path, file)
                if os.path.isfile(fullPath):
                    f.write(f'\\input{{{fullPath}}}\n')
    except Exception as e:
        print(f"Error: {e}")

include_songs_of('../canciones/')