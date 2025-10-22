def define_posicoes(linha,coluna,orientacao,tamanho):
    lista_posicao = []
    if orientacao == 'horizontal':
        i = 0
        while i < tamanho:
            posicao = [linha,coluna]
            lista_posicao.append(posicao)
            coluna += 1
            i += 1
    if orientacao == 'vertical':
        j = 0
        while j < tamanho:
            position = [linha,coluna]
            lista_posicao.append(position)
            linha += 1
            j += 1
    return lista_posicao

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else: 
        frota[nome_navio] = [posicoes]
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if i == linha and j == coluna: 
                if tabuleiro[i][j] == 1:
                    tabuleiro[i][j] = 'X'
                else:
                    tabuleiro[i][j] = '-'
    return tabuleiro