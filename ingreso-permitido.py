# PASO 1: Solicitar al usuario que ingrese la edad del cliente
edad = int(input("Por favor, ingrese la edad del cliente: "))

# PASO 2: Verificar si la edad ingresada cumple con los requisitos para el ingreso a la discoteca
permitido = True if edad >= 18 else False

# PASO 3: Mostrar al usuario si el cliente puede ingresar
if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("Lo sentimos mucho, no puedes ingresar a la discoteca siendo menor de edad")