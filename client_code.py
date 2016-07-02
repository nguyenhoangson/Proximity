from Proximity.WaveGenerator.WaveGenerator import WaveGenerator
from Proximity.SpectrogramGenerator.SpectrogramGenerator import SpectrogramGenerator

w = WaveGenerator().generate_mono_wave_from_wav_file("wav/test2.wav")

print("Frame_rate: " + str(w.get_frame_rate())) 

print("Data: " + str(w.get_data()))

print("Number of frames: " + str(w.get_nframes()))

# spec = SpectrogramGenerator().generate_spectrogram(w)

# spec.show()
# spec.get_data()

# To expose the data of spectrogram to the world




