import numpy as np
import matplotlib.pyplot as plt
import pyaudio
from collections import deque
import wave
from PySide6.QtWidgets import QApplication
import sys
# sys.path.append("/Users/wpgoh/Documents/fyp-teleprompter/display")
# from utility import read_audio as audio
# from utility import check_consecutive_ones as cco

class AudioAnalyser():
    def __init__(self):
        self.CHUNK = 1024  # Number of frames per buffer
        self.FORMAT = pyaudio.paInt16  # Format for audio input
        self.CHANNELS = 1  
        self.RATE = 44100  # Sample rate (samples per second)
        self.nchannels = 1

        self.ENERGY_THRESHOLD = 800 #this is the RMS value threshold 
        self.wordCount = 0
        self.wordFlag = False

        self.WHITENOISEBUFFERSIZE = 56 
        self.CHUNK_SIZE = 35280 // 2

        self.whiteNoiseBuffer = []
        self.energyGraphx, self.energyGraphy = [], []

        self.whiteNoiseEnergy = None
        self.non_silence_count = 0

        self.silenceBuffer = []

        self.audio = pyaudio.PyAudio()
        # print("Recording...")

        self.ROLLING_BUFFER_SIZE = 44100  # Adjust as needed, should be larger than CHUNK_SIZE
        self.audio_data = np.zeros(self.ROLLING_BUFFER_SIZE // 2, dtype=np.int16)
        # self.GUI = gui.MainWindow()
        print("TELEPROMPTER CREATED")

    def start(self):
        print("Starting the teleprompter")
        # self.app = QApplication(sys.argv)
        # self.GUI.show()
        # self.app.exec_()
        while True:
            # Read audio data from the stream
            # print("Recording")
            self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)
            audio_chunk = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.int16)

            # Add the new audio chunk to the rolling buffer
            self.audio_data = np.roll(self.audio_data, -len(audio_chunk))
            self.audio_data[-len(audio_chunk):] = audio_chunk

            buffer = audio_chunk
            npBuffer = np.array(buffer, dtype=np.int32)
            # Calculate the energy or use the peak indices as an indicator
            squared = np.square(npBuffer)
            meaned = np.mean(squared)
            rms = np.sqrt(meaned)
            energy = rms
            # print(energy)

            if len(self.whiteNoiseBuffer) < self.WHITENOISEBUFFERSIZE:
            # if len(whiteNoiseBuffer) < WHITENOISEBUFFERSIZE * 3:
                # print("FILLING WHITENOISE BUFFER")
                self.whiteNoiseBuffer.append(energy)
                # plt.axvline(x=(i + CHUNK_SIZE) / sample_rate / nchannels, color="g")
            elif self.whiteNoiseEnergy is None:
                self.whiteNoiseEnergy = np.mean(self.whiteNoiseBuffer)
                print(f"White Noise energy calculated: {self.whiteNoiseEnergy}")

            if self.whiteNoiseEnergy is not None:
                # print("HERE")
                if energy <= self.whiteNoiseEnergy:
                    # print("SILENCE DETECTED!")
                    self.silenceBuffer.append(energy)
                    self.non_silence_count = 0
                elif len(self.silenceBuffer) > 0 and energy > self.whiteNoiseEnergy:
                    self.non_silence_count += 1

                if self.non_silence_count == 5:
                    self.silenceBuffer.clear()
                    self.non_silence_count = 0
                    # print("SILENCE BUFFER CLEARED!")


                if len(self.silenceBuffer) == self.WHITENOISEBUFFERSIZE // 2 and self.wordFlag:
                    print("PERIOD DETECTED!")
                    # plt.axvline(x=(CHUNK_SIZE) / RATE / nchannels, color="orange")
                    self.silenceBuffer.clear()
                    self.non_silence_count = 0
                    self.wordFlag = False
                    # self.GUI.incrementSentence_fn()
                    # self.GUI.decrementSentence_fn()
                    

            #this is just for plotting of the graph
            self.energyGraphy.append(energy)
            self.energyGraphx.append(buffer / self.RATE / self.nchannels)

            # I want to check the past 3 values, if the middle value is higher than both the values before and after, increment word by one
            ## First get the past 3 values
            if len(self.energyGraphy) >= 5:

                latestValue = energy
                secondLastValue = self.energyGraphy[-2]
                middleValue = self.energyGraphy[-3]
                secondValue = self.energyGraphy[-4]
                firstValue = self.energyGraphy[-5]

                if secondLastValue > latestValue and secondValue > firstValue and middleValue > secondValue and middleValue > secondLastValue and middleValue >= self.ENERGY_THRESHOLD:
                    self.wordCount += 1
                    if not self.wordFlag:
                        self.wordFlag = True
                    print(f"CURRENT WORD COUNT: {self.wordCount}")
                    # self.GUI.incrementWord_fn()
                    


# audioAnalyser = AudioAnalyser()
# audioAnalyser.start()


