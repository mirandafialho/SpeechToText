import speech_recognition as speech

read = speech.Recognizer()
read.energy_threshold = 2000

with speech.Microphone() as source:
    print ('Say something. (English only)')
    audio = read.listen(source)

try:
    print ('Google API thinks you said: \n' + read.recognize_google(audio))

except:
    pass
