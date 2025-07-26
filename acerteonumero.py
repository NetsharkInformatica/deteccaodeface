from random import randint
import speech_recognition as sr
from gtts import gTTS  
from playsound import playsound
import os


def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)


cria_audio("assistente de voz/dados/escolha.mp3","escolha um numero entre 1 e 10")
recon= sr.Recognizer()
with sr.Microphone() as source:
    #recon.adjust_for_ambient_noise(source, duration=1)  # Reduz ruído
    print("diga alguma coisa")
    audio = recon.listen(source,timeout=5)
    #recon.adjust_for_ambient_noise(source, duration=1)  # Reduz ruído

    # print("reconhecendo...")

numero_texto = recon.recognize_google(audio, language="pt-br")

word_to_digit={
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10
}

#numero_digito= word_to_digit[numero_texto]
#print(f"Você disse: {numero_texto}")

resultado=randint(1,10)
print(resultado)

if numero_texto==resultado:
    cria_audio("assistente de voz/dados/acertou.mp3","Parabéns, você acertou o número")
else:
    cria_audio("assistente de voz/dados/errou.mp3","Você errou o número, o número era " + str(resultado))
    
