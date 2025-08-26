produtos = ['feijão', 'arroz', 'macarrão']
x = input('Escolhe o inicio: ')
x.lower()
for i in produtos:
    print(i.startswith(x))