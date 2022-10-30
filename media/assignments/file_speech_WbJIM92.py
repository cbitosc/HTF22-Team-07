import pandas as pd
import re
#chat_file =open("WhatsApp_chat.txt")
from pandas import DataFrame as df
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
emoji_key = df(pd.read_csv('WhatsApp', encoding='utf-8', index_col=0))
engine.setProperty('voice', voices[1].id)
print(emoji_key.iloc[:,0])
engine.say(emoji_key)
engine.runAndWait()