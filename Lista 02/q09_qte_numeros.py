#Crie um programa que peça para digitar um número constantemente sem limite, até que o usário digite o número 0. Em seguida mostre a soma de todos os valores inputados, e a quantidade de números que foram inputados.

soma = 0;
contador = 0;
numero = int(input("Digite o numero:\n"));
while(numero != 0):
    contador += 1;
    soma += numero;
    numero = int(input("Digite um numero:\n"));
print("A soma dos numeros imputados", soma);
print("Quantidade de numeros inseridos", contador);