
import random
from game_data import data

def user_input(person1, person2):
    print(f"A: {person1['name']}        B: {person2['name']} ")
    answer = input("How has more followers? A or B: ")

    if answer == "A":
        if person1['follower_count'] > person2['follower_count']:
            print("You win!")
            win = True
        elif person1['follower_count'] < person2['follower_count']:
            print("You lose!")
            win = False
        else:
            print("It is equal")
            win = True
    else:
        if person1['follower_count'] > person2['follower_count']:
            print("You lose!")
            win = False
        elif person1['follower_count'] < person2['follower_count']:
            print("You win!")
            win = True
        else:
            print("It is equal")
            win = True

    print(f"A: {person1['name']} - {person1['follower_count']}  B: {person2['name']} - {person2['follower_count']} ")
    return win


def game():

    person1 = data[random.randint(0, len(data))]
    person2 = data[random.randint(0, len(data))]
    while person1 == person2:
        person2 = data[random.randint(0, len(data))]

    win = user_input(person1, person2)

    while win:
        if person1['follower_count'] < person2['follower_count']:
            person1, person2 = person2, person1

        person_old = person2
        person2 = data[random.randint(0, len(data))]
        while person1 == person2 or person2 == person_old:
            person2 = data[random.randint(0, len(data))]

        win = user_input(person1, person2)

    print("END of game")



game()
