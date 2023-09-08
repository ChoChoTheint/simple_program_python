import random

minVal = 1
maxVal = 6
rollAgain = "yes"
while rollAgain == 'yes' or rollAgain == 'y':
    print('Rolling The Dices.....')
    print('The Values are :')

    print(random.randint(minVal,maxVal))
    rollAgain = input('Roll the Dices Again? ')