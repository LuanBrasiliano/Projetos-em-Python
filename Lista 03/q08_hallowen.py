#Crie uma função chamada contar_doces que aceite uma lista de tipos de doces como argumento. A função deve contar quantas vezes cada tipo de doce aparece na lista e retornar um dicionário onde as chaves são os tipos de doces e os valores são as quantidades correspondentes.

doces_coletados = ["chocolate", "chocolate", "pirulito", "caramelo", "pirulito", "pirulito"]

def conta_doces(doces):
    dicionario = {};
    for item in doces:
        if not(item in dicionario):
            dicionario[item] = doces.count(item);
    print(dicionario);