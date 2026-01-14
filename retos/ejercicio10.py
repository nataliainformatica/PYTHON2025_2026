

def golf_score(par, strokes):
    diff = strokes - par

    if strokes == 1:
        return "Hole-in-one"
    elif diff <= -3:
        return "Albatross"
    elif diff == -2:
        return "Eagle"
    elif diff == -1:
        return "Birdie"
    elif diff == 0:
        return "Par"
    elif diff == 1:
        return "Bogey"
    elif diff == 2:
        return "Double Bogey"
    else:
        return "Go Home!"

# Ejemplo
print(golf_score(5, 4))  # Birdie
