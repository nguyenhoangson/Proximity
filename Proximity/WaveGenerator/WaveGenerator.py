# Wave generator that can generate wave object from different sources. E.g: .wav files
import numpy as np
from scipy.io import wavfile

# Wave class, it is simply just a data class
class Wave:

    def __init__(self, frame_rate, data):
        self.data = data # numpy array 
        self.nchannels = len(data.shape) # whether it is mono or stereo depending on the shape of the data
        self.frame_rate = frame_rate
        self.sample_width = data[0].dtype.itemsize # in bytes
        self.nframes = len(data)
        
    def get_data(self):
        return self.data
    
    def get_nchannels(self):
        return self.nchannels

    def get_frame_rate(self):
        return self.frame_rate

    def get_sample_width(self):
        return self.sample_width

    def get_nframes(self):
        return self.nframes


class WaveGenerator:

    def generate_from_wav_file(self, file):
        try:
            # Read .wav file
            frame_rate, data = wavfile.read(file)

            print(frame_rate)
            print(data)
            # Make Wave object
            wave = Wave(frame_rate, data)

            return wave

        except Exception as e:
            print("Exception: " + str(e))
        
