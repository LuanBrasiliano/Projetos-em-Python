#Você está desenvolvendo uma função que embaralha as letras de uma palavra para criar palavras embaralhadas.

#**Instrução:**

#Crie uma função chamada embaralhar_palavra que aceite uma palavra como argumento e retorne a mesma palavra com suas letras embaralhadas. Independentemente da entrada ser em maiúsculas ou minúsculas, a saída deve estar sempre em letras minúsculas.

#A palavra deve ser: embaralhados

import random
def embaralhar(palavra):
    embaralhe = list(palavra);
    random.shuffle(embaralhe);
    embaralhe = "".join(embaralhe);
    print(embaralhe);

embaralhar("naul")