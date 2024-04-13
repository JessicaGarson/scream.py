import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100
duration = 5

# Record your scream
myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
print("Recording screams")
sd.wait()

# Play back your scream
print("Scream recorded. Play back time!")
sd.play(myrecording, fs)
sd.wait()

# Create the wav file
print("I can now use my scream file!")
wav.write('/Users/jessgarson/Documents/scream.wav', fs, myrecording)
