import speech_recognition as sr

recon=sr.Recognizer()
with sr.Microphone()as source:
    print("diga alguma coisa")
    audio=recon.listen(source)
    #print("reconhecendo...")


print(recon.recognize_google(audio,language="pt-br"))