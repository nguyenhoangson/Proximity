from WaveGenerator.WaveGenerator import WaveGenerator
from Spectrogram.Spectrogram import Spectrogram

w = WaveGenerator().generate_from_wav_file("wav/test2.wav")

print("Frame_rate: " + str(w.get_frame_rate())) 

print("Data: " + str(w.get_data()))

print("Number of channels: " + str(w.get_nchannels()))

print("Number of frames: " + str(w.get_nframes()))

# spec = SpectrogramGenerator().generate_spectrogra(w)

# spec.plot()





