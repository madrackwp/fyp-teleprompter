import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout, QLineEdit,QLabel, QPushButton, QFileDialog
from text import ReadText, UnreadText
# from PySide6.QtGui import QPalette, QColor
from AudioAnalysis import AudioAnalyser

# class Color(QWidget):

#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)

#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.teleprompterAudio = AudioAnalyser()
        print("CREATED AUDIO ANALYSER INSTANCE")
        self.setWindowTitle("Teleprompter")
        self.script = ""
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        scrollingButtonLayout = QHBoxLayout()
        script = "The sun dipped below the horizon, casting a warm, golden glow across the tranquil sea. Gentle waves lapped at the sandy shore, creating a soothing melody that harmonized with the chirping of distant birds. As the stars began to twinkle in the darkening sky, a sense of serenity washed over those fortunate enough to witness this serene moment of nature's beauty."

        self.readText = ReadText()
        self.unreadText = UnreadText(script)
        self.readText.format()
        self.unreadText.format()

        self.teleprompterScreen = QLabel()
        self.teleprompterScreen.setText(self.readText.format() + self.unreadText.format())
        self.teleprompterScreen.setMinimumSize(400,500)
        self.teleprompterScreen.setStyleSheet("background-color: yellow;color: black; padding: 10px;")
        self.teleprompterScreen.setWordWrap(True)
        # teleprompterScreen.setBack
        layout3.addWidget(self.teleprompterScreen)


        self.inputBox = QLineEdit()
        layout2.addWidget(self.inputBox)

        addButton = QPushButton()
        addButton.setText("Upload Script")
        addButton.clicked.connect(self.uploadScriptHandler)
        layout2.addWidget(addButton)

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
        incrementSentenceButton.clicked.connect(self.incrementSentence_fn)

        decrementSentenceButton = QPushButton()
        decrementSentenceButton.setText("<<")
        decrementSentenceButton.clicked.connect(self.decrementSentence_fn)

        scrollingButtonLayout.addWidget(decrementSentenceButton)
        scrollingButtonLayout.addWidget(decrementWordButton)
        scrollingButtonLayout.addWidget(incrementWordButton)
        scrollingButtonLayout.addWidget(incrementSentenceButton)
        layout2.addLayout(scrollingButtonLayout)

        startStopLayout = QHBoxLayout()
        startButton = QPushButton()
        startButton.setText("Start")
        startButton.clicked.connect(self.startTeleprompter)

        stopButton = QPushButton()
        stopButton.setText("Stop")

        startStopLayout.addWidget(startButton)
        startStopLayout.addWidget(stopButton)

        layout2.addLayout(startStopLayout)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    
    def uploadScriptHandler(self):
        self.script = self.inputBox.text()
        print(self.script)
        self.teleprompterScreen.setText(self.script)

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
        # print(sentence)
        self.readText.addSentence(sentence)
        self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())

    def decrementSentence_fn(self):
        # print("Trying to decrement word")
        sentence = self.readText.removeSentence()
        # print(sentence)
        self.unreadText.addSentence(sentence)
        self.teleprompterScreen.setText(self.readText.format()+self.unreadText.format())
        
    def startTeleprompter(self):
        print("Starting teleprompter")
        self.teleprompterAudio.start()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()