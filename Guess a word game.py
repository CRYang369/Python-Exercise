'''
Guesss a word or alphabet

'''

import random

lives=3

words=['pizza','fairy','teeth','shirt','otter','plane']
secret_word=random.choice(words)
print(secret_word)

clue=list('?????')
heart_symbol=u'\u2764'
guess_word_correctly=False

'''
Update the clue: 
The location/index of the alphabet in the word list to be guessed upon the secret word produced randomly 
'''
def update_clue(guessed_letter,secret_word,clue):
    index=0
    while index < len(secret_word):
        if guessed_letter==secret_word[index]:
            clue[index]=guessed_letter
        index=index+1
while lives>0:
    print(clue)
    print('left number of live'+heart_symbol*lives)
    guess=input('Guess alphabet or the whole word:')

    if guess==secret_word:
        guess_word_correctly=True
        break
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('Wrong,you lose one of your lives\n')
        lives=lives-1
if guess_word_correctly:
    print('You win!The secret word is '+ secret_word)
else:
    print('You lost!The secret word is '+ secret_word)



