#Excelente! A clientela adorou o programa de fidelidade.
#Feito isto, chegou a hora de olhar para os processos internos. A ideia é automatizar a lista de compra da semana, antes feita no papel. 

#a) O chef de cozinha resolveu aprender uma receita que utiliza a fermentação natural, de forma que a pizza fique mais próxima da tradicional italiana. Feito isso, não há mais necessidade de utilizar leite, ovos e fermento biológico para a receita. Retire-os da lista de compras e em seguida, adicione Levain e Açúcar, ingredientes da fermentação natural. Imprima a nova lista.

compras = ['Farinha de Trigo', 'Ovos', 'Fermento Biológico', 'Leite', 'Calabresa', 'Milho', 
           'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo']
compras_a_sair = ['Fermento Biológico','Ovos','Leite'];
novas_compras = ['levain','Açucar'];
for item in compras_a_sair:
    for outroItem in compras:
        if(item == outroItem):
            compras.remove(outroItem);
compras = compras + novas_compras;
print(compras);