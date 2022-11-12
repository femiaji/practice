import random
number = random.randint(1, 10)

player_name = input("Hello, what is your name? ")
number_of_guesses = 0
print(f"""
Nice to meet you {player_name}!
\nLet\'s play a game. 
I will think of a number between 1 and 10. You have to guess the number correctly in three tries. 
You have only 3 chances so start guessing now:'.format(player_name)""")

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low, go up a little!')
    if guess > number:
        print('Your guess is too high, go down a bit!')
    if guess == number:
        break
if guess == number:
    print( 'Congratulations {}, you guessed the number in {} tries!'.format(player_name, number_of_guesses))
    print(f"Thank you {player_name} for playing 'Guess the Number' with me. Have a nice day!")
    print("****THE END****")
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(number))
    print(f"Thank you {player_name} for playing 'Guess the Number' with me. Have a nice day!")
    print("****THE END****")
