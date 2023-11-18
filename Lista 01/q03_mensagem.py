#Você é um detetive de palavras, conhecido por desvendar enigmas usando manipulação de texto. Hoje, você enfrenta um novo mistério envolvendo uma mensagem secreta. Sua missão é decifrar essa mensagem usando operações com texto em Python.

#Mistério da Mensagem Secreta:

#Você recebeu a seguinte mensagem secreta: #Mistério: @lg0 3$c0nd3 3$t@ m3n$@g3m. P0d3r1@$ d3c1fr@-l@?

msg = str(input("Digite a mensagem a ser criptografada"));
new_msg = msg.strip();
other = new_msg.replace('@','a').replace('3','e').replace('$','s').replace('0','o').replace('1','i');
other = other.upper();
print("A mensagem é: ", other); 