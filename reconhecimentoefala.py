import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


cria_audio("assistente de voz/dados/bemvindo.mp3","ola, vou reconhecer a sua voz")
recon = sr.Recognizer()
with sr.Microphone() as source:
    print("diga alguma coisa")
    audio = recon.listen(source)
    # print("reconhecendo...")  

frase=recon.recognize_google(audio,language="pt-br")
cria_audio("assistente de voz/dados/mensagem.mp3",frase)

