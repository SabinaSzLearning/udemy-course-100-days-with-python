import random

number = random.randint(1,100)
game_over = True
counter = 6

while game_over:
    yourNumber = int(input("Guess number: "))
    if yourNumber == number:
        print("You win")
        game_over = False
    elif yourNumber > number:
        print("To much")
    else:
        print("To low")

    counter -= 1
    if counter == 0:
        print(f"You lose, number was {number}")
        game_over = False
    print(counter)