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

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for t in frota:
        for navio in frota[t]:
            for posicao in navio: 
                l = posicao[0]
                c = posicao[1]    
                tabuleiro[l][c] = 1 
    return tabuleiro

def afundados(frota,tabuleiro):
    afundados_total = 0
    for i in frota:
        for navio in frota[i]:
            pn = 0 
            pa = 0 
            for p in navio:
                linha = p[0]
                coluna = p[1]
                pn += 1
                if tabuleiro[linha][coluna] == 'X':
                    pa += 1 
            if pn == pa:
                afundados_total += 1 
    return afundados_total

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for p in posicoes:
        if p[0] < 0 or p[0] > 9 or p[1] < 0 or p[1] > 9:
            return False
        
    posicoes_ocupadas = []
    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                posicoes_ocupadas.append(posicao)

    for p in posicoes:
        if p in posicoes_ocupadas:
            return False

    return True