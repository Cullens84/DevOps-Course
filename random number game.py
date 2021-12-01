var1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_num, guess_num = var1(1, 10), 0
while target_num != guess_num:
    guess_num = int(input( 'guess a number between 1 and 10 until you get it right : '))
print('Well Guessed!')
