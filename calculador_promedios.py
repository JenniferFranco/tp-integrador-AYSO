#Función para validar el ingreso de números
def validar_numero (mensaje, min= float('-Inf'), max= float('Inf')):
    numero = float(input((f'{mensaje} ')));
    while numero < min or numero > max:
        numero = float(input((f'ERROR. {mensaje}')));
    return numero;  

#Función para la suma de los números
def suma_numeros (a, b, c):
    return a + b + c;

#Función para calcular el promedio
def calcular_promedio(nombre, a, b, c):
    total_notas = suma_numeros(a, b, c) / 3
    print (f'El promedio es:  {total_notas:.2f}')

#programa principal
print('Bienvenido al Calculador de Promedios\n')

while True:
    estudiante = input('Ingrese el nombre del estudiante: ')

    nota1 = validar_numero('Ingrese la nota 1 (1 a 10): ', 1, 10)
    nota2 = validar_numero('Ingrese la nota 2 (1 a 10): ', 1, 10)
    nota3 = validar_numero('Ingrese la nota 3 (1 a 10): ', 1, 10)

    calcular_promedio(estudiante, nota1, nota2, nota3)

    while True:
        continuar = input('¿Desea calcular el promedio de otro estudiante? (s/n): ').lower()
        if continuar in ['s', 'n']:
            break  # rompe el bucle de validación de la respuesta
        else:
            print('ERROR. Ingrese "s" para sí o "n" para no.' )

    if continuar == 'n':
        print('\n¡Hasta luego, profesor/a!')
        break  # rompe el bucle principal y termina el programa



