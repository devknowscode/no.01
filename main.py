from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import webbrowser as wb
import wikipedia
import wolframalpha

# Initialize the recognizer
voices = []
engine = None
activationWord = 'echo'
try:
    engine = pyttsx3.init()
except ImportError:
    print('Import Error: pyttsx3')
except RuntimeError:
    print('Runtime Error: pyttsx3')

if engine is not None:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
else:
    print('Error: No voices found')


def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand():
    listener = sr.Recognizer()
    print('Listening...')

    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source, duration=1)
        listener.pause_threshold = 1
        input_speech = listener.listen(source)

    try:
        print('Recognizing...')
        query = listener.recognize_google(input_speech, language='en-in')
        print(f'User said: {query}\n')
    except Exception as exception:
        print('Please say that again...')
        print(exception)
        return 'None'

    return query


# Main loop
if __name__ == '__main__':
    speak('Hello, I am Echo. How can I help you?')

    while True:
        # Parse as a list of words
        query = parseCommand().lower().split()
        
        if query[0] == activationWord:
            query.pop(0)

            # List command
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Hello, I am Echo. How can I help you?')
                else:
                    query.pop(0)  # Remove say
                    speech = ''.join(query)
                    speak(speech)
