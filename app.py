""" Processing voice commands shouldn't run without an active drone connection and vice-versa - the app terminates if either fails.
"""

from vosk import Model, KaldiRecognizer
import pyaudio
from Mosquito import Mosquito
from utils.replace_misheards import replace_misheards
from utils.validate_command import validate_command
from utils.command_router import command_router
import os
import time

# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  "pip install {your_version.whl}"
# https://alphacephei.com/vosk/models

PATH_TO_VOSK = os.environ.get('PATH_TO_VOSK')
model = Model(PATH_TO_VOSK)
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()



def listener():
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    start_time = time.time()
    max_wait_time = 30
    total_time = 0
    while total_time < max_wait_time:
        total_time = time.time()-start_time
        try:
            stream.start_stream()
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                command = recognizer.Result()[14:-3] # Extracting pure command from voice recording object
                stream.close()
                return command
        except Exception as e:
            print(f"[ERROR] Couldn't take voice command. Details: {e}")
            raise SystemExit

    print(f"No commands heard for {max_wait_time}s, exiting the app.")
    return "exit"



def main():
    mosquito = Mosquito()
    while True:
        try:
            if mosquito.drone.is_flying == True:
                mosquito.keep_alive_turn()
            mosquito.check_temp_and_battery()
            print("[Listening...]")

            command_received = listener()
            filtered_command = replace_misheards(command_received)
            validated_command = validate_command(filtered_command)

            if validated_command != []:
                print(f'[--->] Recognized command: \"{" ".join(filtered_command)}\"')

            command_router(mosquito, validated_command)

        except KeyError:
            print("[END] The program has been closed.")
            raise SystemExit
        except Exception as e:
            print(f"[APP ERROR] Details: {e.__class__.__name__} / {e}")
            raise SystemExit



if __name__ == "__main__":
    main()
