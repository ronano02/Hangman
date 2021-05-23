import random

wordList = ['pineapple', 'orange', 'cherry', 'watermelon', 'dragonfruit', 'kiwi', 'onion', 'rockmelon']

print("""Welcome to hangman
A randomised word will be picked once the game starts
Type 'Play' to start \n""")
play = input("").lower()

while play != "play":
    play = input("").lower()

while (player := int(input("Enter either 1 or 2 players: "))) not in [1,2]:
    pass
if player == 1:
    word = random.choice(wordList)
else:
    word = input("Enter a word for your friend to guess: ")


underscoreNum = len(word)
guessedList = ['_'] * underscoreNum

print("\n")
print('_' * underscoreNum)
print("\n")

finished = 0
incorrect = 0
while finished == 0:
    user = input("\nTake a guess:").lower()
    if user == "exit":
        finished = 1
        break
    if user not in word:
        incorrect += 1
    if incorrect == 6:
        finished = 1

    #Cycles through word to find position that the character matches
    i = 0
    while i < len(word):
        if word[i] == user:
            guessedList[i] = user
        i += 1

    ##Printing the game layout
    if incorrect == 1:
        print("""
        
    |         
    |         
    |        
    |         
    |       
    |
 ___|___
         """)
        print(''.join(str(x) for x in guessedList))
    elif incorrect == 2:
        print("""
    ___________
    |         
    |         
    |        
    |         
    |       
    |
 ___|___
         """)
        print(''.join(str(x) for x in guessedList))
    elif incorrect == 3:
        print("""
    ___________
    |         |
    |         O
    |        
    |         
    |       
    |
 ___|___
        """)
        print(''.join(str(x) for x in guessedList))
    elif incorrect == 4:
        print("""
    ___________
    |         |
    |         O
    |        /|\\
    |         
    |       
    |
 ___|___
                 """)
        print(''.join(str(x) for x in guessedList))
    elif incorrect == 5:
        print("""
    ___________
    |         |
    |         O
    |        /|\\
    |         |
    |       
    |
 ___|___
                     """)
        print(''.join(str(x) for x in guessedList))
    elif incorrect == 6:
        print("""
    ___________
    |         |
    |         O
    |        /|\\
    |         |
    |        / \\
    |
 ___|___
                         """)
        print(''.join(str(x) for x in guessedList))
    else:
        print(''.join(str(x) for x in guessedList))

    #Checks if all characters have been guessed correctly
    if '_' not in guessedList:
        print("\nCongrats, You Won!")
        finished = 1

    #Checks if user lost
    if incorrect == 6:
        print("\nGame Over. You Lost. Play Again!")
