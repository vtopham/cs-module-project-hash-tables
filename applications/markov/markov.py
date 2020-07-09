import random
import re

# Read in all the words in one go
with open("input.txt") as f:
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
    
    # print(newWords)

   



# TODO: analyze which words can follow other words
# Your code here
 #create hash table
    lookup = {}
    for i in range(len(newWords) - 1):
        cur = newWords[i]
        if lookup.get(cur) == None:
            lookup[cur] = []
        # print(f"Adding {newWords[i + 1]} as following {cur}")
        lookup[cur].append(newWords[i + 1]) 


# TODO: construct 5 random sentences
# Your code here
    for x in range(5):
        print(f"Sentence {x}:")
        sentence = ""
        curWord = random.choice(list(lookup))
        for w in range(random.randint(5,20)):
            sentence += curWord
            sentence += " "
            options = lookup[curWord]
            curWord = random.choice(options)
        print(sentence[:-1] + ".")
            


        

