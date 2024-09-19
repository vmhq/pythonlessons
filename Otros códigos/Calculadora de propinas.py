def calcular_propina(total, porcentaje):
    return total * (porcentaje / 100)

def main():
    titulo = "Bienvenido a la Calculadora de Propinas"
    print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")
    
    # Solicitar el monto total
    while True:
        try:
            total = float(input("Ingrese el monto total de la cuenta en CLP: "))
            if total <= 0:
                raise ValueError
            break
        except ValueError:
            print("Por favor, ingrese un monto válido mayor que cero.")

    # Preguntar si se divide la cuenta
    while True:
        dividir = input("¿Desea dividir la cuenta entre varias personas? (s/n): ").lower()
        if dividir in ['s', 'n']:
            break
        print("Por favor, responda 's' para sí o 'n' para no.")

    if dividir == 's':
        while True:
            try:
                num_personas = int(input("¿Entre cuántas personas se divide la cuenta?: "))
                if num_personas <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Por favor, ingrese un número válido de personas mayor que cero.")
    else:
        num_personas = 1

    # Preguntar por el porcentaje de propina
    while True:
        opcion_propina = input("Seleccione el porcentaje de propina:\nA) 10%\nB) 15%\nSu elección (A/B): ").upper()
        if opcion_propina == 'A':
            porcentaje = 10
            break
        elif opcion_propina == 'B':
            porcentaje = 15
            break
        print("Por favor, elija A para 10% o B para 15%.")

    # Calcular la propina y el total
    propina = calcular_propina(total, porcentaje)
    total_con_propina = total + propina

    # Mostrar resultados
    print(f"\nResumen de la cuenta:")
    print(f"Monto total: ${total:.0f} CLP")
    print(f"Propina ({porcentaje}%): ${propina:.0f} CLP")
    print(f"Total con propina: ${total_con_propina:.0f} CLP")

    if num_personas > 1:
        monto_por_persona = total_con_propina / num_personas
        print(f"\nDividido entre {num_personas} personas:")
        print(f"Cada persona debe pagar: ${monto_por_persona:.0f} CLP")

if __name__ == "__main__":
    main()