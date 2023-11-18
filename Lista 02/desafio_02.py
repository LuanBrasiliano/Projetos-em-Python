#Escreva um programa em Python que solicite ao usuário que insira um ano (um número inteiro) e determine se o ano é bissexto ou não. O programa deve continuar pedindo ao usuário para inserir anos até que ele decida parar.

#Um ano bissexto é um ano que é divisível por 4, com exceção dos anos que são divisíveis por 100. No entanto, anos divisíveis por 400 também são considerados bissextos. Em outras palavras:

#**Anos divisíveis por 4 são bissextos (por exemplo, 2004, 2008, 2012).**

#**Anos divisíveis por 100 não são bissextos**

#Instruções:

#Solicite ao usuário que insira um ano.

#Verifique se o ano é bissexto de acordo com as regras mencionadas anteriormente.

#Se o ano for bissexto, imprima "O ano [ano] é bissexto.".

#Se o ano não for bissexto, imprima "O ano [ano] não é bissexto.".

#Pergunte ao usuário se ele deseja verificar outro ano.

#Se o usuário quiser verificar outro ano, repita o processo. Caso contrário, encerre o programa.

print("Deseja inserir um ano?\n1)Sim.\n2)Não\n");
opcao = int(input("Opcao:\n"));
if(opcao == 1):
    while(opcao != 2):
        print("Digite um ano para verificar se é bissexto!\n");
        ano = int(input("Digite o numero do ano\n"));
        if((ano % 4 == 0) or (ano % 400 == 0)):
            if(ano % 100 == 0):
                print("O ano {} não é bissexto\n".format(ano));
            else:
                print("O ano {} é bissexto.\n".format(ano));
        else:
            print("O ano {} não é bissexto.\n".format(ano));
        print("Deseja inserir um novo ano para ser verificado?\n1)Sim.\n2)Não.\n");
        opcao = int(input("Opcao:\n"));
else:
    print("Usuário não quer interagir.");