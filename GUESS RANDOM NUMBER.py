import random

num = random.randint(1, 10)
print(num)
guesses = 0
while guesses < 3:
    print('Guess a number between 1 and 10')
    guess = input()
    i = int(guess)
    guesses += 1
    if i == num:
        print('You won, congratulations!!!')
        break
    elif i == num + 1 or i == num - 1:
        print('Hot')
    elif i == num + 2 or i == num - 2:
        print('Warm')
    else:
        print('Cold')

    if guesses == 3:
        print('You guessed 3 times,guess over')
        break
