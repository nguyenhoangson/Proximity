from Proximity.WaveGenerator.WaveGenerator import WaveGenerator, convert_to_mono
import numpy as np
from scipy.io import wavfile

def test_convert_to_mono_when_data_wave_is_mono():
    test_data = np.array([1, 2, 3])
    expected = np.array([1,2,3])
    actual = convert_to_mono(test_data)

    assert np.array_equal(expected, actual)

def test_convert_to_mono_when_data_wave_is_stereo():
    test_data = np.array([[1,2], [2,3]])
    expected = np.array([1.5, 2.5])
    actual = convert_to_mono(test_data)

    assert np.array_equal(expected, actual)

def test_convert_to_mono_by_reading_wave_from_stereo_wav_file():
    frame_rate, data = wavfile.read("test.WAV")
    expected = np.mean(data, axis=1)
    actual = convert_to_mono(data)

    assert np.array_equal(expected, actual)

