import fitz  # PyMuPDF
import json

def insertar_imagenes(pdf_entrada, json_config, pdf_salida):
    """
    Inserta imágenes en un PDF según la configuración dada en un JSON.
    
    Args:
        pdf_entrada (str): ruta al PDF original
        json_config (str): ruta al archivo JSON con las tuplas [pagina, bbox, ruta_imagen]
                           - pagina: número de página (empezando en 1)
                           - bbox: [x0, y0, x1, y1] coordenadas en puntos (72 dpi)
                           - ruta_imagen: string con la ruta a la imagen
        pdf_salida (str): ruta al PDF de salida
    """
    # Cargar configuraciones
    with open(json_config, "r", encoding="utf-8") as f:
        configuraciones = json.load(f)

    # Abrir el PDF
    doc = fitz.open(pdf_entrada)

    for pagina, coords, ruta_imagen in configuraciones:
        bbox = [coords[0], coords[1], coords[0]+coords[2], coords[1]+coords[3]]
        page = doc[pagina - 1]  # índice en PyMuPDF empieza en 0
        rect = fitz.Rect(*bbox)  # crear rectángulo de destino
        page.insert_image(rect, filename=ruta_imagen, keep_proportion=False)

    # Guardar nuevo PDF (manteniendo enlaces y bookmarks)
    doc.save(pdf_salida, incremental=False, deflate=True)
    doc.close()


if __name__ == "__main__":
    # Ejemplo de JSON:
    # [
    #   [1, [100, 200, 300, 400], "imagen1.png"],
    #   [2, [50, 50, 150, 150], "imagen2.jpg"]
    # ]
    insertar_imagenes(
        pdf_entrada="maquetado_auto/source.pdf",
        json_config="maquetado_auto/ubis.json",
        pdf_salida="maquetado_auto/source_maquetado.pdf"
    )