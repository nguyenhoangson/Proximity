# Generator which can generate spectrogram
# from a Wave object
from scipy import signal
import matplotlib.pyplot as plt

# Create Spectrogram for wave object
class Spectrogram:

    def __init__(self, wave, nperseg=512, noverlap=None):

        try: 
            self.wave = wave # Wave must be mono 
            self.nperseg = nperseg # Length of each segment.Defaults to 512

            # Number of points to overlap between each segment
            # Defaults to None = nperseg // 8 
            if(not noverlap):
                self.noverlap = nperseg // 8
            else:
                self.noverlap = noverlap
            
            self.freq, self.times, self.spectrogram = signal.spectrogram(self.wave.get_data())

        except Exception as e:
            print('Exception: ' + str(e))

    def show(self):
        plt.pcolormesh(self.times, self.freq, self.spectrogram)
        plt.xlabel('Time [sec]')
        plt.ylabel('Frequency [Hz]')
        plt.show()
    

class SpectrogramGenerator():

    def generate_spectrogram(self, wave):
        return Spectrogram(wave)



