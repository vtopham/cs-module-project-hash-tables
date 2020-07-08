import re

def word_count(s):

    # Your code here
    # words = s.split(' |\n|\r', s)
    words = re.split(' |\n|\r|\t', s)
    to_remove = [ "\"", ':', ';', ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"]
    
    count = {}
    
    for word in words:
        for char in to_remove:
            word = word.replace(char, "")
        word = word.lower()
        #Now add the cleaned word to the count
        
        if word != "":
            if count.get(word) == None:
                count[word] = 1
            else:
                count[word] = count[word] + 1
    print(count)
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))