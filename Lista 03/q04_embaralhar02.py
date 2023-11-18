#Você está desenvolvendo uma função que embaralha as letras de uma palavra para criar palavras embaralhadas.

#**Instrução:**

#Crie uma função chamada embaralhar_palavra que aceite uma palavra como argumento e retorne a mesma palavra com suas letras embaralhadas. Independentemente da entrada ser em maiúsculas ou minúsculas, a saída deve estar sempre em letras minúsculas.

#A palavra deve ser: embaralhados

import random
def embaralhe(palavra):
    palavra_aux = "";
    lista_aux = [];
    contador = 0;
    while(contador != len(palavra)):
        aleatorio = random.randint(0,(len(palavra)-1));
        if not(aleatorio in lista_aux):
            lista_aux.append(aleatorio);
            palavra_aux = palavra_aux + palavra[aleatorio];
            contador += 1;
    print(palavra_aux);
    
embaralhe("margareth")