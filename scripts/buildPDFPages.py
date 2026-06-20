import os
from pypdf import PdfWriter
from natsort import natsorted

merger = PdfWriter()

# Cambia esto a la carpeta que contiene tus PDFs
dirorigen = "./maquetado/unirFinal"
dirdestino = "./maquetado/"

# Obtener y ordenar los archivos PDF alfabéticamente
pdfs = natsorted([f for f in os.listdir(dirorigen) if f.endswith(".pdf")])

if len(pdfs)==0:
    print("No hay pdfs")
else:
    for pdf in pdfs:
        merger.append(os.path.join(dirorigen, pdf))

    # Guardar el archivo combinado
    merger.write(os.path.join(dirdestino, "final.pdf"))
    merger.close()
