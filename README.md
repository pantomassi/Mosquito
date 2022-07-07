# Mosquito
Mosquito is a voice-controlled app for flying Tello drones.
<br />
<br />
<br />
**CAUTION**\
Speech recognition is fun, but isn't effective comparing to key control. So is the project- it's fun, but not to be relied on if you need some serious live control over the drone. To keep the drone alive when no commands are sent to it, a 1-degree left/right movements are applied, which is practical, but may not be a good safety measure.
<br />
<br />

**WHAT IT DOES**\
The app covers basic operations you could reliably do with voice control - like one-direction moves (no send_rc_control though), turns, flips, taking screenshots and video streaming.
<br />
<br />

**TO DO & WHAT'S NOT WORKING** (yet?)
- Audio recognition part can be greatly improved. This is just a basic working setup I found as I have no knowledge in the sound recognition field. I reckon vosk configuration needs to be suited to the environment you'll be using it in, to your voice input device etc, but it worked with a headset and laptop mic for me. Accepting only a set of words by vosk would be a much better idea (if doable), but for now filtering invalid commands is done through replacement of known misheards and a later validation, so that Tello object doesn't need to throw errors when it's given unknown commands.
- I would make streaming video run on a separate thread - right now, enabling the stream effectively blocks out any speech recognition (thus any other drone commands) until you close the video stream window with a key.
- For some reason I couldn't run motoron/motoroff commands ('not found'), even though the firmware was updated. A commented-out piece of code is left in the command_router module to include them.
- Rapid changes in movement are not possible, as each command first requires audio recognition and then processing. Multiple commands cannot be chained in one go- the only idea I have is to pass multiple commands at once and have them separated and validated. But the longer a command is, the bigger the chance it won't be recognized correctly.
<br />

**HOW TO USE**
<br />
1) Connect the drone to your machine through wifi.  
2) Run the app and say the commands (check the instructions.txt for details).  
-The app will disconnect after consecutive 30s of no commands provided (technically, empty commands: "").  
-To rapidly stop the engines, say 'emergency'. [!] This will make your drone fall uncontrollably if it was in the air.  
-To stop the app, say 'exit'.  
<br />

**REQUIREMENTS** (apart from requirements.txt)
<br />
1) Grab your pyAudio .whl file here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio; "pip install {your_version.whl}" - not included in the requirements.txt file.
2) Once connected via wifi to the drone, your machine will be offline. Vosk is something you want to use in offline mode for speech recognition, but you need to download a model first: https://alphacephei.com/vosk/models; small-en-us should do.
