# b)Você ficou animado com o novo programa criado acima para imprimir os números e mostrou pra um amigo que dá aula para o fundamental 1. Ao ver a mágica acontecendo seu amigo implorou para que você construísse uma tabuada automática para ele.

#Escreva um código que receba o input de um número e retorne sua tabuada padrão, multiplicando até 10 e ajude o profesor a automatizar suas aulas.
  
#OBS: deixe sua tabuada toda alinhada conforme exemplo:
 
#    n = 7
    
#    7 x 1 = 7
#    7 x 2 = 14
#    .
#    .
#    .
#    7 X  9 = 63
#    7 X 10 = 70

num = int(input("Digite o numero da tabuada"));
for i in range(1,11,1):
    print("{}x{}={}".format(num, i, num*i));