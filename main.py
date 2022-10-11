from morse import MORSE_CODE_DICT


def encrypter(message):
    encrypted_message = ''
    message = message.upper()
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            encrypted_message += '/' + MORSE_CODE_DICT[letter]
        else:
            # 1 forward-slash indicates different characters
            # and 3 indicates different words
            encrypted_message += '///' + " "

    print(encrypted_message)
