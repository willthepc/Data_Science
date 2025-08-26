#preparar arquivo para leitura
arq1 = open('Att/45.txt', 'r')

#ler o arquivo
print(arq1.read())

#contar caracteres
print(arq1.tell())

#retornar para inicio do arquivo
print(arq1.seek(0,0))

#ler primeiros 23 caracteres
print(arq1.read(23))

