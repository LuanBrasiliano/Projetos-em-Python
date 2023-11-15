#b) Enquanto você estava com o computador ligado, um hacker da pizzaria rival do bairro resolveu atacar sua lista de compras invertendo alguns dos itens, como se vê abaixo:

sarpmoc = ['ogirT ed ahniraF', 'Calabresa', 'Milho', 'Champignon', 'etamoT ed ohloM', 'Frango', 
           'Requeijão', 'Lombo', 'niaveL', 'Açúcar']

compras = ['Farinha de Trigo', 'Calabresa', 'Milho', 'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo', 'levain', 'Açúcar'];
novas_compras = [];

for item in sarpmoc:
    if item != compras[sarpmoc.index(item)]:
        str_aux = '';
        for letra in item:
            str_aux = letra+str_aux;
        novas_compras.append(str_aux);
    else:
        novas_compras.append(item);
print(novas_compras);