lista_num = []

#Para que el usuario ingrese los valores a su gusto
while True:
    numero = input("Ingrese un numero (o escribe fin para terminar): ")
    if numero.lower() == 'fin':
        break

    numeros = int(numero)
    lista_num.append(numeros)

print("Lista de números original:", lista_num)

lista_invertida = lista_num[::-1]

print("Lista de números inversa:", lista_invertida)



