message = input("> ")
emojis = {
    ":)":"😀",
    ":(":"🥲"
}

def convert_emoji(message):
    words = message.split()
    covert_msg = ""
    for word in words:
        covert_msg += emojis.get(word, word)
    return covert_msg

converted_message = convert_emoji(message)
print(converted_message)

