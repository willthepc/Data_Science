import os
os.system('cls')
import pandas as pd

df = pd.read_csv('Att/salario.csv')
# abrindo dataset em uma unica linha
f = open('Att/salario.csv', 'r')
data = f.read()
rows = data.split('\n')

#dividindo o arquivo em colunas (posso usar o pandas)
f = open('Att/salario.csv', 'r')
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)
    first_row = full_data[0]
    
count = 0
for now in full_data:
    count += 1
    
print(count)
print(df.shape) # forma com panda mais facil
count = 0
for column in first_row:
    count = count + 1

print(count)