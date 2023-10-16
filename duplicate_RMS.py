import numpy as np
import matplotlib.pyplot as plt
import pyaudio
from collections import deque
import wave
from utility import read_audio as audio
from utility import check_consecutive_ones as cco


def audioAnalysis(audio_file_input = None):
    

    CHUNK = 1024  # Number of frames per buffer
    FORMAT = pyaudio.paInt16  # Format for audio input
    CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
    RATE = 44100  # Sample rate (samples per second)
    RECORD_SECONDS = 5  # Duration of recording in seconds

    ENERGY_THRESHOLD = 800
    # ENERGY_THRESHOLD = 1000
    # WHITENOISE_DURATION = 0.5 #in seconds
    wordCount = 0
    # is_speaking = False
    wordFlag = False

    whiteNoiseBuffer = []
    energyGraphx, energyGraphy = [], []

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    print("Recording...")

    ROLLING_BUFFER_SIZE = 44100  # Adjust as needed, should be larger than CHUNK_SIZE
    audio_data = np.zeros(ROLLING_BUFFER_SIZE, dtype=np.int16)

    # while True:
    while True:
        # Read audio data from the stream
        audio_chunk = np.frombuffer(stream.read(CHUNK), dtype=np.int16)

        # Add the new audio chunk to the rolling buffer
        audio_data = np.roll(audio_data, -len(audio_chunk))
        audio_data[-len(audio_chunk):] = audio_chunk

    # for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)




    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    print(audio_data)


    


    audioFile = audio_file_input


    # audio_data, sample_rate, nchannels = audio.read_audio(
    #     f"audiofiles/raw/{audioFile}"
    # )
    # audio_data, sample_rate, nchannels = audio.read_audio(
    #     audioFile
    # )
    print("DATA HERE!")
    # print(audio_data)
 
    CHUNK_SIZE = 35280 // 2

    time_axis = np.linspace(
        0, len(audio_data) / sample_rate / nchannels, num=len(audio_data)
    )
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_data)


    WHITENOISEBUFFERSIZE = 56 

    count = 0
    whiteNoiseEnergy = None
    non_silence_count = 0

    silenceBuffer = []
    
    for i in range(0, len(audio_data) - CHUNK_SIZE, CHUNK_SIZE // 32):

        count += 1

        buffer = audio_data[i : i + CHUNK_SIZE]
        npBuffer = np.array(buffer, dtype=np.int32)
        # Calculate the energy or use the peak indices as an indicator
        squared = np.square(npBuffer)
        meaned = np.mean(squared)
        rms = np.sqrt(meaned)
        energy = rms

        if len(whiteNoiseBuffer) < WHITENOISEBUFFERSIZE * 3:
            whiteNoiseBuffer.append(energy)
            # plt.axvline(x=(i + CHUNK_SIZE) / sample_rate / nchannels, color="g")
        elif whiteNoiseEnergy is None:
            whiteNoiseEnergy = np.mean(whiteNoiseBuffer)
            print(f"White Noise energy calculated: {whiteNoiseEnergy}")

        if whiteNoiseEnergy is not None:
            # print("HERE")
            if energy <= whiteNoiseEnergy:
                # print("SILENCE DETECTED!")
                silenceBuffer.append(energy)
                non_silence_count = 0
            elif len(silenceBuffer) > 0 and energy > whiteNoiseEnergy:
                non_silence_count += 1

            if non_silence_count == 5:
                silenceBuffer.clear()
                non_silence_count = 0
                print("SILENCE BUFFER CLEARED!")


            if len(silenceBuffer) == WHITENOISEBUFFERSIZE // 2 and wordFlag:
                print("PERIOD DETECTED!")
                plt.axvline(x=(i + CHUNK_SIZE) / sample_rate / nchannels, color="orange")
                silenceBuffer.clear()
                non_silence_count = 0
                wordFlag = False
                

        #this is just for plotting of the graph
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
                if not wordFlag:
                    wordFlag = True
                plt.axvline(x=energyGraphx[len(energyGraphx)-3], color="r")

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
    # print(len(whiteNoiseBuffer))
    # print(np.mean(whiteNoiseBuffer))
    # print(WHITENOISE_DURATION * sample_rate // 32)
    # plt.plot(energyGraphx, energyGraphy, "ro", markersize=3)
    plt.title(f"{audioFile}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    print(f"NUMBER OF WORDS: {wordCount}")
    # print(count)

    # plt.show()


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
# audioFile = "audiofiles/raw/harvard.wav"
audioFile = "audiofiles/processed/output_segment_1.wav"

audioAnalysis(audioFile)
