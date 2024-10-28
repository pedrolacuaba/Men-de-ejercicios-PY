def menu():
    print("")
    print("---------------------------------=== MENU PRINCIPAL -------------------------------------=== ")
    print("")
    print(
    "Ejercicios POO:\n"
        "1. Ejercicio Personas                           | "
        "2. Ejercicio Cuenta\n"
        "3. Ejercicio Fraccion                           | "
        "4. Ejercicio Complejo\n"
        "5. Cliente y Banco                              | "
        "6. Clases Cuenta, Plazo Fijo y Caja Ahorro\n\n"

    "Ciclo While:\n"
        "7. Notas Alumnos                                | "
        "8. Sueldos de Empleados\n"
        "9. Aprobados y Suspendidos de Alumnos\n\n"
    
    "Ciclo For:\n"
        "10. Suma de Últimos 5 Números                   | "
        "11. Tabla de Multiplicar\n"
        "12. Ingreso de Puntos en Cuadrantes             | "
        "13. Clasificación de Triángulos\n\n"
    
    "Funciones:\n"
        "14. Cuadrado y Producto de Números              | "
        "15. Conteo de Vocales en un String\n"
        "16. Separación de Números Positivos y Negativos | "
        "17. Conteo de Personas Mayores de 18 Años\n\n"
    
    "Simples:\n"
        "18. Análisis de String\n\n"
    
    "Otros:\n"
        "19. Validación de Nombres de Usuario            | "
        "20. Adivina el Número"
    )
    print("")
    choice = int(input("Elige una opcion (1-20). Para salir (0): "))    #dejar como entero.
    print("")
    return choice

#Bucle while para mostrar el menú hasta que se ingrese 0 "Para salir", por teclado.
while True:
    
    #Ejercicios de Jheinel:
    # Fin ejercicios de Jheinel
    
    #Ejercicios de jhael:
    # Fin ejercicios de Jhael
    
    #Ejercicios de Ronny:

    # Realizar un programa que solicite la carga de un valor entero del 1 al 10. Mostrar
    # después la tabla de multiplicar de dicho número.
    def tabla_multiplicar():
        print("\n--- Tabla de Multiplicar ---"),
        print("")

        #Pedimos el numero
        num = int(input("Ingresa un valor del 1 al 10: "))

        #Bucle para multiplicar el numero ingresado por la tabla
        if 1 <= num <= 10: #num debe estar entre 1 y 10
            for i in range(1,12):
                print(f"{num} x {i} = {num * i}")
        else:
            print("El número debe estar entre 1 y 10.")

    
    """Esto es lo que hay que hacer para poder llamar al menú y elegir una opcion."""
    ##Llamar a la funcion si elige su opcion
    opcion = menu()     #pregunta "porqué si no instancio la funcion se imprime dos veces el menú, ejemplo si hago if menu() == 11: tabla_multiplicar()
    if opcion == 11:
        tabla_multiplicar()

    # Realizar un programa que pida ingresar dos datos enteros (coordenadas x e y). Al
    # comenzar el programa se pedirá ingresar el total de puntos a procesar. Informar de
    # cuantos puntos se han ingresado en cada uno de los cuatro cuadrantes.

    def puntos_cuandrantes():
        print("\n--- Ingreso de Puntos en Cuadrantes ---\n")

        # Contadores para cada cuadrante y puntos sobre ejes
        cuadrante_1 = 0
        cuadrante_2 = 0
        cuadrante_3 = 0
        cuadrante_4 = 0
        sobre_ejes = 0

        # Pedir al usuario el total de puntos a procesar
        puntos_totales = int(input("Ingresa el total de puntos a procesar: "))

        # Procesar cada punto
        for i in range(puntos_totales):
            coord_x = int(input(f"Ingrese la coordenada x del punto {i + 1}: "))
            coord_y = int(input(f"Ingrese la coordenada y del punto {i + 1}: "))
            
            # Determinar en qué cuadrante se encuentra el punto o si está sobre los ejes
            if coord_x > 0 and coord_y > 0:
                cuadrante_1 += 1
            elif coord_x < 0 and coord_y > 0:
                cuadrante_2 += 1
            elif coord_x < 0 and coord_y < 0:
                cuadrante_3 += 1
            elif coord_x > 0 and coord_y < 0:
                cuadrante_4 += 1
            else:
                sobre_ejes += 1  # Punto está sobre los ejes

        # Resultados
        print(f"\nPuntos en el cuadrante 1: {cuadrante_1}")
        print(f"Puntos en el cuadrante 2: {cuadrante_2}")
        print(f"Puntos en el cuadrante 3: {cuadrante_3}")
        print(f"Puntos en el cuadrante 4: {cuadrante_4}")
        print(f"Puntos sobre los ejes: {sobre_ejes}")

    ##Llamar a la funcion si elige su opcion
    #(No volver a llamar a la funcion menú, solo usar la instancia opcion)
    if opcion == 12:
        puntos_cuandrantes()


    # Realizar un programa que lea los lados de n triángulos. Informar después de cada
    # triángulo si es equilátero (tres lados iguales), isósceles (dos lados iguales) o
    # escaleno (ningún lado igual). Informar después del total de triángulos de cada tipo.

    def clasificion():
        print("\n--- Clasificación de Triángulos ---")
        print("")

    #Clasificacion
    def clasificar_triangulo(lado1, lado2, lado3):
            if lado1 == lado2 == lado3:
                return "equilátero"
            elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                return "isósceles"
            else:
                return "escaleno"

    # Función principal
    def princip():
        #números de triángulos
        n = int(input("Ingrese la cantidad de triángulos a clasificar: "))
            
        # Contadores para cada tipo de triángulo
        equilateros = 0
        isosceles = 0
        escalenos = 0

        # clasificaciion
        for i in range(n):
            print(f"\nTriángulo {i + 1}:")
            lado1 = float(input("Ingrese el primer lado: "))
            lado2 = float(input("Ingrese el segundo lado: "))
            lado3 = float(input("Ingrese el tercer lado: "))
                
            tipo = clasificar_triangulo(lado1, lado2, lado3)
                
                # Tipo de triangulo
            print(f"El triángulo {i + 1} es {tipo}.")
                
                # Incrementar el contador de cada var
            if tipo == "equilátero":
                    equilateros += 1
            elif tipo == "isósceles":
                    isosceles += 1
            elif tipo == "escaleno":
                escalenos += 1

            # Totales
        print("\nResumen:")
        print(f"Total de triángulos equiláteros: {equilateros}")
        print(f"Total de triángulos isósceles: {isosceles}")
        print(f"Total de triángulos escalenos: {escalenos}")

    ##Llamar a la funcion si elige su opcion
    if opcion == 13:
        clasificion()
        princip()


    # Realizar un programa con dos funciones. La primera debe solicitar la carga de un 
    # valor entero y mostrar el cuadrado de dicho valor. La segunda que solicite la carga 
    # de dos valores y muestre el producto de los mismos. Deberán llamar a estas dos 
    # funciones desde el bloque principal (Fuera de toda función, como en el ejemplo 
    # realizado al principio de este tema).

    def cuadrado_producto_numero():
        print("\n--- Cuadrado y Producto de Números ---")
        print("")

    #Funcion para el primer numero al cuadrado
    def cuadrado():
        num1 = int(input("Ingrese el primer numero: "))
        result_cuadrado = num1**2
        print( f" {num1}^2 = {result_cuadrado}")

    #Funcion para multiplicar los 2 numeros
    def producto():
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        result_producto = num1 * num2
        print (f"{num1} x {num2} = {result_producto}")

    ##Llamar a la funcion si elige su opcion
    if opcion == 14:
        cuadrado_producto_numero()
        cuadrado()
        producto()

    # Realizar un programa que tenga una función que reciba un string como parámetro.
    # Debe mostrar la cantidad de vocales que tiene dicho string. Se deberá llamar 3
    # veces desde el bloque principal, con 3 strings diferentes.

    def conteo_vocales():
        print("\n--- Conteo de Vocales en un String ---")
        print("")

    def contar_vocales(texto):
        try:
            if not texto.isalpha(): #verificar si hay un numero en el texto
                raise ValueError("El texto no debe contener numeros, ni caracteres especiales.\n")   #forzar manejo de error
                    
            vocales = 'aeiou'
            cant_vocales = sum(1 for letra in texto.lower() if letra in vocales)    #se suma 1 a cant_vocales si en si en texto hay una vocal
            print(f"{texto} tiene {cant_vocales} vocales")
                    
        except ValueError as error:
                print("¡Ha ocurrido un error!: ",error) #imprime el error

    ##Llamar a la funcion si elige su opcion
    if opcion == 15:
        conteo_vocales()
        contar_vocales('0')
        contar_vocales('Ronny')
        contar_vocales('ITLA')
    

#Fin ejercicios de Ronny

#Ejercicios de Ricardo
# Fin ejercicios de Ricardo

    #Poner sus los bloques de codigo de sus programas encima de el siguiente bloque de codigo:
    """OJO DEJAR ESTO SIEMPRE AL FINAL DE EL PROGRAMA EN GENERAL"""
    #Con esto cerramos el menú.
    if opcion == 0:
        print("Haz salido del programa.")
        break