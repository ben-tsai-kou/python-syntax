temperature = 9

if temperature > 30:
    print("it's a hot day")
elif temperature < 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")

# question

text = input("please type something text: ")

if len(text) < 3:
    print("text must be at least 3 characters long")
elif len(text) > 50:
    print("text must be less than 50 characters long")
else:
    print("text looks good!")


