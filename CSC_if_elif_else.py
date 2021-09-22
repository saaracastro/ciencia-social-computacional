'''Esse script é um exercício de if, elif e else.'''
#outra forma de comentar
nota1 = float(input('digite a primeira nota:'))
nota2 = float(input('digite a segunda nota:'))
media = (nota1 + nota2) / 2
print(f'sua média é {media}')
if media < 4.9:
    print('Reprovado')
elif media > 5.0 and media < 6.9:
    print('Recuperação')
elif media == 10.0:
    print('Parabéns!!')
else:
    print('Aprovado/a!')
print('final do programa')

