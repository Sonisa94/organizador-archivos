import os
import shutil

#Configuracion de carpeta a organizar y extensiones
folder_to_organize = "/ruta/a/organizar"  #Cambiar según necesidades.
DESTINATIONS = {
    "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx",".xsl", ".csv", ".pptx", ".ppt"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Código": [".py", ".js", ".html", ".css", ".java"],
    "Instalables": [".deb"],
    "Binarios": [".bin"],
    "Logs": [".log"],
    "Otros": []
}

def organizar_archivos():
    for archivo in os.listdir(folder_to_organize):
        ruta_archivo = os.path.join(folder_to_organize, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            for carpeta, extensiones in DESTINATIONS.items():
                if extension in extensiones:
                    carpeta_destino = os.path.join(folder_to_organize, carpeta)
                    if not os.path.exists(carpeta_destino):
                        os.makedirs(carpeta_destino)
                    shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                    print(f"Movido: {archivo} -> {carpeta}")
                    break

if __name__ == "__main__":
    organizar_archivos()
