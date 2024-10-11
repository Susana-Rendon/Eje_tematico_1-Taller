lista_num = []
suma_pares = 0

#Para que el usuario ingrese los valores a su gusto
while True:
    numeros = input("Ingresa un número (o escribe fin para terminar): ")
    if numeros.lower() == "fin":
        break

    numero = int(numeros)
    lista_num.append(int(numero))

#Analiza los numeros pares y los suma entre ellos
    if numero % 2 == 0:
        suma_pares += numero

print("Lista de números original:", lista_num)
print("Resultado de la suma de pares es:", suma_pares)

