from random import randint
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time

def cria_audio(audio, mensagem):
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(audio), exist_ok=True)
    
    tts = gTTS(mensagem, lang="pt-br")
    tts.save(audio)
    playsound(audio)
    os.remove(audio)

# Configuração inicial
recon = sr.Recognizer()
microfone = sr.Microphone()

# Ajuste de ruído ambiente (IMPORTANTE!)
with microfone as source:
    print("Ajustando ruído ambiente... Aguarde 2 segundos.")
    recon.adjust_for_ambient_noise(source, duration=2)
    print("Microfone ajustado!")

# Gera número secreto
numero_secreto = randint(1, 10)
cria_audio("assistente de voz/dados/escolha.mp3", f"Escolha um número entre 1 e 10")

# Captura de voz com tratamento de erros
try:
    with microfone as source:
        print("\nDiga o número agora (você tem 5 segundos):")
        audio = recon.listen(source, timeout=5, phrase_time_limit=3)
        
    # Reconhecimento
    numero_texto = recon.recognize_google(audio, language="pt-br").strip()
    print(f"Você disse: {numero_texto}")
    
    # Verificação
    if numero_texto.isdigit():
        numero = int(numero_texto)
        if numero == numero_secreto:
            cria_audio("assistente de voz/dados/acertou.mp3", "Parabéns! Você acertou!")
        else:
            cria_audio("assistente de voz/dados/errou.mp3", f"Errado! O número era {numero_secreto}")
    else:
        cria_audio("assistente de voz/dados/invalido.mp3", "Isso não é um número válido.")

except sr.WaitTimeoutError:
    print("Tempo esgotado! Você não disse nada.")
    cria_audio("assistente de voz/dados/timeout.mp3", "Não ouvi sua resposta. Tente novamente.")

except sr.UnknownValueError:
    print("Não entendi o que você disse.")
    cria_audio("assistente de voz/dados/nao_entendi.mp3", "Não consegui entender. Repita, por favor.")

except sr.RequestError as e:
    print(f"Erro na conexão: {e}")
    cria_audio("assistente de voz/dados/sem_internet.mp3", "Preciso de internet para funcionar.")

except Exception as e:
    print(f"Erro inesperado: {e}")