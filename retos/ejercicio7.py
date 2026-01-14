#EJERCICIO PARA EL PRÓXIMO TEMA4

def check_order(numbers):
    # función built -in de python sorted()
    if numbers == sorted(numbers):
        return "ascending"
    elif numbers == sorted(numbers, reverse=True):
        return "descending"
    else:
        return "neither"

#usando el método de la burbuja
def sorted_manual(lst):
    result = lst[:]  # copia

    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

# Ejemplos
print(check_order([1, 2, 3]))      # ascending
print(check_order([3, 2, 1]))      # descending
print(check_order([1, 3, 2]))      # neither
