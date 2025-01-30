#input (Request Sentence)
sentence = input("Type in a Sentence ? ")
sentence_length = len(sentence)
#Display Sentence from the user
print(sentence)
#Split the sentence into a list
split_sentence = sentence.split(" ")
#Display the first character from the split
print(split_sentence[0])

#Selecting the 3 characters from the sentence
print(sentence[0:3])

#selecting last 3 characters of the sentence
print(sentence[-3:])

#resverse the sentence
print(sentence[::-1])

#Modify Sentence to Upper Cases
print(sentence.upper())

#Modify Sentence to Lower Cases
print(sentence.lower())

#Replace Spaces in sentence with "-"
print(sentence.replace(" ", "-"))