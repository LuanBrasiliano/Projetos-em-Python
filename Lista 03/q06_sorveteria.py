#Você está desenvolvendo um sistema para uma sorveteria que permite aos clientes escolherem seus sabores de sorvete favoritos e montar seus próprios sorvetes. Crie uma função que ajude os clientes a escolher os sabores de sorvete.

#Crie uma função chamada escolher_sabores que aceite uma lista de sabores de sorvete como argumento. A função deve escolher aleatoriamente um sabor de sorvete da lista e retorná-lo.

sabores_disponíveis = ["Baunilha", "Chocolate", "Morango", "Creme", "Café", "Chocolate com menta", "Milho"]

import random
def escolhe_sabores(sabores):
    sabor = "";
    aleatorio = random.randint(0,(len(sabores)-1));
    sabor = sabor + sabores[aleatorio];
    print(sabor);