def sum_numbers_in_string(text):
    total = 0
    current_number = ""

    for char in text:
        # Comprobación manual de dígito
        if '0' <= char <= '9':
            current_number += char
        else:
            if current_number != "":
                total += int(current_number)
                current_number = ""

    # Si el string termina con un número
    if current_number != "":
        total += int(current_number)

    return total

# Pruebas
print(sum_numbers_in_string("abc123xyz45"))   # 168
print(sum_numbers_in_string("7dogs3cats"))    # 10
print(sum_numbers_in_string("no numbers"))    # 0



''' 
import re

def sum_numbers_in_string(text):
    numbers = re.findall(r'\d+', text)
    return sum(int(n) for n in numbers)

# Ejemplo
print(sum_numbers_in_string("abc123xyz45"))  # 168'''
