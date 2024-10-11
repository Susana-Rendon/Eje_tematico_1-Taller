lista_num = []

#Para que el usuario ingrese los valores a su gusto
while True:
    numero = input("Ingresa un numero (o escribe fin para terminar): ")
    if numero.lower() == "fin":
        break

    numeros = int(numero)
    lista_num.append(int(numeros))

#Con set se quita los numeros duplicados
    sin_duplicados = list(set(lista_num))
    sin_duplicados.sort()

print("Lista de números original:", lista_num)
print("Lista de números sin repetidos:", sin_duplicados)
