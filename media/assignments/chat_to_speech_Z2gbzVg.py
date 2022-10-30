import pandas as pd
import re
from pandas import DataFrame as df
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
emoji_key = df(pd.read_csv('WhatsApp_chat.txt', encoding='utf-8', index_col=0))
chat=((emoji_key.iloc[:,0]))
print(chat)
x=''
y=''
for i in range(len(chat)):
    s=str(chat[i])
    a=s[12:].split()
    if x=="":
        x=a[0]
        p1=1
    elif x==a[0]:
        p1=1
    elif y=="":
        y=a[0]
        p1=0 
    else :
        p1=0
    rx=" ".join(a[1:])
    engine.setProperty('voice', voices[p1].id)
    engine.say(rx)

engine.runAndWait()