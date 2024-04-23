# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário;
# A tabuada não deve necessariamente iniciar em 1 e terminar em 10;
# O valor inicial e final devem ser informados também pelo usuário

num_tabuada = int(input("Digite um número, entre 1 e 10, apara que seja executada a tabuada: "))
num_inicial = int(input("Digite um número, entre 1 e 10, que vai iniciar a tabuada de multiplicação: "))
num_final = int(input("Digite um número, entre 1 e 10, que vai finalizar a tabuada de multiplicação: "))

if num_final < num_inicial:
    print("Erro: O número final deve ser maior ou igual ao número inicial.")
else:
    print(f"Montando a tabuada de {num_tabuada}, iniciando em {num_inicial} e terminando em {num_final}.")
    print(20*"==")
    
for item in range(num_inicial, num_final + 1):
    resultado = num_tabuada * item
    print(f"O resultado de {num_tabuada} x {item} é: {resultado}.")
        
print("Fim da Tabuada!")