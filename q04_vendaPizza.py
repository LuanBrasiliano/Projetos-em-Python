#Você acaba de ingressar no curso de Python do FEA.dev e decide iniciar sua própria consultoria. Parabéns!!! Você logo recebe seu primeiro cliente, a pizzaria do bairro. Ela tem um grande objetivo em mente: desbancar a grande indústria de pizza Baralho's e Pizza Wut. Para isso, vai recorrer à tecnologia em seus processos. 

#Sua primeira função é criar um sistema que recebe o valor de cada venda de pizza e bebida e imprima o valor final.

print("Registro de vendas da Pizzaria:");
opcao = int(input("Digite a opcao\n1)\n2)\n"));
if(opcao == 1):
    valor_pizza = float(input("Digite o valor pago na pizza\t"));
    valor_refri = float(input("Digite o valor pago no Refri\t"));
    soma = valor_pizza+valor_refri;
    print("O valor total gasto é: ", soma);
else:
    print("Não há vendas a se registrar");