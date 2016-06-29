# Wave generator that can generate wave object from different sources. E.g: .wav files
from Wave import Wave
import numpy as np
from scipy.io import wavfile

class WaveGenerator:

    def generate_from_wav_file(self, file):

        try:

            # Read .wav file
            frame_rate, data = wavfile.read(file)

            # Make Wave object
            wave = Wave(frame_rate, data)

            return wave

        except Exception as e:
            
            print("Exception: " + str(e))
        
