#Escreva um programa em Python que solicite ao usuário que insira um número inteiro e, em seguida, verifique se o número é par ou ímpar. Se for par, o programa deve imprimir "O número é par." Caso contrário, deve imprimir "O número é ímpar."

print("Digite o numero a ser verificado:");
numero = float(input("Digite o numero:\n"));
if(numero % 2 == 0):
    print("O numero é par");
else:
    print("O numero é impar");