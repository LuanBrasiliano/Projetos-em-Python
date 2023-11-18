#O primeiro passo será tornar o panfleto digital, de forma que seja enviado pelas redes sociais e não precise ser impresso e consequentemente descartável. Para demonstrar essa funcionalidade ao dono, você deve criar um exemplo de panfleto que contenha os sabores de pizza salgadas e doces (separados), tipos de bebida e adicionais, conforme os valores a seguir:
#-  Pizzas salgadas: Calabresa, Portuguesa, Mussarela e Pepperoni;
#-  Pizzas doces: Prestígio, Chocolate e Doce de Leite;
#-  Bebidas: Guaraná, Cola, Suco de Laranja e Suco de Uva;
#-  Adicionais: Bacon, Requeijão, Milho e Azeitona

#Imprima o panfleto final.

p_salgada = ['Calabresa', 'Portuguesa', 'Mussarela', 'Pepperoni'];
p_doce = ['Prestígio', 'Chocolate', 'Doce de Leite'];
bebidas = ['Guaraná', 'Cola', 'Suco de Laranja', 'Suco de Uva'];
adicionais = ['Bacon', 'Requeijão', 'Milho', 'Azeitona'];

print('\nLista de Pizzas Salgadas.\n');
for pizza in p_salgada:
    print('{0}) Pizza de {1}.'.format(p_salgada.index(pizza), pizza));
print('\nLista de Pizzas Doces.\n');
for pizza in p_doce:
    print('{0}) Pizza de {1}.'.format(p_doce.index(pizza), pizza));
print('\nLista de Bebidas.\n')
for liquido in bebidas:
    print('{0}) Bebida de {1}.'.format(bebidas.index(liquido), liquido));
print('\nAdicionais.\n');
for item in adicionais:
    print('{0}) Pizza de {1}.'.format(adicionais.index(item), item));