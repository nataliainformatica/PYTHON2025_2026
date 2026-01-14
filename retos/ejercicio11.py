def how_many_plants(field_length, field_width, plant_space):
    area = field_length * field_width
    return area // (plant_space ** 2)

# Ejemplo
print(how_many_plants(10, 5, 1))  # 50
