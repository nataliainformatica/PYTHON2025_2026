def convert_vowels(text):
    vowels = "aeiou"
    result = ""

    for char in text:
        if char.lower() in vowels:
            result += char.upper()
        elif char.isalpha():
            result += char.lower()
        else:
            result += char

    return result


def convert_vowels2(text):
    vowels = "aeiouAEIOU"
    result = ""

    for char in text:
        if char in vowels:
            result += char
        elif charIsAlphabetic(char):
        #elif char.isalpha():
            # result += char.lower()
            result += lower_manual(char)
        else:
            result += char

    return result



def charIsAlphabetic(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z')
def lower_manual(char):
    # Si es mayúscula A–Z, convertirla
    #'a' - 'A' = 32
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

def lower_manual2(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + (ord('a') - ord('A')))
    return char

def upper_manual(char):
    if 'a' <= char <= 'z':
        return chr(ord(char) - 32)
    return char
# Ejemplo
print(convert_vowels("Hello World!"))  # hEllO wOrld!
