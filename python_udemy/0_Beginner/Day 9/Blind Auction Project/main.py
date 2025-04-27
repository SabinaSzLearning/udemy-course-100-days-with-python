# TODO-1: Ask the user for input
dictionary = {}
nextone = "yes"

while nextone == "yes":
    name = input("Name: ")
    price = input("Price: ")
    nextone = input("Next?: ")

    # TODO-2: Save data into dictionary {name: price}

    dictionary[str(name)] = float(price)


# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary
maximum = next(iter(dictionary))
for key in dictionary:
    if dictionary[key] > dictionary[maximum]:
        maximum = key

print(f"Name: {maximum}, price: {dictionary[maximum]}")

