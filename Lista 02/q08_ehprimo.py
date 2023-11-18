# Solicita ao usuário que insira um número
# Verifica se o número é maior que 1
# Inicializa uma variável para contar os divisores
# Loop para verificar se o número é primo
# Se encontrarmos um divisor, podemos parar de verificar
# Se não houver divisores além de 1 e o próprio número, é primo

numero = int(input("Digite o numero que deseja:\n"));
for i in range(1,numero+1,1):
    if(numero%i == 0):
        contador += 1;
if (contador == 2):
    print("É primo!");
else:
    print("Não é primo!");