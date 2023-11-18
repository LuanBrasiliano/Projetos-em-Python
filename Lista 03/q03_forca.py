#Você está criando um jogo da forca em Python, um jogo popular de adivinhação de palavras. Neste jogo, um jogador tenta adivinhar uma palavra, letra por letra, antes que o enforcado seja completamente desenhado.

#**Instrução:**

#Crie uma função chamada verificar_letra que aceite dois argumentos: uma palavra secreta e uma letra. A função deve verificar se a letra está presente na palavra secreta. Se a letra estiver na palavra secreta, a função deve retornar True, caso contrário, deve retornar False.

#Apenas 1 letra.

def verificar_letra(palavra,letra):
    if (letra in palavra):
        return true;
    else:
        return false;