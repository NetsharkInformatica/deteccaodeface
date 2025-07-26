from random import randint
import speech_recognition as sr
from gtts import gTTS  
from playsound import playsound
import os
import sys

def cria_audio(audio, mensagem):
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(audio), exist_ok=True)
    
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

def monitora_audio():
    recon = sr.Recognizer()  # Corrigido: Recognizer()
    with sr.Microphone() as source:  # Corrigido: Microphone()
        print("Ajustando ruído ambiente...")
        recon.adjust_for_ambient_noise(source, duration=1)  # Reduz ruído
        
        while True:
            print("Diga alguma coisa (ou 'fechar assistente' para sair):")
            try:
                audio = recon.listen(source, timeout=5)
                mensagem = recon.recognize_google(audio, language="pt-br").lower()
                print(f"Você disse: {mensagem}")
                return mensagem  # Retorna a mensagem para processamento externo

            except sr.UnknownValueError:
                print("Não entendi. Repita, por favor.")
                cria_audio("assistente de voz/dados/erro.mp3", "Não entendi. Repita, por favor.")
            except sr.RequestError:
                print("Erro de conexão. Verifique a internet.")
                cria_audio("assistente de voz/dados/sem_internet.mp3", "Sem conexão com a internet.")

def executa_comandos(acao):
    if "fechar assistente" in acao:
        cria_audio("assistente de voz/dados/adeus.mp3", "Até logo!")
        sys.exit()
    else:
        cria_audio("assistente de voz/dados/resposta.mp3", f"Você disse: {acao}")

def main():
    cria_audio("assistente de voz/dados/bemvindo.mp3", "Olá, sou a Ranicléia. Em que posso te ajudar?")
    while True:
        mensagem = monitora_audio()  # Captura a mensagem
        executa_comandos(mensagem)  # Executa a ação

if __name__ == "__main__":
    main()



""" numero_texto = monitora_audio()

    word_to_digit = {
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

    resultado = randint(1, 10)
    print(resultado)

    if numero_texto in word_to_digit:
        numero_digito = word_to_digit[numero_texto]
        if numero_digito == resultado:
            cria_audio("assistente de voz/dados/acertou.mp3", "Parabéns, você acertou o número")
        else:
            cria_audio("assistente de voz/dados/errou.mp3", f"Você errou o número, o número era {resultado}")
    else:
        cria_audio("assistente de voz/dados/erro.mp3", "Número inválido, tente novamente")
"""