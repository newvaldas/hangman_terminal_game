import string

def load_file(file_path: str) -> list:
        random_words = []
        f = open(file_path, "r")
        for x in f:
            random_words.append(x.strip("\n"))
        f.close()
        return random_words
        
def mask_word(word:str) -> str:
        masked_word = ""
        for character in word:
            if(character != " "):
                masked_word = masked_word + "*"
            else:
                masked_word = masked_word + " "
        return masked_word  

def select_letter(letters: list) -> tuple:
    while True:
        l = input("Choose Letter: ")
        if l in letters:
            return (letters.index(l), l)
        print("Letter not in the list! Try again!")

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

def reduce_health(health:int, found:int) -> int:
        if(found == 0):
            health -= 1
            
        return health

def print_letters(letters: list) -> None:
    print("Available Letters:")
    print("|" + "|".join(letters) + "|")
        
def print_info(masked_word:str, health:int) -> str:
        print("Health: " + "❤" * health)
        print("Word: " + masked_word)
        
def check_game_over(masked_word:str, health:int) -> int:
        game_over = 0
        if(health == 0 or masked_word.find("*" ) == -1):
            game_over = 1
        return game_over 