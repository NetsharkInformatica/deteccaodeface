import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")

#utilizando prompt para entrada de texto
# frase = input("Digite a frase:/n ")
# engine.say(frase)
# engine.runAndWait()

#utilizando um arquivo de texto

# arquivo = open("dados//frase.txt", "r",encoding="utf-8")
# conteudo= arquivo.read()
# engine.say(conteudo)
# engine.runAndWait()

with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo=arquivo.read()
    engine.say(conteudo)
    engine.runAndWait()
