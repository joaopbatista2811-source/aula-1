nome = input('qual seu nome? ')
print('Ola,',nome, ', seja bem vindo ao jogo')
senha = input('qual a senha? ')
print('sua senha é: ',senha)
dominio = input('qual seu dominio?')
print('O seu dominio é: ', dominio)
email = nome + '@' + dominio
print('Seu email é: ',email)

palavra = 'jaca'
#como colocar a string como toda maiuscula
print('colocando o texto em maiuscula: ',palavra.upper())

PALAVRA = 'JACA'
#colocar a string como toda minuscula
print('colocando o texto em minuscula: ', PALAVRA.lower())

#contar caracter da string
palavra_contar = 'banana'
print('contar a letra b', palavra_contar.count('b') )
print('contar a letra a', palavra_contar.count('a') )
print('contar a letra n', palavra_contar.count('n') )

#email = palavra_contar.count('a')
print('a letra a foi contada: ', palavra_contar.count('a'))

print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e'+ str(e_c) + 'i'+ str(i_c) + 'o'+ str(o_c) + 'u'+ str(u_c)
print(nova_senha)


nome = input('olá, seja bem vindo a criação do seu formulário, para começar, qual o seu nome?' )
print('Seja bem vindo, ', nome, '') 
