# Your code here
import re
with open("robin.txt") as f:
    words = f.read()

newWords = []

words = re.split(' |\n|\r|\t', words)
to_remove = [ "\"", ':', ';', "?", ",", ".", "!", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]

for word in words:
    #clean the words
    for char in to_remove:
        word = word.replace(char, "")
    word = word.lower()
    if word != "":
        newWords.append(word)

#use a hash table to track occurance
#Also track length of longest word

tracking = {}
length = 0

for word in newWords:
    if tracking.get(word) == None:
        if len(word) > length:
            length = len(word)
        tracking[word] = 1
    else:
        tracking[word] += 1

#now we have a table of values

bufferLength = length + 2

#Create an ordered list to print out

def get_val(key):
    return tracking[key]
sorted_tracking = sorted(tracking)
sorted_tracking = sorted(sorted_tracking, key=get_val, reverse = True)

for word in sorted_tracking:
    string = word
    for s in range(bufferLength - len(word)):
        string += " "
    for h in range(tracking[word]):
        string += "#"
    print(string)
    


