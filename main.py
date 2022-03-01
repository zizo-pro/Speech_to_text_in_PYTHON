import speech_recognition as sr
from os import chdir , listdir , path , remove
from pydub import AudioSegment


chdir(r"C:\zizo\projects\PYTHON\speech_to_text\audio")

test = listdir()
for i in test:
	sound = AudioSegment.from_mp3(i)
	ind = i.find(".")
	wa = i[:int(ind)]
	wav = f"{wa}.wav"
	sound.export(wav,format="wav")

	r = sr.Recognizer()

	with sr.AudioFile(wav) as source:
		audio_data = r.record(source)

		text = r.recognize_google(audio_data , language="de-DE")
	
	with open(fr"C:\zizo\projects\PYTHON\speech_to_text\text\{wa}.txt", "w") as f:
		f.write(text)

	remove(i)
	remove(wav)



