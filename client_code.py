from Proximity.WaveGenerator.WaveGenerator import WaveGenerator
from Proximity.Spectrogram.Spectrogram import Spectrogram

w = WaveGenerator().generate_from_wav_file("wav/test1.wav")

print("Frame_rate: " + str(w.get_frame_rate())) 

print("Data: " + str(w.get_data()))

print("Number of channels: " + str(w.get_nchannels()))

print("Number of frames: " + str(w.get_nframes()))

# spec = SpectrogramGenerator().generate_spectrogram(w)

# spec.plot()

# spec.get_data() # To expose the data of spectrogram to the world




