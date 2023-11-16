#Você descobriu um sebo perto da sua casa e resolve dar uma olhada e encontra muitos títulos interessantes. Mas como você não está nadando em dinheiro, terá que fazer algumas escolhas. 
#- Escreva um programa que retorne se você deverá comprar ou não o livro, considerando que:
#  - Ele precisa estar na sua wishlist (nada de comprar por impulso);
#  - O preço do sebo deve ser mais barato do que na internet.

#a) Você deverá comprar Moby Dick?

#b) Você deverá comprar Crime e Castigo?

#c) Você deverá comprar a Odisseia?

#####SEU CODIGO COMECA AQUI#####
def compra_livro(livro):
    wishlist = ['Moby Dick', 'Helena', 'A Origem das Espécies', 'Grande Sertão: Veredas', 'Odisseia', 'Rápido e Devagar', 'Sidarta'];
    precos_sebo = {'Odisseia':50, 'Jane Eyre':61, 'A Divina Comédia': 56, 'Helena':10, 'Moby Dick':55, 'Crime e Castigo':20};
    precos_internet = {'Odisseia':30, 'Jane Eyre':32, 'A Divina Comédia': 22, 'Helena':26, 'Moby Dick':145, 'Crime e Castigo':80};
    if(livro in wishlist):
        if((livro in precos_sebo) and (livro in precos_internet)):
            if(precos_sebo[livro]<precos_internet[livro]):
                return "Deve comprar o livro";
            else:
                return "Não deve comprar o livro";
        else:
            return "Livro não foi encontrado na internet ou no sebo";
    else:
        return "Livro não está na sua wishlist";

print(compra_livro('Moby Dick'));
print(compra_livro('Crime e Castigo'));
print(compra_livro('Odisseia'));