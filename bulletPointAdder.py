#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on 
# the clipboard

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for index, line in enumerate(lines):
	lines[index] = '* ' + line

pyperclip.copy("\n".join(lines))