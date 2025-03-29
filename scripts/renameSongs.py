import os
import sys
import re

def rename_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
        
        match = re.match(r"\\beginsong\{(.+?)\}\[.*\]", first_line)
        if not match:
            print(f"No se encontró un título en {file_path}")
            return
        
        title = match.group(1).replace(" ", "_")  # Reemplazar espacios por guiones bajos
        dir_name, old_filename = os.path.split(file_path)
        new_filename = f"{os.path.splitext(old_filename)[0]}_{title}.tex"
        new_file_path = os.path.join(dir_name, new_filename)
        
        os.rename(file_path, new_file_path)
        print(f"Renombrado: {file_path} -> {new_file_path}")
    except Exception as e:
        print(f"Error renombrando {file_path}: {e}")

if __name__ == "__main__":
    root_dir = "canciones"
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".tex"):
                file_path = os.path.join(dirpath, filename)
                rename_file(file_path)
