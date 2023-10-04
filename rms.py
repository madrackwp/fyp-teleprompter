import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import wave
from utility import read_audio as audio
from utility import check_consecutive_ones as cco


def RMS(audio_file_input):
    ENERGY_THRESHOLD = 1000
    wordCount = 0
    is_speaking = False
    # audioFile = "output_segment_0.wav"
    audioFile = audio_file_input

    energyGraphx, energyGraphy = [], []

    audio_data, sample_rate, nchannels = audio.read_audio(
        f"audiofiles/processed/{audioFile}"
    )

    # CHUNK_SIZE = 4096
    CHUNK_SIZE = 35280 // 2
    # CHUNK_SIZE = 13000
    # peakBuffer = deque(maxlen=CHUNK_SIZE // 16)
    time_axis = np.linspace(
        0, len(audio_data) / sample_rate / nchannels, num=len(audio_data)
    )
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_data)

    # plt.figure(figsize=(10, 4))
    # plt.plot(time_axis, audio_data, color="b")
    # plt.title(f"{audioFile}")
    # plt.xlabel("Time (s)")
    # plt.ylabel("Amplitude")
    # plt.grid(True)

    count = 0
    for i in range(0, len(audio_data) - CHUNK_SIZE, CHUNK_SIZE // 32):
        count += 1

        buffer = audio_data[i : i + CHUNK_SIZE]
        npBuffer = np.array(buffer, dtype=np.int32)
        # Calculate the energy or use the peak indices as an indicator
        squared = np.square(npBuffer)
        meaned = np.mean(squared)
        rms = np.sqrt(meaned)
        energy = rms
        # print(energy)
        # if energy == np.nan:
        #     print(energy)
        energyGraphy.append(energy)
        energyGraphx.append((i + CHUNK_SIZE) / sample_rate / nchannels)

        # I want to check the past 3 values, if the middle value is higher than both the values before and after, increment word by one
        ## First get the past 3 values
        if len(energyGraphy) >= 5:

            latestValue = energy
            secondLastValue = energyGraphy[-2]
            middleValue = energyGraphy[-3]
            secondValue = energyGraphy[-4]
            firstValue = energyGraphy[-5]

            if secondLastValue > latestValue and secondValue > firstValue and middleValue > secondValue and middleValue > secondLastValue and middleValue >= ENERGY_THRESHOLD:
                wordCount += 1
                plt.axvline(x=energyGraphx[len(energyGraphx)-2], color="r")

            # latestValue = energy
            # middleValue = energyGraphy[-2]
            # earliestValue = energyGraphy[-3]
            # if middleValue >= latestValue and middleValue >= earliestValue and middleValue >= ENERGY_THRESHOLD:
            #     print(earliestValue, middleValue, latestValue)
            #     # print(middleValue, i)
            #     wordCount += 1
            #     plt.axvline(x=energyGraphx[len(energyGraphx)-2], color="r")

        # if energy > ENERGY_THRESHOLD:
        #     print(energy, i / sample_rate / nchannels)
        #     wordCount += 1
        #     # plt.axvline(x=i / sample_rate / nchannels, color="g")  # Start of window
        #     plt.axvline(
        #         x=(i + CHUNK_SIZE) / sample_rate / nchannels, color="r"
        #     )  # End of window
        # is_speaking = energy > ENERGY_THRESHOLD
        # # Determine if someone is speaking based on the threshold
        # if len(peakBuffer) == CHUNK_SIZE//16:
        #     peakBuffer.popleft()
        # peakBuffer.append(is_speaking)

        # flag = cco.check_consecutive_ones(peakBuffer, 2)
        # if flag:
        #     wordCount += 1
        #     peakBuffer.clear()
        #     plt.axvline(x=(i - CHUNK_SIZE) / sample_rate / nchannels, color="g")
        #     plt.axvline(x=i / sample_rate / nchannels, color="r")

    plt.plot(energyGraphx, energyGraphy, "ro", markersize=3)
    plt.title(f"{audioFile}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    # plt.show()

    print(f"NUMBER OF WORDS: {wordCount}")
    # print(count)

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
audioFile = "output_segment_1.wav"

RMS(audioFile)
