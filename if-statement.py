is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("it's a lovely day")
print("enjoy your day")

# question

price = 1000000
is_good_credit = False

if is_good_credit:
    print(f"you need to put down: ${price * 0.1}")
else:
    print(f"you need to put down: ${price * 0.2}")