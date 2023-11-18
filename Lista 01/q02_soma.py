#Imagine que você é um professor de Matemática para crianças do ensino fundamental e um aluno curioso te #pergunta:

#"Professor, quanto é 13 + 15 + 16 + 6?"

#Você, é claro, não quer parecer contar nos dedos por baixo da mesa para uma pergunta tão simples. Então, #você decide mostrar toda a sua sabedoria tecnológica e recorre ao Python para dar a resposta #instantaneamente.

#Como deve ser o código para chegar ao resultado?

print("Quantos número deseja somar?");
num_total = int(input(" Quantos numero somar? "));
soma = 0;
contador = 0;
while contador < num_total:
    numero =  int(input("Digite o numero a ser somado: "));
    soma=soma+numero;
    contador=contador+1;
print("A soma é: ",soma);