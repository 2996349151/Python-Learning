import re

"""words extraction"""

text = re.split(" |,|!|\.|\?", input())
for each in text:
    if each == "":
        text.remove("")
print(text)
