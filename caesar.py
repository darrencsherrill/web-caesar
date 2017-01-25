def encrypt(text, rot):
    newstr = ''
    for letter in text:
        newstr += (rotate_character(letter, rot))
    return newstr

def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter) - 97
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter) - 65
    else:
        pass

def rotate_character(char, rot):
    if len(char) != 1:
        return -1
    elif char.isalpha() == False:
        return char
    else:
        if (ord(char) >= 97) and (ord(char) <= 122):
            return chr(97 + (alphabet_position(char) + rot) % 26)
        elif (ord(char) >= 65) and (ord(char) <= 90):
            return chr(65 + (alphabet_position(char) + rot) % 26)
        else:
            return char    
