arq2 = open('Att/46.txt(m.a)', 'w', encoding='utf-8') #write -> escrever
arq2.write('Olá mi hermano\n')
ola = 'Hey\n'
arq2.write(ola)
arq2.close()

arq2 = open('Att/46.txt(m.a)', 'r', encoding='utf-8') #read -> ler
print(arq2.read())

arq2 = open('Att/46.txt(m.a)', 'a', encoding='utf-8') #append -> acrescentar
arq2.write('1 + 1 = 3')

arq2 = open('Att/46.txt(m.a)', 'r', encoding='utf-8') #read -> ler
print(arq2.read())