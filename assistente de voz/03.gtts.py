from gtts import gTTS
from playsound import playsound


texto="Não fales bem de ti aos outros, pois não os convencerás. Não fales mal,pois te julgarão muito pior do que és."

tts= gTTS(texto, lang='pt-br')
tts.save(r"assistente de voz\dados\audio.mp3")
playsound("assistente de voz/dados/audio.mp3")