'''
Programa para criação de fomulario, teste
'''
nome = input('Entre com o seu nome: ')
sobrenome = input('Entre com seu sobrenome: ')
dia_nascimento = input('Dia de Nascimento: ')
mes_nascimento = input('Mes de nascimento: ')
ano_nascimento = input('Ano de nascimento: ')
universidade = input('qual a sua universidade: ')

e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + universidade + '.br'
senha = str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))

print('O seu email é: {}'. format(e_mail))
print('A sua senha é: {}'. format(senha))


