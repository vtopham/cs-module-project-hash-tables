# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

with open("ciphertext.txt") as f:
    text = f.read()

#create a hash table of frequencies

freq = {}
for char in text:
    if char != "." and char != "\n" and char != "1" and char != ")" and char != "(\n)" and char != "\"" and char != "(" and char != ";" and char != "-" and char != "," and char != "'" and char != " " and char != "—" and char != ":"  and char != "!"and char != "?":
        if freq.get(char) == None:
            freq[char] = 1
        else:
            freq[char] += 1

#now turn it into an actual frequency

for char in list(freq):
    freq[char] = freq[char] / len(text)

#sort by frequency
def get_freq(key):
    return freq[key]

sorted_freq = sorted(freq, key = get_freq, reverse = True)

ordered_letters = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

cypher = {}

for l in range(26):
    cypher[sorted_freq[l]] = ordered_letters[l]



final = ""
for char in text:
    if cypher.get(char) == None:
        final += char
    else:
        final += cypher[char]

print(final)
