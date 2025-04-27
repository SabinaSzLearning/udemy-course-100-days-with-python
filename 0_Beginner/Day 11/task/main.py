cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

comCards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
myCards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]

print(f"ComCards: {comCards[0]}, Yours: {myCards}")

decision1 = input("Hit or passe? H/P?")
if decision1 == "P":
    if sum(myCards) > sum(comCards) and sum(myCards) <= 21:
        print("you win")
    elif sum(myCards) == sum(comCards):
        print("draw")
    else:
        print("you lose")

    print(f"ComCards: {comCards}, Yours: {myCards}")

else:
    myCards.append(cards[random.randint(0, 12)])

    if sum(myCards) > sum(comCards) and sum(myCards) <= 21:
        print("you win")
    elif sum(myCards) == sum(comCards):
        print("draw")
    else:
        print("you lose")