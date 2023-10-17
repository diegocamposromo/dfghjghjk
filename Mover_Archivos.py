import os
import shutil

def mover_pdf(origen, destino):
    # Comprobar si el directorio de destino existe
    if not os.path.exists(destino):
        os.makedirs(destino)

    # Obtener la lista de archivos en el directorio de origen
    archivos = os.listdir(origen)

    # Iterar sobre los archivos y mover los que tienen extensión .pdf
    for archivo in archivos:
        if archivo.endswith(".PDF"):
            origen_archivo = os.path.join(origen, archivo)
            destino_archivo = os.path.join(destino, archivo)
            shutil.move(origen_archivo, destino_archivo)
            print(f"Archivo {archivo} movido correctamente.")

# Ruta de la carpeta de origen y destino
origen = "C:/Users/campo/Downloads/proyecto111"
destino = "C:/Users/campo/OneDrive/Escritorio/documentos_archivos"

mover_pdf(origen, destino)