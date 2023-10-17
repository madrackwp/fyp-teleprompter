import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit,QLabel, QPushButton, QFileDialog, QScrollArea, QSizePolicy
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, Signal, QObject, QThreadPool, Qt

import matplotlib.pyplot as plt
from datetime import datetime

from text import ReadText, UnreadText
# from gui import MainWindow
from PySide6.QtCore import QRunnable, Slot, Signal, QObject, QTimer, QThreadPool
import traceback
import time
import pyaudio
import numpy as np
import os
import wave
import json


class WorkerSignals(QObject):
    finished = Signal()
    incrementWord = Signal(bool)
    incrementSentence = Signal(bool)
    result = Signal(list, list, list, list)
    error = Signal(tuple)
    # progress = Signal(int)
    
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn #callback function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()


        #This worker function will take a 'progess_callback' argument
        # Add the callback to our kwargs
        # self.kwargs['increment_word_callback'] = self.signals.progress #This is saying that increment_word_callback should use the signals.progress 
        self.kwargs['increment_word_callback'] = self.signals.incrementWord #This is saying that increment_word_callback
        self.kwargs['increment_sentence_callback'] = self.signals.incrementSentence
    @Slot()
    def run(self):
        try:
            xArray, yArray, wordCountTiming, periodCountTiming = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(xArray, yArray, wordCountTiming, periodCountTiming)
        finally:
            self.signals.finished.emit()
    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.teleprompterAudio = AudioAnalyser()
        print("CREATED AUDIO ANALYSER INSTANCE")
        self.wordCount = 0
        self.periodCount = 0

        self.RECORDING = False
        self.INFORMATION_SCREEN_TEXTS = {
            "welcome": "Use the arrow keys to jump forward\nUpload your own scripts as a .txt files or type it in directly in the box below!",
            "end" : "You have reached the end of your script",
            "start" : "You have reached the start of your script",
            "recording": "You may now speak!",
            "restart": "Click start to restart!"
        }

        self.setWindowTitle("Teleprompter")
        self.script = ""
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        scrollingButtonLayout = QHBoxLayout()
        # script = "In a cozy cottage in the forest, a cat named Whiskers sat by the window. The aroma of freshly baked bread filled the room, creating a warm and inviting atmosphere. It was a perfect moment to curl up by the fireplace with a book and forget about the world outside."
        # script = "The cat sat on the mat. It saw a big bug. It ran and hid. The dog barked. "
        script = "The extraordinary, magnificent landscape stretched endlessly before us, with the sun casting a brilliant, luminous glow over the picturesque, snow-capped mountains."


        self.readText = ReadText()
        self.unreadText = UnreadText(script)
        self.readText.format()
        self.unreadText.format()

        self.teleprompterContainer = QScrollArea()
        
        
        self.teleprompterScreen = QLabel()
        self.teleprompterScreen.setText(self.readText.format() + self.unreadText.format())
        # self.teleprompterScreen.setMinimumSize(400,500)
        self.teleprompterScreenWrapper = QVBoxLayout()

        self.teleprompterScreenWrapper.addWidget(self.teleprompterScreen)

        self.teleprompterScreen.setStyleSheet("background-color: yellow;color: black; padding: 10px;")
        self.teleprompterScreen.setWordWrap(True)
        # teleprompterScreen.setBack
        self.teleprompterWidget = QWidget()
        # self.teleprompterContainer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Set the size policy to Expanding
        self.teleprompterWidget.setLayout(self.teleprompterScreenWrapper)

        self.teleprompterContainer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.teleprompterContainer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.teleprompterContainer.setWidgetResizable(True)
        self.teleprompterContainer.setWidget(self.teleprompterWidget)

        layout3.addWidget(self.teleprompterContainer, 2)

        self.informationDisplay = QLabel()
        self.informationDisplay.setText(self.INFORMATION_SCREEN_TEXTS["welcome"])
        layout2.addWidget(self.informationDisplay)

        self.inputBox = QLineEdit()
        layout2.addWidget(self.inputBox)
        self.inputBox.setPlaceholderText("Type or paste your script here!")

        uploadButton = QPushButton()
        uploadButton.setText("Upload Script")
        uploadButton.clicked.connect(self.uploadScriptHandler)
        layout2.addWidget(uploadButton)

        fileUploadButton = QPushButton()
        fileUploadButton.setText("Upload from computer")
        fileUploadButton.clicked.connect(self.open_file_dialog)
        layout2.addWidget(fileUploadButton)

        incrementWordButton = QPushButton()
        incrementWordButton.setText(">")
        incrementWordButton.clicked.connect(self.incrementWord_fn)

        decrementWordButton = QPushButton()
        decrementWordButton.setText("<")
        decrementWordButton.clicked.connect(self.decrementWord_fn)

        incrementSentenceButton = QPushButton()
        incrementSentenceButton.setText(">>")
        incrementSentenceButton.clicked.connect(self.incrementSentenceManual_fn)

        decrementSentenceButton = QPushButton()
        decrementSentenceButton.setText("<<")
        decrementSentenceButton.clicked.connect(self.decrementSentence_fn)

        scrollingButtonLayout.addWidget(decrementSentenceButton)
        scrollingButtonLayout.addWidget(decrementWordButton)
        scrollingButtonLayout.addWidget(incrementWordButton)
        scrollingButtonLayout.addWidget(incrementSentenceButton)
        layout2.addLayout(scrollingButtonLayout)


        
        debuggingLayout = QHBoxLayout()
        self.wordCounterDisplay = QLabel(f"Word Count: {self.wordCount}")
        self.periodCounterDisplay = QLabel(f"Period Counter: {self.periodCount}")
        debuggingLayout.addWidget(self.wordCounterDisplay)
        debuggingLayout.addWidget(self.periodCounterDisplay)
        layout2.addLayout(debuggingLayout)


        startStopLayout = QHBoxLayout()
        startButton = QPushButton()
        startButton.setText("Start")
        startButton.clicked.connect(self.startTeleprompter)

        stopButton = QPushButton()
        stopButton.setText("Stop")
        stopButton.clicked.connect(self.thread_completion)
        
        startStopLayout.addWidget(startButton)
        startStopLayout.addWidget(stopButton)

        layout2.addLayout(startStopLayout)

        layout1.addLayout(layout2,1)
        layout1.addLayout(layout3, 2)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    
    def audioAnalysis(self, increment_word_callback, increment_sentence_callback):
        self.CHUNK =  1024 * 2# Number of frames per buffer
        self.ENERGY_THRESHOLD = 1500 #this is the RMS value threshold 
        self.FORMAT = pyaudio.paInt16  # Format for audio input
        self.CHANNELS = 1  
        self.RATE = 44100  # Sample rate (samples per second)
        self.nchannels = 1
        self.elapsedTime = 0
 
        self.wordFlag = False

        self.WHITENOISEBUFFERSIZE = 56 // 2
        # self.CHUNK_SIZE = 35280 // 2

        self.whiteNoiseBuffer = []
        self.energyGraphx, self.energyGraphy = [], []

        self.whiteNoiseEnergy = None
        self.non_silence_count = 0

        self.silenceBuffer = []

        self.audio = pyaudio.PyAudio()

        self.audioDataY = []
        self.audioDataX = []
        self.wordCountTimings =[]
        self.periodCountTimings = []

        self.ROLLING_BUFFER_SIZE = 44100  # Adjust as needed, should be larger than CHUNK_SIZE
        # self.audio_data = np.zeros(self.ROLLING_BUFFER_SIZE // 2, dtype=np.int16)

        print("Starting the teleprompter")
        self.RECORDING = True
        start_time = time.time()
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)
        while self.RECORDING:
            
            audio_chunk = np.frombuffer(self.stream.read(self.CHUNK), dtype=np.int16)
            self.audioDataY.extend(audio_chunk)

            # Add the new audio chunk to the rolling buffer
            # self.audio_data = np.roll(self.audio_data, -len(audio_chunk))
            # self.audio_data[-len(audio_chunk):] = audio_chunk

            buffer = audio_chunk
            npBuffer = np.array(buffer, dtype=np.int32)
            # Calculate the energy or use the peak indices as an indicator
            squared = np.square(npBuffer)
            meaned = np.mean(squared)
            rms = np.sqrt(meaned)
            energy = rms
            # print(energy)

            if len(self.whiteNoiseBuffer) < self.WHITENOISEBUFFERSIZE:

                self.whiteNoiseBuffer.append(energy)
            elif self.whiteNoiseEnergy is None:
                self.whiteNoiseEnergy = np.mean(self.whiteNoiseBuffer)
                print(f"White Noise energy calculated: {self.whiteNoiseEnergy}")

            if self.whiteNoiseEnergy is not None:
                if energy <= self.whiteNoiseEnergy:
                    self.silenceBuffer.append(energy)
                    self.non_silence_count = 0
                elif len(self.silenceBuffer) > 0 and energy > self.whiteNoiseEnergy:
                    self.non_silence_count += 1

                if self.non_silence_count == 5:
                    self.silenceBuffer.clear()
                    self.non_silence_count = 0


                if len(self.silenceBuffer) == self.WHITENOISEBUFFERSIZE // 2 and self.wordFlag:
                    period_curr_time = time.time()
                    self.periodCountTimings.append(period_curr_time-start_time)
                    print("PERIOD DETECTED!")
                    self.periodCount += 1
                    self.periodCounterDisplay.setText(f"Period Counter: {self.periodCount}")
                    self.silenceBuffer.clear()
                    self.non_silence_count = 0
                    self.wordFlag = False
                    increment_sentence_callback.emit(True)

                    

            #this is just for plotting of the graph
            self.energyGraphy.append(energy)
            # self.elapsedTime 
            self.energyGraphx.append(self.elapsedTime)
            self.elapsedTime += self.CHUNK / self.RATE / self.nchannels
            # self.energyGraphx.append(self.CHUNK / self.RATE / self.nchannels)

            # I want to check the past 3 values, if the middle value is higher than both the values before and after, increment word by one
            ## First get the past 3 values
            if len(self.energyGraphy) >= 5:

                latestValue = energy
                secondLastValue = self.energyGraphy[-2]
                middleValue = self.energyGraphy[-3]
                secondValue = self.energyGraphy[-4]
                firstValue = self.energyGraphy[-5]

                if secondLastValue > latestValue and secondValue > firstValue and middleValue > secondValue and middleValue > secondLastValue and middleValue >= self.ENERGY_THRESHOLD:
                    wordCount_time = time.time()
                    self.wordCountTimings.append(wordCount_time - start_time)
                    self.wordCount += 1
                    increment_word_callback.emit(True)
                    self.wordCounterDisplay.setText(f"Word Count: {self.wordCount}")
                    if not self.wordFlag:
                        self.wordFlag = True
                    print(f"CURRENT WORD COUNT: {self.wordCount}")
                    # self.GUI.incrementWord_fn()
        # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # plt.plot(self.energyGraphx, self.energyGraphy)
        # plt.xlabel("Time")
        # plt.ylabel("Energy")
        # plt.savefig(f"/results/{timestamp}")
        # print(self.energyGraphx)
        # print(self.energyGraphy)
        self.audioDataX = []
        for index, data in enumerate(self.energyGraphx):
            for i in range(index*self.CHUNK, (index+1)*self.CHUNK):
                self.audioDataX.append((index+i)/self.RATE/self.CHANNELS)

        # return self.energyGraphx, self.energyGraphy
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        print(len(self.audioDataX))
        return self.audioDataX, self.audioDataY, self.wordCountTimings, self.periodCountTimings
    
    def print_output(self,s):
        print(s)

    def thread_completion(self):
        self.RECORDING = False
        self.informationDisplay.setText(self.INFORMATION_SCREEN_TEXTS["restart"])
        print("YOU ARE DONE!")
    
    def startTeleprompter(self):
        print("CREATING A NEW WORKER!")
        self.informationDisplay.setText(self.INFORMATION_SCREEN_TEXTS["recording"])
        worker = Worker(self.audioAnalysis)

        worker.signals.incrementWord.connect(self.incrementWord_fn)
        worker.signals.finished.connect(self.thread_completion)
        worker.signals.result.connect(self.saveLogs)
        worker.signals.incrementSentence.connect(self.incrementSentence_fn)

        self.threadpool.start(worker)

    def uploadScriptHandler(self):
        self.script = self.inputBox.text()
        self.unreadText = UnreadText(self.script)
        self.readText = ReadText()
        self.teleprompterScreen.setText(self.readText.format() + self.unreadText.format())
        
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            # Read the selected text file and display its content in the QLabel
            with open(file_path, "r") as file:
                file_content = file.read()
                # self.label.setText(file_content)
                self.script = file_content
                self.unreadText = UnreadText(self.script)
                self.readText = ReadText()
                self.teleprompterScreen.setText(self.readText.format() + self.unreadText.format())

    def incrementWord_fn(self):
        # print("Getting data!")
        print("TRYING TO INCREMENT WORD")
        word = self.unreadText.removeWord()
        # print(word)
        self.readText.addWord(word)
        self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())
    
    def decrementWord_fn(self):
        print("Trying to decrement word")
        word = self.readText.removeWord()
        # print(word)
        self.unreadText.addWord(word)
        self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())

    def incrementSentence_fn(self):
        # print("TRYING TO INCREMENT WORD")
        sentence = self.unreadText.removeSentence()
        print(sentence)
        if sentence is not None:
            self.readText.addSentence(sentence)
            self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())

    def incrementSentenceManual_fn(self):
        # print("TRYING TO INCREMENT WORD")
        sentence = self.unreadText.removeSentenceManual()
        print(sentence)
        if sentence is not None:
            self.readText.addSentence(sentence)
            self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())

    def decrementSentence_fn(self):
        # print("Trying to decrement word")
        sentence = self.readText.removeSentence()
        # print(sentence)
        self.unreadText.addSentence(sentence)
        self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())

    def saveLogs(self, xRAWArray, yRAWArray, wordCountTimings, periodCountTimings):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_directory = f"/Users/wpgoh/Documents/fyp-teleprompter/results/Long/{timestamp}"  
        # directory = "results"
        os.mkdir(output_directory)
        savepath = os.path.join(output_directory, f"{timestamp}.png")
        plt.plot(xRAWArray, yRAWArray)

        for timings in wordCountTimings:
            plt.axvline(x=timings, color='r', linestyle='--')
        for timings in periodCountTimings:
            plt.axvline(x=timings, color='g', linestyle='--')
            
        plt.xlabel("Time")
        plt.ylabel("RMS")

        # plt.show()
        plt.savefig(savepath, dpi = 300, format ="png")

        savepath = os.path.join(output_directory, f"{timestamp}.wav")
        with wave.open(savepath, "wb") as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(yRAWArray))    
        

        # logsData = {"timingData": xRAWArray, "audioData" : yRAWArray, "wordCountData": wordCountTimings, "periodCountData": periodCountTimings}

        # with open(f"{output_directory}/data.json", "w") as jsonFile:
        #     json.dump(logsData, jsonFile)
        
        # print(f"Logs saved to: {output_directory}")        
        np.savez(f"/Users/wpgoh/Documents/fyp-teleprompter/results/Long/{timestamp}/data.npz", xRAWArray = xRAWArray, yRAWArray = yRAWArray, wordCountTimings = wordCountTimings, periodCountTimings = periodCountTimings)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()    

if __name__ == "__main__":
    main()