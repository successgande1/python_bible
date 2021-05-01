#Get Sentence from User
original = input("Please Enter a Sentence: ").strip().lower()

#Split the sentence to Words using the split method
words = original.split()


#Loop through the words in the sentence and convert to pig latin
new_word = []

for word in words:
    #check if the first letter of the word is a vowel
    if word[0] in 'aeiou':
        new_words = word + 'yay'
        new_word.append(new_words)
    else:
        #Set Vowel Position
        vowel_pos = 0
        #Loop through each letters in the word and know the index where it turns to vowel
        for letter in word:
            #Check for consonant position and continue if not found
            if letter not in 'aeiou':
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_words = the_rest + cons + 'ay'
        new_word.append(new_words)


#print(new_word)



#stick the words together by using the join() string method
output = " ".join(new_word)

#Output the Sentence
print(output)