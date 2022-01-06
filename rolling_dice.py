import random

reply = input('Would you like to roll the dice? (Y/N): ')

if reply.lower() == 'y':
    print(random.randint(1, 6))
else:
    print('Thank you for your answer')
