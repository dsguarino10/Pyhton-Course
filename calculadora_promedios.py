import numpy as np
def ingresar_calificaciones():
    materias = []
    calificaciones = []

    while True:
        materia = input("Ingrese el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío.")
            continue

        while True:
            try:
                nota = float(input(f"Ingrese la calificación para {materia} (0 a 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        materias.append(materia)
        calificaciones.append(nota)

        continuar = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break

    return materias, calificaciones


def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return np.mean(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    aprobadas = []
    reprobadas = []

    for i, nota in enumerate(calificaciones):
        if nota >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    if not calificaciones:
        return None, None

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


def main():
    print("Bienvenido a la Calculadora de Promedios\n")
    materias, calificaciones = ingresar_calificaciones()

    if not materias:
        print("\nNo se ingresaron materias. Finalizando el programa.")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas, reprobadas = determinar_estado(calificaciones)
        idx_max, idx_min = encontrar_extremos(calificaciones)

        print("\nResumen de calificaciones:")
        for i in range(len(materias)):
            print(f"- {materias[i]}: {calificaciones[i]}")

        print(f"\nPromedio general: {promedio:.2f}")

        print("\nMaterias aprobadas:")
        if aprobadas:
            for i in aprobadas:
                print(f"- {materias[i]} ({calificaciones[i]})")
        else:
            print("Ninguna materia aprobada.")

        print("\nMaterias reprobadas:")
        if reprobadas:
            for i in reprobadas:
                print(f"- {materias[i]} ({calificaciones[i]})")
        else:
            print("Ninguna materia reprobada.")

        print("\nMejor calificación:")
        print(f"- {materias[idx_max]} ({calificaciones[idx_max]})")

        print("\nPeor calificación:")
        print(f"- {materias[idx_min]} ({calificaciones[idx_min]})")

    print("\nGracias por usar la Calculadora de Promedios.")


if __name__ == "__main__":
    main()