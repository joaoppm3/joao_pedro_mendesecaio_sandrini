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