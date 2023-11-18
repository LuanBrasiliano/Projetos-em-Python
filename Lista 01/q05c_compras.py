#c) Após esse duro golpe, você percebe que é necessário guardar as informações importantes em uma estrutura de dados que seja mais segura (isto é, que não seja mutável). Converta a lista de compras para uma estrutura com estas características e imprima o tipo da variável. &nbsp; Dica: Utilize a função type() para obter o tipo da variável

compras = ['Farinha de Trigo', 'Calabresa', 'Milho', 'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo', 
           'levain', 'Açúcar'];
n_compras = tuple(compras);
print(type(n_compras));