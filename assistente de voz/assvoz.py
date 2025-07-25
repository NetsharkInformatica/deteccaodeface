import pyttsx3

engine=pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.say("Olá, eu sou o assistente de voz. Estou aqui para ajudar você com suas tarefas diárias. O que posso fazer por você hoje?")

engine.runAndWait()