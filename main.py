import random

elementos ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña = int(input("introduzca la longitud de la contraseña"))

password = ""

for i in range(contraseña):
password = password + random.choice(elementos)


print(password)
