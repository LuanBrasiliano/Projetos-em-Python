#**Bad Romance:** 

#De volta a 2009. Tem umas músicas com um refrão tão gostosinho que fica martelando na nossa mente, então vamos aproveitar para analisar e exercitar nossas skills de programação. Escreva um código que conte quantas vezes a letra "a" aparece em duas estrofes do famoso hit de Lady Gaga:

letra = "a";
contador = 0;
ad_romance = """Rah, rah-ah-ah-ah
                 Roma, roma-ma
                 Gaga, ooh-la-la
                 Want your bad romance

                 Rah, rah-ah-ah-ah
                 Roma, roma-ma
                 Gaga, ooh-la-la
                 Want your bad romance""";
bad_romance = ad_romance.lower();
list = bad_romance.split();
for i in list:
    for j in i:
        if(j == letra):
            contador += 1;
print("A quantidade de Letras {} é {}:".format(letra,contador));