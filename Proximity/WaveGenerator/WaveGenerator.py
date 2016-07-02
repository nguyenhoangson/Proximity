# Wave generator that can generate wave object from different sources. E.g: .wav files
import numpy as np
from scipy.io import wavfile

# Wave class, it is simply just a data class
class Wave:

    def __init__(self, frame_rate, data): 
        self.frame_rate = frame_rate
        self.data = data # numpy array
        self.sample_width = data[0].dtype.itemsize # in bytes
        self.nframes = len(data)
         
    def get_data(self):
        return self.data

    def get_frame_rate(self):
        return self.frame_rate

    def get_sample_width(self):
        return self.sample_width

    def get_nframes(self):
        return self.nframes


class WaveGenerator:

    ''' 
       | generate_from_wav_file() will always generate mono Wave,
       | if file is stereo, it will convert to mono 
    '''
    def generate_mono_wave_from_wav_file(self, file):
        try:
            # Read .wav file
            frame_rate, data = wavfile.read(file)

            # Convert data to mono, if it is stereo
            data = convert_to_mono(data)
            
            # Make Wave object
            wave = Wave(frame_rate, data)

            return wave

        except Exception as e:
            print("Exception: " + str(e))
        


# Helper functions
''' 
   | convert mono audio data to stereo audio data, if data is already mono, 
   | then it will keep data and return 
'''
def convert_to_mono(data):

    mono_wave = []

    # Convert data into mono, if it is stereo
    if(len(data.shape) == 1):
        mono_wave = data
    else:
        mono_wave = np.mean(data, axis=1)
        
    return mono_wave
