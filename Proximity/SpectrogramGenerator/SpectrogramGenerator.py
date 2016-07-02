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
            
            self.spectrogram = signal.spectrogram(x=self.wave.get_data(), fs=self.wave.get_frame_rate(), nperseg=nperseg, noverlap=noverlap)

        except Exception as e:
            print('Exception: ' + str(e))

    def show(self):

        ''' 
          | Show the spectrogram graphically
        '''
        plt.pcolormesh(self.spectrogram[1], self.spectrogram[0], self.spectrogram[2])
        plt.xlabel('Time [sec]')
        plt.ylabel('Frequency [Hz]')
        plt.show()

    def get_data(self):
        return self.spectrogram

class SpectrogramGenerator():

    def generate_spectrogram(self, mono_wave):
        return Spectrogram(mono_wave)



