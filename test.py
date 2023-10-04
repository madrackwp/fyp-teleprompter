import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np

x_continuous = np.linspace(0, 10, 100)
y_continuous = np.sin(x_continuous)

# Non-continuous x-axis data
x_non_continuous = [1, 2, 4, 7, 8]
y_non_continuous = [0.5, 0.8, 0.2, 0.6, 0.9]

# Create a figure and plot the continuous data
plt.figure(figsize=(8, 4))  # Set the figure size
plt.plot(x_continuous, y_continuous, label='Continuous')

# Plot the non-continuous data with markers
plt.plot(x_non_continuous, y_non_continuous, 'ro', label='Non-Continuous')

# Add labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.grid(True)  # Add a grid for clarity
plt.title('Mixed Continuous and Non-Continuous Plot')
plt.show()
# wav_file = wave.open('your_audio.wav', 'rb')
# wav_file = wave.open('audiofiles/processed/output_segment_0.wav', 'rb')

# channels = wav_file.getnchannels()
# sample_width = wav_file.getsampwidth()
# frame_rate = wav_file.getframerate()
# num_frames = wav_file.getnframes()

# audio_data = wav_file.readframes(num_frames)


# if channels == 2:
#     left_channel_data = np.frombuffer(audio_data, dtype=np.int16)[::2]
#     right_channel_data = np.frombuffer(audio_data, dtype=np.int16)[1::2]
#     # right_channel_data =
# else:
#     left_channel_data = np.frombuffer(audio_data, dtype=np.int16)

# time = np.arange(0, len(left_channel_data)) / frame_rate

# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))


# ax1.plot(time, left_channel_data)
# ax1.set_title('Left Channel')
# ax1.set_xlabel('Time (s)')
# ax1.set_ylabel('Amplitude')
# ax1.grid()

# # Plot the right channel waveform (if available)

# ax2.plot(time, right_channel_data)
# ax2.set_title('Right Channel')
# ax2.set_xlabel('Time (s)')
# ax2.set_ylabel('Amplitude')
# ax2.grid()

# # Adjust spacing between subplots
# plt.tight_layout()

# # Show the plots
# plt.show()


# Read the audio data
# audio_data = wav_file.readframes(num_frames)


# wav_file = wave.open('your_audio.wav', 'rb')

# audio = pyaudio.PyAudio()

# stream = audio.open(
#     format=audio.get_format_from_width(wav_file.getsampwidth()),
#     channels=wav_file.getnchannels(),  # Listen to the left channel
#     rate=wav_file.getframerate(),
#     output=True
# )

# chunk_size = 1024

# data = wav_file.readframes(chunk_size)

# while data:
#     stream.write(data)
#     data = wav_file.readframes(chunk_size)

# stream.stop_stream()
# stream.close()
# audio.terminate()
