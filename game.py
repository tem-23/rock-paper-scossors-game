import random
turns = ['rock','paper','scossors']

human_turn = input('Enter your turn: ')
computer_turn = random.choice(turns)

print(f'Human:{human_turn} vs. Computer:{computer_turn}')
if human_turn == computer_turn:
    print('Draw!')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print ('Human Wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print ('Human Wins!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print ('Human Wins!')
else:
    print('Computer wins!')
