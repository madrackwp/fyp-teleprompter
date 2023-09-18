import wave
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Function to read audio data from a WAV file
def read_audio(file_path):
    wf = wave.open(file_path, "rb")
    data = wf.readframes(-1)
    print(data)
    processData = np.frombuffer(data, dtype=np.int16)
    print(processData)
    print(len(processData))
    return processData, wf.getframerate()

xdata, ydata = [], []




# WAV file path
# wav_file = "your_audio.wav"
wav_file = "audiofiles/processed/output_segment_0.wav"

# Read audio data and frame rate
audio_data, frame_rate = read_audio(wav_file)
print(len(audio_data))

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, len(audio_data))
ax.set_ylim(-32768, 32767)  # Adjust based on the audio data format

# Create an initial line object for the plot
line, = ax.plot([], [], lw=2)


# Chunk size for updating the plot (adjust as needed)
chunk_size = int(frame_rate / 10)  # Update every 100 ms

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open an audio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=frame_rate, output=True)

# Function to update the plot in real-time
def update_plot(frame):
    # print(frame)
    xdata.append(1)
    ydata.append(frame)
    # print(len(frame))
    line.set_data(xdata, ydata)
    return line, 
    # try:
    #     data_chunk = audio_data[frame * chunk_size : (frame + 1) * chunk_size]
    #     line.set_ydata(data_chunk)
    #     return (line,)
    # except IndexError:
    #     return (line,)

# Create an animation to update the plot
ani = FuncAnimation(fig = fig, func = update_plot, frames = audio_data, blit=True)

# Play the audio
# for frame in range(len(audio_data) // chunk_size):
#     data_chunk = audio_data[frame * chunk_size : (frame + 1) * chunk_size]
#     stream.write(data_chunk.tobytes())

# Close the audio stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()

plt.show()
