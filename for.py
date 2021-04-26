#Program to count number of vowels and consonants in a word

#Initiate the Vowel word count by 0
Vowels = 0

#Initiate the Consonant word count by 0
Consonants = 0

#Request for User Word/Phrase input
vowel_consonant = input("Enter Phrases: ")

#Loop through each letter in the phrases/words inputed by the user using a For Loop
for letter in vowel_consonant:

    #Check each letter if it contains the specified letters for Vowels and change them to lower case 
    if letter.lower() in 'aoui':

        #Once the a Vowel letter if found increasement by 1
        Vowels = Vowels + 1

    #And if the character found is a space them there should be no count (pass without counting)
    elif letter.lower() == ' ':
        pass
    else:

        #And if the characters found are not Vowels nor spaces them increasement Consonant by 1
        Consonants = Consonants+1

#Count the number of Vowel characters
print(f'There are {Vowels} Vowels in {vowel_consonant}')

#Count the number of Consonant characters
print(f'And There are {Consonants} Consonants in {vowel_consonant}')

