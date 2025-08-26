perguntas = [
    ("Digite o campeão brasileiro de 2023: ", "palmeiras"),
    ("Em qual clube europeu o Cristiano Ronaldo jogou antes de retornar ao United em 2021: ", "juventus"),
    ("Qual país sediou a copa do mundo de 2018: ", "rússia"),
    ("Qual é o maior artilheiro da história da Seleção Brasileira? ", "neymar"),
    ("Em que ano o Brasil foi campeão da Copa do Mundo pela última vez? ", "2002"),
    ("Quantos jogadores um time de futebol tem em campo? ", "11")
]

for texto, resposta_certa in perguntas:
    acertou = False
    for tentativa in range(3):
        resposta = input(texto).strip().lower()
        if resposta == resposta_certa:
            print("Parabéns, você acertou!")
            acertou = True
            break
        else:
            print(f"Errado. Tentativas restantes: {2 - tentativa}")
    
    if not acertou:
        print(f"Você errou todas as tentativas. A resposta correta era: {resposta_certa.capitalize()}\n")