def no_dups(s):
    # Your code here
    lookup = {}
    output = []
    #separate into an array of words
    s = s.split(" ")
    #check to see if the word is in the lookup. if it isn't store it.
    #if it is, remove it from the array
    for word in s:
        if lookup.get(word) == None:
            lookup[word] = 1
            output.append(word)
    #return the array as a string
    output_string = ""
    for word in output:
        output_string += f" {word}"
    return output_string[1:]

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))