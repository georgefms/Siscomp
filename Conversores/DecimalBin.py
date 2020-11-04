#Programa de conversão de decimal para Binario
#implementação do metodo de divisoes consecutivas
#primeiro é definida a função
#Em seguida temos a condição que permite a continuação do laço
#caso a  condição seja verdadeira temos a chamada recursiva da função
#a qual usa o valor de entrada e obtem o resultado da divisão inteira
#em seguida temos a impressão do resto da divisão que nada mais e que o numero convertido


def DecBin(num):

  if (num > 1):
    decBin(num//2)

  print(num%2, end='')
  
  
#exemplo de uso da funcao
decBin(37)
