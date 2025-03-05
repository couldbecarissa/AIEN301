import random
word_list=["Anoud","Adnan","Carissa","Bryan","James","Thembily"]
chosen_word=input("Gimme sum!")

lives=6

display=["_" for _ in chosen_word]
print(''.join(display))

game_over=False
while not game_over:
    guess=input("Guess a letter dammit!").lower()

    for index,letter in enumerate(chosen_word):
        if letter==guess:
            display[index]=letter
        print(' '.join(display))

        if guess not in chosen_word:
            lives-=1
            if lives==0:
                game_over=True
                print("LOOOSSSSSEEEEEEERRRRRRRRR")

        if "_" not in display:
            game_over=True
            print("SLAYYYYY!!!!")

        