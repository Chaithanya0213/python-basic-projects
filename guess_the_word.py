

import random
words_list=['apple','ball','cat','dog','eagle','fox','gun','hat','ice']
lives=6
chosen_word=random.choice(words_list)#b a l l
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guess_word=input("Guess letter: ")#b
    for i in range(len(chosen_word)):# 0 1 2 3 4
        letter=chosen_word[i]
        if letter==guess_word:
            display[i]=guess_word
    print(display)
    if guess_word not in chosen_word:
        lives-=1
        print(f"You have {lives} only")
        if lives==0:
            game_over=True
            print("Sorry buddy you don't have lives \"YOU LOSE\"")
    if '_' not in display:
            game_over=True
            print("Hey you guessed the word \"YOU WON\"")
