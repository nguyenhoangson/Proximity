from Proximity.WaveGenerator.WaveGenerator import WaveGenerator
from Proximity.SpectrogramGenerator.SpectrogramGenerator import SpectrogramGenerator

w = WaveGenerator().generate_mono_wave_from_wav_file("wav/daron1.wav")

# print("Frame_rate: " + str(w.get_frame_rate())) 

# print("Data: " + str(w.get_data()))

# print("Number of frames: " + str(w.get_nframes()))


spec = SpectrogramGenerator().generate_spectrogram(w)

spec.show() # Draw the spectrogram 

freq, times, spect = spec.get_data() # get data of spectrogram




