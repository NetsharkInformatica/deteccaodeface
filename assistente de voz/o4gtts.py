from gtts import gTTS
from playsound import playsound
import os

def cria_audio(mensagem):
    tts= gTTS(mensagem,lang="pt-br")
    tts.save("assistente de voz/dados/mensagem.mp3")
    playsound("assistente de voz/dados/mensagem.mp3")
    os.remove("assistente de voz/dados/mensagem.mp3")
    #os.rename("assistente de voz/dados/mensagem.mp3", "assistente de voz/dados/audio.mp3")


cria_audio("Para conhecermos os amigos é necessário passar pelo sucesso e pela desgraça. No sucesso, verificamos a quantidade e, na desgraça, a qualidade")

frase=input("digite uma frase  :")
cria_audio(frase)

with open("assistente de voz/dados/frase.txt","r",encoding="utf-8")as texto:
    conteudo =texto.read()
    cria_audio(conteudo)