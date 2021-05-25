#Get Sentence from user
original_words = input("Please Enter some Phrases: ").strip().lower()

#Slipt the origin words using the split method
words = original_words.split()

#create an empty list for saving the new words
new_words = []

#Loop throught the split words
for word in words:
    #check the first character of the word if it contains vowels the add 'yay' to it
    if word[0] in "aeoui":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        #Set the vowel position to 0
        vowel_pos = 0
        #Loop through the word again
        for letter in word:
            #Check the word 1st index again if it does not contain vowels
            if letter not in "aeoui":
                #Move the vowel position by 1
                vowel_pos = vowel_pos + 1
            else:
                break
        con = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        real_word = the_rest + con + "ay"
        new_words.append(real_word)
out_put = " ".join(new_words)

print(out_put)


