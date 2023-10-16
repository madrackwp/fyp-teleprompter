import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load an audio file
audio_file = "/Users/wpgoh/Documents/fyp-teleprompter/2023-10-14_16-13-26 copy.wav"

# Recognize the speech and obtain timestamps
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Record the entire audio file
    try:
        results = recognizer.recognize_google(audio_data, show_all=True)
        print(results)
        # Process recognized words and timestamps
        # for alternative in results['alternative']:
        #     transcript = alternative['transcript']
        #     timestamps = alternative['timestamps']
            
        #     print("Transcription: " + transcript)
        #     print("Word Timestamps:")
        #     for word, start, end in timestamps:
        #         print(f"{word}: {start} - {end}")
                
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))