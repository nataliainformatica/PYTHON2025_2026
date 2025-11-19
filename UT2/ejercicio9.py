import string

text="texto de prueba"
decrypt =False
shift = 3

alphabet = list(string.ascii_lowercase)
alphabet.insert(alphabet.index("n") + 1, "ñ")

caesar_text = ""

for value in text.lower():
    if value in alphabet:
        index = (alphabet.index(value) + (-shift if decrypt else shift)) % len(alphabet)
        caesar_text += alphabet[index]
    else:
        caesar_text += value

print(caesar_text)

"""
Constante	Contenido
string.ascii_lowercase	"abcdefghijklmnopqrstuvwxyz"
string.ascii_uppercase	"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string.ascii_letters	Todas las mayúsculas y minúsculas
string.digits	"0123456789"
string.hexdigits	"0123456789abcdefABCDEF"
string.punctuation	símbolos como !"#$%&'()*+,-./:;<=>?@[\]^_{

"""
