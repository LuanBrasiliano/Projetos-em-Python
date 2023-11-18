#Você está desenvolvendo uma aplicação de gerenciamento de eventos para auxiliar pessoas a planejarem seus compromissos mensais. Para isso, é essencial criar uma função que gera um calendário mensal para que os usuários possam visualizar os dias da semana e planejar seus eventos.

#Crie uma função chamada gerar_calendario_mensal que aceita dois argumentos: o ano e o mês para o qual você deseja gerar um calendário. A função deve retornar uma representação do calendário do mês especificado, exibindo os dias da semana e os números dos dias do mês.

import calendar #lembre-se da lista passada
def gerar_calendario(ano,mes):
    print(calendar.month(ano,mes));