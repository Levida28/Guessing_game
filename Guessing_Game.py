import random

num = random.randint (1,21)

print("Welcome to guessing game!")
print("I'm thinking of number between 1 and 20")
print("You have to guess the number I'm thinking of.")
print("LET'S PLAY!")

guesses = [0]


while True:
    
    
    guess = int(input("I'm thinking of number between 1 and 20.\n What is your guess? :"))
    
    
    
    if guess < 1 or guess > 20:
        print('OUT OF BOUNDS! Please try again: ')
        continue
 
    
    # compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 5:
            print('WARM!')
        else:
            print('COLD!')
    