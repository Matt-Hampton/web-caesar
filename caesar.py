alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):

    if letter.islower():
        alphabet = alpha_lower
    else:
        alphabet = alpha_upper
    return alphabet.index(letter)

def rotate_char(char, rot):
    if not char.isalpha():
        return char
    if char.islower():
        alphabet = alpha_lower
    else:
        alphabet = alpha_upper
    new_pos = (alphabet_position(char) + rot) % 26
    return alphabet[new_pos]

def encrypt(text, rot):
    answer = ""
    for char in text:
        answer += rotate_char(char, rot)
    return answer
