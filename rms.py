import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import wave
from utility import read_audio as audio
from utility import check_consecutive_ones as cco

def RMS(audio_file_input):
    ENERGY_THRESHOLD = 0.0005
    count = 0
    is_speaking = False
    # audioFile = "output_segment_0.wav"
    audioFile = audio_file_input

    audio_data, sample_rate, nchannels = audio.read_audio(f"audiofiles/processed/{audioFile}")

    CHUNK_SIZE = 4096
    peakBuffer = deque(maxlen=CHUNK_SIZE)
    time_axis = np.linspace(0, len(audio_data)/sample_rate/nchannels, num=len(audio_data))

    plt.figure(figsize=(10,4))
    plt.plot(time_axis, audio_data, color="b")
    plt.title(f"{audioFile}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)


    for i in range(0, len(audio_data) - CHUNK_SIZE, CHUNK_SIZE//2):
        buffer = audio_data[i:i+CHUNK_SIZE]
        # Calculate the energy or use the peak indices as an indicator
        energy = np.mean(np.square(buffer))
        # print(energy)

        is_speaking = energy > ENERGY_THRESHOLD
        # Determine if someone is speaking based on the threshold
        if len(peakBuffer) == CHUNK_SIZE:
            peakBuffer.popleft()
        peakBuffer.append(is_speaking)

        flag = cco.check_consecutive_ones(peakBuffer, 2)
        if flag:
            count += 1
            peakBuffer.clear()
            plt.axvline(x=(i-CHUNK_SIZE)/sample_rate/nchannels, color="g")
            plt.axvline(x=i/sample_rate/nchannels, color="r")


    print(f"NUMBER OF WORDS: {count}")
    plt.show()



# def check_consecutive_ones(arr, consecutive_threshold):
#     ones_count = 0
#     # print(len(arr))
#     for i in range(len(arr)):
#         if arr[i] == True:
#             ones_count += 1
#             if ones_count >= consecutive_threshold:
#                 if i + 1 < len(arr) and arr[i + 1] == False:
#                     return True
#                 # else:
#                 #     return False
#         else:
#             ones_count = 0

#     return False
audioFile = "output_segment_0.wav"

RMS(audioFile)