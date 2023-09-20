import string
from art import logo

alphabets = list(string.ascii_lowercase)
run_again = True

print(logo)
while run_again:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt : \n' ).lower()
    text = input('Type your message : \n').lower()
    shift = int(input('Type the shift number : \n'))

    def caesar(direction_input, message, key):
        final_text = ''
        if direction_input == 'decode' or direction_input == 'decrypt':
            key *= -1

        for char in message:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = position + key
                while abs(new_position) > len(alphabets) - 1:
                    if new_position < 0:
                        new_position += len(alphabets)
                    else:
                        new_position -= len(alphabets)
                final_text += alphabets[new_position]
            else:
                final_text += char
        print(f'The {direction_input}d text is: {final_text}\n')

    caesar(direction, text, shift)
    run = input('Type "yes" if you want to go again. Otherwise type "no": \n').lower()
    if run == 'no':
        run_again = False
        print('Goodbye')