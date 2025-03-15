from typing import Union
from fastapi import FastAPI, File, UploadFile
import whisper
import tempfile
import os

#from dotenv import dotenv_values
#config = dotenv_values(".env")
model = whisper.load_model("small")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/audio_aTexto")
async def prueba(upload_file: UploadFile = File):
    return {"resp": audio_a_text(upload_file.read())}

@app.post("/upload_file/")
async def create_upload_file(upload_file: UploadFile = File(...)):
    res = await upload_file.read()
    if not res:
        return {"message": "No upload file sent"}
    # Guardar el archivo en un temporal para Whisper
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(res)
        temp_audio_path = temp_audio.name
    try:
        response = audio_a_text(temp_audio_path)
    finally:
        os.remove(temp_audio_path)  # Limpiar archivo temporal
    return {"filename": upload_file.filename, "size": len(res), "respuesta": response}


def audio_a_text(audio_file_path):
    # Cargar un archivo de audio y extraer 30 seg
    audio = whisper.load_audio(audio_file_path)
    audio = whisper.pad_or_trim(audio)

    # Crear espectrograma
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detectar idioma
    _, probs = model.detect_language(mel)
    idioma = max(probs, key=probs.get)
    print(f"Idioma detectado: {idioma}")

    # Decodificar audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Imprimir el texto reconocido
    print(result.text)
    return {"idioma": idioma, "transcripcion": result.text}