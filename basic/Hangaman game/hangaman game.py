import random
from collections import Counter

name = input("Enter your name: ")
print(f'Welcome to Hangaman Game, {name}')

def play_hanaman_game():
    somewords = 'apple banana carrot drumstick eggplant fig grape hazlenut iceberg lettuce java apple kiwi lemon melon nectarine orange plum quince radish strawberry tomato ugni vanilla bean watermelon ximenia yam zucchini'
    somewords = somewords.split(' ')
    word = random.choice(somewords)
    if __name__ =='__main__':
        print("\n Guess the word😉, HINT: Word is name of a fruit")
        
        for i in word:
            print('_',end=' ')
        print()
        
        #playing = True
        letterguessed = ''
        chances = len(word) + 2
        correct = 0
        flag = 0
        
        try:
            while (chances != 0) and flag == 0:
                print()
                chances -= 1
                try:
                    guess = str(input("Enter a letter to guess: ").lower())
                except:
                    print('Enter only letter!')
                    continue
                if not guess.isalpha():
                    print('Enter only letter😢')
                elif len(guess) > 1:
                    print('enter only single letter😉')
                elif guess in letterguessed:
                    print('You have aldready guessed the letter😒')
                    continue
                
                if guess in word:
                    r = word.count(guess)
                    for i in range(r):
                        letterguessed += guess
                        
                for char in word:
                    if char in letterguessed and (Counter(letterguessed) != Counter(word)):
                        print(char, end=' ')
                        correct += 1
                    elif (Counter(letterguessed) == Counter(word)):
                        print("The word is: ", end=' ')
                        print(word)
                        flag = 1
                        print('conGradulations, you won!')
                        break
                    else:
                        print('_', end=' ')
            if chances <= 0 and (Counter(letterguessed) != Counter(word)):
                print()
                print('You lost! try again...😁👍')
                print('The word was {}'.format(word))
        except KeyboardInterrupt:
            print()
            print('Bye! Try again..👋')
while True:
    play_hanaman_game()
    again = input("\n do you wanna play again? (yes/no):").strip().lower()
    if again != 'yes':
        print('Thanks for playing! catch you later! 👋')
        break
                
        