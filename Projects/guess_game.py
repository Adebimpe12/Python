myset = {1, 5, 9, 3, 8, 2, 4, 7, 6, 10}
score = 0
x = 0

while x is range(5):
    guess = int(input('guess a number from 1-10: '))
    chosen_number = myset.pop()
    myset.add(chosen_number)
    print(chosen_number)
    if guess == chosen_number:
        print('You guessed right. ')
        score += 5
    else:
        print(f'wrong')
        score -= 5
    user = input('press 1 to replay or # to exit')
    if user == '#':
        break
    else:
        print('Game over!')

print(f'Your score is {score}')