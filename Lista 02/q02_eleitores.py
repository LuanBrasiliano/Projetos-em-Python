# Você deseja criar um programa que ajude os eleitores a entenderem se são obrigados a votar ou se têm apenas o direito de votar com base em sua idade.  Faça um programa que ao digitar a idade, ele diga se a pessoa já pode votar, se é obrigatório ou não

#* Faixas de idade e output esperados:*
#  - até 16 anos: "Não pode votar"
#  - Entre 16 e 18 anos: "Direito a voto, mas não obrigatório"
#  - Entre 16 e 70: "Voto Obrigatório"
#  - A partir de 70: "Direito a voto, mas não obrigatório"

print("Digite a idade que deseja verificar:\n");
idade = int(input("Digite uma idade:\n"));
if(idade<=16):
    print("Não pode votar:");
elif((idade>16) and (idade<70)):
    print("Voto obrigatorio.");
else:
    print("Direito a voto, mas não obrigatório.");