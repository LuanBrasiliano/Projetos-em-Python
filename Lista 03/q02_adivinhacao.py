#Você está desenvolvendo um jogo de adivinhação muito simples, no qual o jogador tenta adivinhar um número secreto entre 1 e 100.

#**Instrução:**

#O programa gerará aleatoriamente um número entre 1 e 100 que o jogador deve adivinhar.

#O jogador poderá inserir um palpite (um número inteiro) e pressionar "Enter".

#O programa fornecerá feedback sobre o palpite do jogador, dizendo se o palpite é muito alto, muito baixo ou correto em relação ao número secreto.

#O jogador continuará a adivinhar até acertar o número secreto.

#O programa informará quantas tentativas foram necessárias para acertar o número.

#Bem-vindo ao Jogo de Adivinhação! Tente adivinhar o número secreto entre 1 e 100.

#Digite o seu palpite: 50 O número é maior. Tente novamente.

#Digite o seu palpite: 25 O número é maior. Tente novamente.

#Digite o seu palpite: 37 O número é menor. Tente novamente.

#Digite o seu palpite: 42 Parabéns! Você acertou o número secreto 42 em 4 tentativas.

import random

contador = 1;
aleatorio = random.randint(1,100);
palpite = int(input("Digite seu palpite:\n"));
while(palpite != aleatorio):
    if(palpite > aleatorio):
        print("O numero é menor. Tente novamente.\n");
    else:
        print("O numero é maior. Tente novamente.\n");
    palpite = int(input("Digite seu palpite:\n"));
    contador += 1;
print("Voce acertou o numero secreto {} em {} tentativas.\n".format(aleatorio,contador));