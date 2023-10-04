import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import wave
from utility import read_audio as audio
from utility import check_consecutive_ones as cco


def sliding_window(audio_file_input):
    # ENERGY_THRESHOLD = 1000
    wordCount = 0
    # audioFile = "output_segment_0.wav"
    audioFile = audio_file_input

    ambientNoiseSampleDuration = 0.2

    # energyGraphx, energyGraphy = [], []

    audio_data, sample_rate, nchannels = audio.read_audio(
        f"audiofiles/processed/{audioFile}"
    )

    ambientNoiseBufferLen = int(ambientNoiseSampleDuration * sample_rate * nchannels)
    print(ambientNoiseBufferLen)

    # CHUNK_SIZE = 4096
    CHUNK_SIZE = 35280 // 2
    # CHUNK_SIZE = 13000
    # peakBuffer = deque(maxlen=CHUNK_SIZE // 16)
    time_axis = np.linspace(
        0, len(audio_data) / sample_rate / nchannels, num=len(audio_data)
    )
    plt.figure(figsize=(10, 4))
    plt.plot(time_axis, audio_data)

    ambientNoiseBuffer = []
    for i in range(ambientNoiseBufferLen):
        ambientNoiseBuffer.append(audio_data[i])
    print(len(ambientNoiseBuffer))
    print(max(ambientNoiseBuffer), min(ambientNoiseBuffer))
    print(abs(np.mean(ambientNoiseBuffer)))


audioFile = "output_segment_1.wav"

sliding_window(audioFile)
