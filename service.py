import librosa
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from collections import deque


def detect_peaks(signal, threshold):
    peaks, _ = find_peaks(signal, height=threshold, width=100)
    return peaks


def peakAnalysis():
    audio = pyaudio.PyAudio()
    # Parameters for audio stream
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    RATE = 44100
    CHUNK_SIZE = 2048


    THRESHOLD = 0.02
    audio = pyaudio.PyAudio()
    count = 0
    peakBuffer = deque(maxlen=CHUNK_SIZE)



    # Set up PyAudio

    # Create an input stream
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
    )

    plt.ion()  # Turn on interactive mode AKA allows for dynamic updates to the plot
    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK_SIZE)  # This sets the range of the x axis
    (line,) = ax.plot(x, np.random.rand(CHUNK_SIZE))

    # Continuous audio capture and analysis
    while True:
        # Read audio data from the stream
        audio_data = stream.read(CHUNK_SIZE)

        # Convert the data to a numpy array
        audio_array = np.frombuffer(audio_data, dtype=np.float32)


        peak_indices = detect_peaks(audio_array, THRESHOLD)
        # print(len(peak_indices))
        if len(peakBuffer) == CHUNK_SIZE:
            peakBuffer.popleft()
        if len(peak_indices) > 0:
            peakBuffer.append(True)
        else:
            peakBuffer.append(False)

        flag = check_consecutive_ones(peakBuffer, 2)
        if flag:
            count += 1
            peakBuffer.clear()
            print("WORD SPOKEN")
            print("WORD COUNT: ", count)

        line.set_ydata(audio_array)
        fig.canvas.draw()
        fig.canvas.flush_events()

def energyLevelDetection():
    ENERGY_THRESHOLD = 0.0005
    count = 0
    is_speaking = False
    bufferSize = 10
    # Set up PyAudio
    audio = pyaudio.PyAudio()
    # Parameters for audio stream
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    RATE = 44100
    CHUNK_SIZE = 2048
    peakBuffer = deque(maxlen=CHUNK_SIZE)

    bufferMin = 5
    buffer = deque(maxlen=bufferMin)
    # Create an input stream
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE,
    )

    plt.ion()  # Turn on interactive mode AKA allows for dynamic updates to the plot
    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK_SIZE)  # This sets the range of the x axis
    (line,) = ax.plot(x, np.random.rand(CHUNK_SIZE))

    while True:
        audio_data = stream.read(CHUNK_SIZE)

        # Convert the data to a numpy array
        audio_array = np.frombuffer(audio_data, dtype=np.float32)

        # Calculate the energy or use the peak indices as an indicator
        energy = np.mean(np.square(audio_array))

        is_speaking = energy > ENERGY_THRESHOLD
        # Determine if someone is speaking based on the threshold
        if len(peakBuffer) == CHUNK_SIZE:
            peakBuffer.popleft()
        peakBuffer.append(is_speaking)

        flag = check_consecutive_ones(peakBuffer, 2)
        if flag:
            count += 1
            peakBuffer.clear()
            print("Word spoken!")
            print("Word Count: ", count)


        line.set_ydata(audio_array)
        fig.canvas.draw()
        fig.canvas.flush_events()

        # Print the result


def check_consecutive_ones(arr, consecutive_threshold):
    ones_count = 0
    # print(len(arr))
    for i in range(len(arr)):
        if arr[i] == True:
            ones_count += 1
            if ones_count >= consecutive_threshold:
                if i + 1 < len(arr) and arr[i + 1] == False:
                    return True
                # else:
                #     return False
        else:
            ones_count = 0

    return False


# energyLevelDetection()
peakAnalysis()