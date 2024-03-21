import random

#The player starts with nine lives
lives=9

#Make a list of words that we want to use in the game. Each item in the list is a word with five characters
words=['pizza','teeth','fairy','shirt','otter','plane']

#Pick a word from wordlist at random.
secret_word = random.choice(words)

#Tell the user what the game is - no special characters, only letters
#Make another list with '?'. Every ? represents one letter-secretword
clue=list('?????')

heart_symbol = '\u2764\uFE0F'
guessed_word_correctly = False

def update_clue(guessed_letter,secret_word,clue):
#Guessed_letter = i, secret_word = pizza, clue = ?????
  index=0
  while index < len(secret_word):
    if guessed_letter == secret_word[index]:
      clue[index] = guessed_letter
      index = index + 1
        
while lives > 0:
  print(clue)
  print('Lives left:', heart_symbol, lives)
  #Ask the player to guess the letter
  guess=input('guess a letter or the whole word: ')
  
  if guess == secret_word:
    #When the word is guessed correctly, this will break out of the loop
    guessed_word_correctly = True
    break

  if guess in secret_word:
    update_clue(guess,secret_word, clue)
            
  else:
    #check wheter guessletter is part of secretword, if no, subtract a life
    print('Incorrect. You lost a life')
    lives = lives-1
    
#Tell the player if they are correct or not
#continue this loop until either the word is guessed by player or all nine lives are lost
if guessed_word_correctly:
    print('You won! the secret word was ',secret_word)

else:
    print('You lost! The secret word was ',secret_word)
