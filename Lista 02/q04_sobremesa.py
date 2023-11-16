#Você está comprando uma sobremesa em uma cafeteria. O preço da sobremesa pode variar, e você tem um voucher que cobre até $20. Se a sobremesa custar mais, você precisará pagar a diferença. Se custar menos, você economizará o valor restante do voucher.

#Crie um programa em Python que solicite o preço da sobremesa que você deseja comprar. Em seguida, o programa deve calcular se a operação foi vantajosa e quanto você economizou ou precisa pagar a mais.

#Se o preço da sobremesa for maior que 20, o programa deve imprimir "Você precisa pagar X a mais." (onde X é a diferença entre o preço da sobremesa e 20).

#Se o preço da sobremesa for igual a 20, o programa deve imprimir "Você não precisa pagar nada a mais."

#Se o preço da sobremesa for menor que 20, o programa deve imprimir "Você economizou X." (onde X é a diferença entre 20 e o preço da sobremesa).

##SEU CÓDIGO COMEÇA AQUI##

voucher = 20;
credito = 0;
divida = 0;
valor = int(input("Digite o valor da sobremesa:\n"));
if(valor < voucher):
   credito = voucher - valor;
   print("Voce economizou {}".format(credito));
elif(valor == voucher):
   print("Voce não precisa pagar mais nada.");
else:
   divida = valor - voucher;
   print("Voce precisa pagar {} a mais.".format(divida));