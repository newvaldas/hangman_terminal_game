import numpy as np
import string
import time
import logging
from game_functions import *


logging.basicConfig(filename="hangman.log", encoding="UTF-8",
level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# -------------------------main game loop----------------------------------

file_path = "dictionary.txt"
random_words = load_file(file_path)

letters = list(string.ascii_lowercase)

index = np.random.randint(len(random_words))

word = random_words[index].lower() #<- make and upper

masked_word = mask_word(word)

health = 10

game_over = 0

name = input("Enter you name: ")

print (f"=============Welcome to the Hangman game!============\n")
time.sleep(1.5)
print (f"================={name} ,Good luck!=====================\n")

logging.info("Starting game")
while(not game_over):
  
    print_info(masked_word, health)
   
    print_letters(letters)
   
    logging.info(f"Player {name} selecting letter")
    (i,l) = select_letter(letters)
    logging.info(f"Player {name} selected letter: %s", l)
    
    letters.pop(i)
   
    [masked_word,found] = update_mask(masked_word, word, l)
  
    health = reduce_health(health, found)
    logging.info(f"Player has left {health} lives")
    
    game_over = check_game_over(masked_word, health)
    print("---------------------------------------")
    
    logging.info("Ending game")

if(health > 0):
    
    print("You Won!")
else:
    
    print("You Lost!")
print("The word was: ",(word.upper())) 



    