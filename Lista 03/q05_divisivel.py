#Você está desenvolvendo uma função chamada eh_numero_par que verifica se um número é par ou ímpar. Esta função ajudará a determinar se um número dado é divisível por 2.

#**Instruções:**

#Crie uma função chamada eh_numero_par que aceite um número como argumento.

#Dentro da função, verifique se o número é divisível por 2. Se for divisível por 2, retorne True. Caso contrário, retorne False.

def eh_numero_par(numero):
    if(numero % 2 ==0):
        print("É numero par.");
    else:
        print("É numero Impar.");