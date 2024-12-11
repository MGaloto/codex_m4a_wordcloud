from pydub import AudioSegment
import speech_recognition as sr
from dotenv import load_dotenv
import os


load_dotenv(override=True)
WORKING_DIR = os.getenv("WORKING_DIR")

def convert_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="m4a")
    audio.export(output_file, format="wav")
    print(f"Archivo convertido a {output_file}")
    return audio

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print(f"Reconociendo el audio de {audio_file}...")
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio, language="es-ES")  # Cambia 'es-ES' si usas otro idioma
            return text
        except sr.UnknownValueError:
            return "No se pudo entender el audio."
        except sr.RequestError as e:
            return f"Error al conectar con el servicio de reconocimiento de voz: {e}"

input_m4a = WORKING_DIR+"video.m4a"
output_wav = "archivo_convertido.wav"

audio = convert_to_wav(input_m4a, output_wav)

segment_duration = 60000  # Duración de cada segmento en milisegundos (1 minuto)
segments = []

# Dividir el audio en segmentos
for i in range(0, len(audio), segment_duration):
    segment = audio[i:i + segment_duration]
    segment_file = f"segment_{i//segment_duration}.wav"
    segment.export(segment_file, format="wav")
    segments.append(segment_file)

for i, segment_file in enumerate(segments):
    text = transcribe_audio(segment_file)
    output_txt = f"transcripcion_segment_{i+1}.txt"  # Crear nombre único para cada archivo
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    os.remove(segment_file)  # Eliminar el archivo temporal

    print(f"Transcripción del segmento {i+1} guardada en {output_txt}")
