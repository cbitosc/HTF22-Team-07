# Import the required module for text
# to speech conversion

# This module is imported so that we can
# play the converted audio
import os
import gtts
from playsound import playsound
# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gtts.gTTS(text=mytext, lang='fr', slow=False)

# Saving the converted audio in a mp3 file named
# welcome
tts = gtts.gTTS("Hello world 😍👌😘💕",lang="fr")
tts.save("hello.mp3")
# Playing the converted file
playsound("hello.mp3")
