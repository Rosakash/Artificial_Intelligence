import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read the audio file
sampling_freq, signal = wavfile.read('C://Users//Akash Roshan//Downloads//hmm-Reading_Audio_File-recognition-0.1//hmm-Reading_Audio_File-recognition-0.1//audio//apple//apple01.wav')

# Normalize the values
signal = signal / np.power(2, 15)

# Extract the length of the audio signal
len_signal = len(signal)
# Extract the half length
len_half = np.ceil((len_signal + 1) / 2.0).astype(np.int)

freq_signal = np.fft.fft(signal)

freq_signal = abs(freq_signal[0:len_half]) / len_signal

freq_signal **=2
len_fts = len(freq_signal)
# Adjust the signal for even and odd cases
if len_signal % 2:
    freq_signal[1:len_fts] *= 2
else:
    freq_signal[1:len_fts-1] *= 2
signal_power = 10 * np.log10(freq_signal)

x_axis = np.arange(0, len_half, 1) * (sampling_freq/len_signal) / 1000.0

plt.figure()
plt.plot(x_axis, signal_power, color='black')
plt.xlabel('Frequency (kHz)')
plt.ylabel('$ignal power (dB)')
plt.show()