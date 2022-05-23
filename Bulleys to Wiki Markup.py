#Adds Wikipedia bullets points to the start of each line of text on the clipboard

#
from cgitb import text
import pyperclip
text = pyperclip.paste()

lines= text.split('\n')

for i in range(len(lines)):
    lines[i]='* ' + lines[i]
    print(lines[i])

text= '\n'.join(text)

pyperclip.copy(text)

