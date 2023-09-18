import wave
import numpy as np


def read_audio(file_path):
    wf = wave.open(file_path, "rb")
    data = wf.readframes(-1)
    nchannels = wf.getnchannels()
    sample_rate = wf.getframerate()

    audio_data = np.frombuffer(data, dtype=np.int16)
    return audio_data, sample_rate, nchannels

    # if wf.getnchannels() == 1:
    #     audio_data = np.frombuffer(data, dtype=np.int16)
    # else: #when there are 2 channels
    #     data_per_channel = [data[offset::nchannels] for offset in range(nchannels)]
    #     left_channel, right_channel = data_per_channel[0], data_per_channel[1]
    #     print(type(left_channel))
    #     audio_data = np.frombuffer(
    #         right_channel, dtype=np.int16
    #     )  # for some reason the left channel has very weird noise?
    # return audio_data, sample_rate
