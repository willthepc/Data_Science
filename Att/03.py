produto = {
    'Samsung': {'preco': 1200},
    'LG': {'preco': 700},
    'Iphone': {'preco': 2400}
}

produto['Samsung']['quantidade'] = 23
produto['LG']['quantidade'] = 10
produto['Iphone']['quantidade'] = 5

produto['LG']['quantidade'] += 10
verificar = 'Samsung' in produto
print(verificar)
print(produto['LG']['quantidade'])
for i,j in produto.items():
    print(f'{i} -> {j}')
