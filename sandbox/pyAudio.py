import librosa
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

audio = pyaudio.PyAudio()

# Set up PyAudio
audio = pyaudio.PyAudio()

# Parameters for audio stream
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 2048

# Create an input stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)

plt.ion()  # Turn on interactive mode AKA allows for dynamic updates to the plot
fig, ax = plt.subplots()
x = np.arange(0, CHUNK_SIZE) #This sets the range of the x axis
line, = ax.plot(x, np.random.rand(CHUNK_SIZE))

# Continuous audio capture and analysis
while True:
    # Read audio data from the stream
    audio_data = stream.read(CHUNK_SIZE)
    
    # Convert the data to a numpy array
    audio_array = np.frombuffer(audio_data, dtype=np.float32)
    
    # Perform audio analysis with Librosa
    # Example: Compute RMS energy
    rms = np.sqrt(np.mean(np.square(audio_array)))
    
    # Print the RMS energy
    print("RMS energy:", rms)
    line.set_ydata(audio_array)
    fig.canvas.draw()
    fig.canvas.flush_events()



