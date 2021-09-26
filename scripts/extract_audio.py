import sys
import moviepy.editor as mpy

clip = mpy.VideoFileClip(sys.argv[1], audio=True)
clip.audio.to_audiofile(sys.argv[2], write_logfile=False)

# visualization with matplotlib : https://ngbala6.medium.com/audio-processing-and-remove-silence-using-python-a7fe1552007a
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

# Read the Audiofile
samplerate, data = read(sys.argv[2])
# Frame rate for the Audio
print(samplerate)

# Duration of the audio in Seconds
duration = len(data)/samplerate
print("Duration of Audio in Seconds", duration)
print("Duration of Audio in Minutes", duration/60)

time = np.arange(0,duration,1/samplerate)

# Plotting the Graph using Matplotlib
plt.plot(time,data)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('tmp.wav')
plt.show()
