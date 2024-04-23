# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

num_int = list(range(0, 21))
lista_pares = []
lista_impares = []

for numero in range(1,21):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
        
print(f"Os números são: {num_int}.")
print(20 * "==")
print(f"Os números pares são: {lista_pares}.")
print(20 * "==")
print(f"Os números ímpares são: {lista_impares}.")
