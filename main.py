import numpy as np
import string
import time


def load_file(file_path: str) -> list:
        random_words = []
        f = open(file_path, "r")
        for x in f:
            random_words.append(x.strip("\n"))
        f.close()
        return random_words
        
def mask_word(word:str) -> str:
        masked_word=''
        for character in word:
            if(character != " "):
                masked_word = masked_word + "*"
            else:
                masked_word = masked_word + " "
        return masked_word  

def select_letter(letters:str) -> list:
        index = -1
        while(index == -1):
            l = input("Choose Letter: ")
            try:
                index = letters.index(l)
            except:
                print("Letter not in the list! Try again!")
        return [index,l]

def update_mask(masked_word:str, word:str, letter:str) -> list:
        found = 0
        new_masked_word = ""
        for i in range(len(word)):
            if(letter == word[i]):
                new_masked_word += letter
                found = 1
            else:
                new_masked_word += masked_word[i]
        if(found == 1):
            print("The selected letter is part of the word!")
        else:
            print("Wrong letter!")
        return [new_masked_word, found]

def reduce_health(health:int, found:int):
        if(found == 0):
            health -= 1
        return health

def print_letters(letters:str) -> str:
        print("Available Letters: ")
        s = "|"
        for l in letters:
            s = s + l + "|"
        print(s)
        
def print_info(masked_word:str, health:int) -> str:
        print("Health: " + "❤" * health)
        print("Word: " + masked_word)
        
def check_game_over(masked_word:str, health:int) -> int:
        game_over = 0
        if(health == 0 or masked_word.find("*" ) == -1):
            game_over = 1
        return game_over 
            
       

# -------------------------main game loop----------------------------------

file_path = "dictionary.txt"
  
random_words = load_file(file_path)

letters = list(string.ascii_lowercase)

index = np.random.randint(len(random_words))

word = random_words[index].lower()

masked_word = mask_word(word)

health = 10

game_over = 0

print ("========Welcome to the Hangman game!============\n")
time.sleep(1.5)
print ("=================Good luck!=====================\n")

while(not game_over):
  
    print_info(masked_word, health)
   
    print_letters(letters)
   
    [i,l] = select_letter(letters)
    
    letters.pop(i)
   
    [masked_word,found] = update_mask(masked_word, word, l)
  
    health = reduce_health(health, found)
    
    game_over = check_game_over(masked_word, health)
    print("-------------------")

if(health > 0):
    
    print("You Won!")
else:
    
    print("You Lost!")
print("The word was: ",(word.upper())) 



    