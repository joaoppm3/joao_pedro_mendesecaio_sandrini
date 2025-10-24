from funcoes import *
navios = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

frota_jogador = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}

for tipo, tamanho_navio, quantidade in navios:
    posicionados = 0
    while posicionados < quantidade:
        print(f"Insira as informações referentes ao navio {tipo} que possui tamanho {tamanho_navio}")
        linha_navio = int(input("Linha: "))
        coluna_navio = int(input("Coluna: "))

        if tipo == "submarino":
            direcao = "vertical"
        else:
            opcao = int(input("[1] Vertical [2] Horizontal >"))
            if opcao == 1:
                direcao = "vertical"
            else:
                direcao = "horizontal"

        if posicao_valida(frota_jogador, linha_navio, coluna_navio, direcao, tamanho_navio):
            frota_jogador = preenche_frota(frota_jogador, tipo, linha_navio, coluna_navio, direcao, tamanho_navio)
            posicionados += 1
        else:
            print("Esta posição não está válida!")

print(frota_jogador)

