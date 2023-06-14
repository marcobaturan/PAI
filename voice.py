import pyttsx3
import os
from functions import read_file


def load_voice_configuration(text):
    """Load voice configuration.

        It is a module which function is to read the configuration file and load
        the params for generating the voice of the chatbot.

    """
    file_path = 'configuration.mem'
    # Example usage
    if os.path.isfile(file_path):

        start_line = 15
        end_line = 19
        lines = read_file(start_line, end_line, file_path)
        rate = lines[0]
        volume = lines[1]
        language = lines[3]

        engine = pyttsx3.init()
        # rate need a integer to work properly
        engine.setProperty('rate', int(rate))
        engine.setProperty('voice', language)
        engine.setProperty('volume', volume)

        # It's just a text to speech function.
        def say_something(somethingToSay):
            engine.say(somethingToSay)
            engine.runAndWait()
            engine.stop()
        say_something(text)


