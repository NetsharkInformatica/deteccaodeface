import os
import time
from datetime import datetime


def verifica_hora():
    hora= datetime.now().strftime("%H:%M")
    frase=f"Agora são {hora} ."
    return frase


def desliga_computador_uma_hor():
    os.system("shutdown /s /t 3600")


def reinicia_computador():
    os.system("shutdown /r /t 1800")

def cancela_desligamento():
    os.system("shutdown /a")
    print("Desligamento cancelado.")
    time.sleep(2)
    print("Você pode continuar usando o computador.")