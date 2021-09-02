from math import sqrt

ESI = 1
n = int(input('Quantos parâmetros você deseja? '))
for p in range(0, n):
    w = float()
    x0 = float()
    escolha = int(input('''
    DIGITE O NÚMERO ENTRE []
    [1] Parâmetro: Raio
    [2] Parâmetro: Densidade
    [3] Parâmetro: Velocidade de Escape
    [4] Parâmetro: Temperatura
    [5] "Caso o desejado não esteja na lista"
'''))
    if escolha == 1:
        w = 0.57
        x0 = 1
        x = float(input(f'\n O valor do parâmetro {escolha} do planeta (em relação ao da Terra): '))
        raio = x
    elif escolha == 2:
        escolha_den = str(input('Deseja calcular a densidade do planeta? [S/N] '))
        if escolha_den in 'Ss':
            massa = float(input('Digite a massa do planeta (em relação ao da Terra): '))
            if 'raio' not in globals():
                raio = float(input('Digite o raio do planeta (em relação ao da Terra): '))
            volume = (4 / 3) * 3.141592653 * (raio * 6378140) ** 3
            x = (massa * 5.9722 * (10 ** 24)) / volume
            x0 = 5494.948046903008
        else:
            x = float(input(f'\n O valor do parâmetro {escolha} do planeta: '))
            x0 = 1
        w = 1.07
    elif escolha == 3:
        if 'massa' or 'raio' not in globals():
            escolha_ve = str(input('Deseja calcular a velocidade de escape do planeta? [S/N] '))
            if escolha_ve in 'Ss':
                if 'massa' not in globals():
                    massa = float(input('Digite a massa do planeta (em relação ao da Terra): '))
                if 'raio' not in globals():
                    raio = float(input('Digite o raio do planeta (em relação ao da Terra): '))
            else:
                x = float(input(f'\n O valor do parâmetro {escolha} do planeta: '))
        x = sqrt(2 * massa * 5.9722 * (10 ** 24) * 6.674184 * (10 ** -11) / (raio * 6378140))
        x0 = 11179.805121191846
        w = 0.70
    elif escolha == 4:
        w = 5.58
        x0 = 288
        x = float(input(f'\n O valor do parâmetro {escolha} do planeta: '))
    else:
        x0 = float(input('Digite o x0 da Terra desejado: '))
        w = float(input('Digite o w do parâmetro desejado: '))
        x = float(input(' O valor do parâmetro escolhido do planeta: '))
    div = x + x0
    if x >= x0:
        modulo = float((x - x0) / div)
    else:
        modulo = float((x0 - x) / div)
    formula = float(1 - modulo) ** (w / n)
    ESI *= formula
print(f'\nESI = {ESI}')
