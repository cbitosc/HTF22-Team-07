import demoji
import re
text="Hehe 🤣🤣😁 very funny😂"
r=(demoji.findall(text))
x=list(r.keys())
y=list(r.values())
for i in range(len(r)):
   text=re.sub(x[i],' emoji '+ y[i],text)
print(text)