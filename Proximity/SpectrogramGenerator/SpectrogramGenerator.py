# Generator which can generate spectrogram
# from a Wave object

from Spectrogram import Spectrogram

class SpectrogramGenerator():

    def generate_spectrogram(self, wave):
        return Spectrogram(wave)
