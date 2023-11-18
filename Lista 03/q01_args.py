#Observando o departamento de contabilidade da HelloWorld, você percebeu que os funcionários passam o dia multiplicando valores e, como um bom programador, resolveu tornar esse processo mais eficiente. Desenvolva a função mult, que retorna a multiplicação dos parâmetros "a", "b", "c" e "d". Porém, a função não precisa necessariamente receber os 4 argumentos. Caso um parâmetro não receba um argumento, ele deve valer 1.

def mult(*args):
    soma = 0;
    if(len(args) == 0):
        print("A soma é 1");
    else:
        for num in args:
            soma += num;
        print("A soma é {}".format(soma));
        