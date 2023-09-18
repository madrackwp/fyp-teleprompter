from pydub import AudioSegment
from pydub.playback import play

# Audiofiles are from https://www.kaggle.com/datasets/pavanelisetty/sample-audio-files-for-speech-recognition?resource=download


# Load the WAV file
def split(audio_input, audio_output):
    audio = AudioSegment.from_wav(audio_input)
    # audio = AudioSegment.from_wav("audiofiles/processed/output_segment_0.wav")
    output_dir = audio_output
    # output_dir = "audiofiles/output_segment_0_split"
    output_filename = "segment"

    # Define the segment start and end times in milliseconds
    segment_start_times = [
        1280,  # The
        1500,  # stale
        1880,  # smell
        2350,  # of
        2400,  # old
        2830,  # beer
        3120,  # lingers
    ]  # Example: split every 10 seconds
    segment_end_times = [1500, 1880, 2350, 2400, 2830, 3120, 3760]

    # Split the audio into segments
    segments = [
        audio[start:end] for start, end in zip(segment_start_times, segment_end_times)
    ]

    # Export each segment as a separate WAV file
    for i, segment in enumerate(segments):
        segment.export(f"{output_dir}/{output_filename}_{i}.wav", format="wav")
    print("AUDIO SPLIT!")
    # Play the first segment as an example
    # play(segments[4])


input = "audiofiles/processed/output_segment_0.wav"
output = "audiofiles/output_segment_0_split"
split(input, output)
