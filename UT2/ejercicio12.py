num_estudiantes = int(input("¿Cuántos estudiantes hay? "))
num_dias = int(input("¿Cuántos días se registrará la asistencia? "))



for i in range(num_estudiantes):
    nombre = input(f"\nIntroduce el nombre del estudiante {i+1}: ")
    dias_asistidos = 0

    for dia in range(1, num_dias + 1):
        respuesta = input(f"Día {dia}: ¿{nombre} asistió? (sí/no) ").lower()
        if respuesta == "sí" or respuesta == "si":
            dias_asistidos += 1
    print(f"{nombre} asistió {dias_asistidos} días de {num_dias}")

