#as variáveis
av1 = float(input('Digite sua nota AV1 '))
av2 = float(input('Digite sua nota AV2 '))
#cálculo
media = (av1 + av2) / 2
#mensagem na tela
if(media == 10):
  print('Sua média é ', media,'Aprovado com Distinção')
elif(media >= 7):
  print('Sua média é ', media,'Aprovado')
else:
  print('Sua média é ', media,'Reprovado')