# from Wave import Wave
from WaveGenerator.WaveGenerator import WaveGenerator

w = WaveGenerator().generate_from_wav_file("wav/test1.wav")

print("Frame_rate: " + str(w.get_frame_rate()))

print("Data: " + str(w.get_data()))

print("Number of channels: " + str(w.get_nchannels()))

print("Number of frames: " + str(w.get_nframes()))
