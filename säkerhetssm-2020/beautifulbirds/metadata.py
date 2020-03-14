'''
import eyed3
tag = eyed3.Tag()
tag.link("birds.wav")
for frame in tag.frames:
   print(frame)
'''
import wave
audiofile = wave.open("birds.wav")
