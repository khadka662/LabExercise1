
'''
game finding a secret number within 3 attempts using while loop
'''

import random
random_num = random.randint(1,10)
guess = int(input('enter your number:'))
i = 1
while i<3:
    if random_num ==guess:
        print(f"congratulation: you have guessed it")
        break

    else:
        guess = int(input("guess again:"))
    i = i+1

print('you have crossed your limit')

