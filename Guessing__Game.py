secret__number = 9
guess__count = 0
guess__limit = 3
print('You have only thrice chance ! ''\n''Lets start...')
while guess__count < guess__limit:
    guess = int(input('Guess : '))
    guess__count += 1
    if guess == secret__number:
        print('You won :)')
        break
    elif guess__count == guess__limit:
        print('Sorry, you failed :(''\n''Never mind play again 👍')
    else:
        print("Sorry, You failed !!! :( ")

