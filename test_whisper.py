import whisper
model = whisper.load_model("medium")

# cargar un archivo de audio y extraer 30 seg
audio = whisper.load_audio("test.mp3")
audio = whisper.pad_or_trim(audio)

#crear espectrogrma
mel = whisper.log_mel_spectrogram(audio).to(model.device)

#detectar idioma
_,probs = model.detect_language(mel)
print(f"Idioma detectado:{max(probs,key=probs.get)}")

#decodificar audio
options = whisper.DecodingOptions()
result = whisper.decode(model,mel,options)

#Imprimir el texto reconocido
print(result.text)
