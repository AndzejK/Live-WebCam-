import sounddevice
from scipy.io.wavfile import write
# How long to record
sec=5 
fps=44100 # Sampling rate/Hertz

my_rec=sounddevice.rec(frames=sec*fps,samplerate=fps,channels=1)
sounddevice.wait()
write('audio/rec_output.mp3',fps,my_rec)