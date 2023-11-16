#Você está criando um programa de boas-vindas em Python para um jogo simples. Você deseja que o programa peça ao jogador para inserir um número, e com base nesse número, o programa dará uma resposta personalizada. Se o número inserido pelo jogador for maior que 10, o programa dará as boas-vindas a um jogador experiente. Se for 10 ou menor, o programa dará as boas-vindas a um jogador iniciante. Você precisa usar uma estrutura condicional (if-else) para fazer isso.

#Crie um programa em Python que peça ao jogador para digitar um número inteiro. Em seguida, verifique se o número é maior que 10. Se for maior que 10, imprima "Bem-vindo, jogador experiente!". Se for 10 ou menor, imprima "Bem-vindo, jogador iniciante!". Certifique-se de usar uma estrutura condicional (if-else) para determinar a saída com base no número inserido pelo jogador.



#lembre-se para pedir que o jogador insira um número você deve usar *input*

print("Bem vindo jogador!\n");
numero = float(input("Digite o numero.\n"));
if(numero > 10):
    print("Bem vindo, Jogador Experiente.");
else:
    print("Bem vindo, jogador iniciante.");