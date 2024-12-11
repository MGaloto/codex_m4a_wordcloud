
from dotenv import load_dotenv
import os


load_dotenv(override=True)
WORKING_DIR = os.getenv("WORKING_DIR")

# Carpeta donde se encuentran los archivos .txt
txt_folder = WORKING_DIR

# Nombre del archivo final donde se combinarán las transcripciones
final_txt = "transcripcion_final.txt"

# Abrir el archivo final en modo de escritura
with open(final_txt, "w", encoding="utf-8") as final_file:
    # Iterar sobre todos los archivos en la carpeta
    for filename in os.listdir(txt_folder):
        # Comprobar si el archivo tiene extensión .txt
        if filename.endswith(".txt"):
            file_path = os.path.join(txt_folder, filename)
            # Abrir y leer el archivo
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Escribir el contenido del archivo en el archivo final
                # final_file.write(f"--- Transcripción de {filename} ---\n")
                final_file.write(content)
                final_file.write("\n")
    
print(f"Todas las transcripciones han sido combinadas en {final_txt}")
