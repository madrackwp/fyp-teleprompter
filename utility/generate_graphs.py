# import wave
import matplotlib.pyplot as plt
import numpy as np
import os
import read_audio as audio


# Load the WAV file
directory = "audiofiles/processed"
# wav_file = "audiofiles/processed/output_segment_0.wav"
graph_dir = "graphs/harvard"

def generate_graphs(audio_directory, graph_directory):
    files = os.listdir(audio_directory)
    for file in files:
        wav_file = os.path.join(directory, file)
        filename = file.split(".")
        savepath = f"{graph_directory}/{filename[0]}.png"

        audio_data, sample_rate, nchannels = audio.read_audio(wav_file)
        print(len(audio_data))
        # print(audio_data)
        time_axis = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))

        plt.figure(figsize=(10, 5))
        plt.plot(time_axis, audio_data, color="b")
        plt.title(f"Audio Wave: {filename[0]}")
        # plt.title(f"{filename[0]}")
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.grid(True)
        # plt.show()

        plt.savefig(savepath, dpi=300, format="png")


generate_graphs(directory, graph_dir)
