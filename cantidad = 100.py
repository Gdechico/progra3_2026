import itertools
import string

password = input("Ingrese la contraseña: ")

caracteres = string.ascii_letters + string.digits + string.punctuation

intentos = 0

encontrada = False

for longitud in range(1, len(password) + 1):
    for combinacion in itertools.product(caracteres, repeat=longitud):
        intentos += 1
        intento = ''.join(combinacion)
        print(f"Probando: {intento}", end="\r", flush=True)
        
        if intento == password:
            print(f"Contraseña encontrada: {intento}")
            print(f"Número de intentos: {intentos}")
            encontrada = True
            break
    if encontrada:
        break