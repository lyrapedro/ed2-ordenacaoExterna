import math
import mergeSort


def intercalacaoBalanceada(nomeDoArquivo):
    arquivoEntrada = open(nomeDoArquivo + '.txt', 'r')
    vetorEntrada = ArmazenarValoresDeEntradaNoVetor(arquivoEntrada)
    arquivoEntrada.close()
    numRegistros = len(vetorEntrada)
    entrada = ["fita1.txt", "fita2.txt", "fita3.txt"]
    saida = ["fita4.txt", "fita5.txt", "fita6.txt"]

    fita1 = open(entrada[0], 'a')
    fita2 = open(entrada[1], 'a')
    fita3 = open(entrada[2], 'a')

    DistribuirEntreAsFitasDeEntrada(fita1, fita2, fita3, vetorEntrada)

    Intercalacao(entrada, saida, numRegistros)


def ArmazenarValoresDeEntradaNoVetor(arquivoEntrada):
    vetorEntrada = arquivoEntrada.readlines()

    for i, val in enumerate(vetorEntrada):
        vetorEntrada[i] = val.replace('\n', '')

    vetorEntrada = list(map(int, vetorEntrada))

    return vetorEntrada


def DistribuirEntreAsFitasDeEntrada(fita1, fita2, fita3, vetorEntrada):
    tamanhoVetor = len(vetorEntrada)

    while tamanhoVetor > 0:
        auxVetor = vetorEntrada[:3]
        aux = [0] * len(auxVetor)
        mergeSort.mergesort(auxVetor, aux, 0, len(auxVetor) - 1)

        for val in auxVetor:
            fita1.write(f'{val}\n')

        fita1.write('-\n')
        del vetorEntrada[:3]
        tamanhoVetor = len(vetorEntrada)
        if tamanhoVetor == 0:
            break

        auxVetor = vetorEntrada[:3]
        aux = [0] * len(auxVetor)
        mergeSort.mergesort(auxVetor, aux, 0, len(auxVetor) - 1)

        for val in auxVetor:
            fita2.write(f'{val}\n')

        fita2.write('-\n')
        del vetorEntrada[:3]
        tamanhoVetor = len(vetorEntrada)
        if tamanhoVetor == 0:
            break

        auxVetor = vetorEntrada[:3]
        aux = [0] * len(auxVetor)
        mergeSort.mergesort(auxVetor, aux, 0, len(auxVetor) - 1)

        for val in auxVetor:
            fita3.write(f'{val}\n')

        fita3.write('-\n')
        del vetorEntrada[:3]
        tamanhoVetor = len(vetorEntrada)
        if tamanhoVetor == 0:
            break

    fita1.close()
    fita2.close()
    fita3.close()


def Intercalacao(bolaDaVez, a, numRegistros):
    n = numRegistros
    # Numero de registros no primeiro bloco
    m = 3
    # Numero de fitas
    f = 6

    # Comeco das passadas
    passada = 0

    # Enquanto as passadas nao alcancarem o calculo, faca:
    while passada <= math.ceil(math.log(n / m) / math.log(f)):
        '''
                ## PARTE 2

        '''

        # Abre os arquivos para leitura
        arq1 = open(bolaDaVez[0], 'r')
        arq2 = open(bolaDaVez[1], 'r')
        arq3 = open(bolaDaVez[2], 'r')
        # Abre e fecha as 3 primeiras fitas para zera-las
        arq21 = open(a[0], 'w')
        arq22 = open(a[1], 'w')
        arq23 = open(a[2], 'w')
        arq21.close()
        arq22.close()
        arq23.close()

        arq1Fechado = 0
        arq2Fechado = 0
        arq3Fechado = 0

        # Se arqFechado = 0 - A variavel percorre o arquivo
        # Se arqFechado = 1 - A variavel encontrou um separador de blocos, entao ela tera que esperar as outras chegarem tambem para voltarem a ser 0
        # Se arqFechado = 2 - A variavel chegou no final do arquivo

        # LinhaDo1 - Variavel que percorre o arquivo 1 dos 3 a ser comparados
        # LinhaDo2 - Variavel que percorre o arquivo 2 dos 3 a ser comparados
        # LinhaDo3 - Variavel que percorre o arquivo 3 dos 3 a ser comparados

        # Setando o indice para 0
        i = 0
        while arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
            arq21 = open(a[i], 'a')

            # Le a linha do primeiro arquivo
            linhaDo1 = arq1.readline()
            # Tratamento caso a linha seja igual a um separador de blocos
            if linhaDo1 == '-\n':
                linhaDo1 = arq1.readline()
            # Se for igual a '' quer dizer que chegou no final do arquivo
            if linhaDo1 != '':
                linhaDo1 = int(linhaDo1)
                arq1Fechado = 0
            else:
                arq1.close()
                arq1Fechado = 2
                linhaDo1 = 9000  # LinhaDo1 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas
            #####
            # Le a linha do segundo arquivo
            linhaDo2 = arq2.readline()
            # Tratamento caso a linha seja igual a um separador de blocos
            if linhaDo2 == '-\n':
                linhaDo2 = arq2.readline()
            # Se for igual a '' quer dizer que chegou no final do arquivo
            if linhaDo2 != '':
                linhaDo2 = int(linhaDo2)
                arq2Fechado = 0
            else:
                arq2.close()
                arq2Fechado = 2
                linhaDo2 = 9000  # LinhaDo2 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas
            ####
            # Le a linha do terceiro arquivo
            linhaDo3 = arq3.readline()
            # Tratamento caso a linha seja igual a um separador de blocos
            if linhaDo3 == '-\n':
                linhaDo3 = arq3.readline()
            # Se for igual a '' quer dizer que chegou no final do arquivo
            if linhaDo3 != '':
                linhaDo3 = int(linhaDo3)
                arq3Fechado = 0
            else:
                arq3.close()
                arq3Fechado = 2
                linhaDo3 = 9000  # LinhaDo3 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas

            while arq1Fechado == 0 or arq2Fechado == 0 or arq3Fechado == 0:
                # Se linhaDo1 for menor que linhaDo2 e linhaDo3:
                if arq1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    # Converte para string e pula uma linha
                    linhaDo1 = str(linhaDo1) + '\n'
                    # Escreve a linha no final do arquivo
                    arq21.writelines(linhaDo1)
                    linhaDo1 = arq1.readline()                          # Le outra linha
                    if linhaDo1 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq1.close()
                        arq1Fechado = 2
                        linhaDo1 = 999
                    if linhaDo1 == "-\n":                               # Se chegar no final do bloco
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        arq1Fechado = 1
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo1 = 999
                    else:
                        # Se nao, converta para inteiro, para continuar as comparacoes
                        linhaDo1 = int(linhaDo1)
                # Se linhaDo2 for menor que linhaDo1 e linhaDo3:
                if arq2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    # Converte para string e pula uma linha
                    linhaDo2 = str(linhaDo2) + '\n'
                    # Escreve a linha no final do arquivo
                    arq21.writelines(linhaDo2)
                    linhaDo2 = arq2.readline()                          # Le outra linha
                    if linhaDo2 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq2.close()
                        arq2Fechado = 2
                        linhaDo2 = 999
                    if linhaDo2 == '-\n':                               # Se chegar no final do bloco
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo2 = 999
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        arq2Fechado = 1
                    else:
                        # Se nao, converta para inteiro, para continuar as comparacoes
                        linhaDo2 = int(linhaDo2)
                # Se linhaDo3 for menor que linhaDo1 e linhaDo2:
                if arq3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    # Converte para string e pula uma linha
                    linhaDo3 = str(linhaDo3) + '\n'
                    # Escreve a linha no final do arquivo
                    arq21.writelines(linhaDo3)
                    linhaDo3 = arq3.readline()                          # Le outra linha
                    if linhaDo3 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq3.close()
                        arq3Fechado = 2
                        linhaDo3 = 999
                    if linhaDo3 == "-\n":                               # Se chegar no final do bloco
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo3 = 999
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        arq3Fechado = 1
                    else:
                        # Se nao, converta para inteiro, para continuar as comparacoes
                        linhaDo3 = int(linhaDo3)
            # Se nao estiver chegado no final dos 3 arquivos:
            if arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
                # Escreva o separador do bloco
                arq21.writelines('-\n')
                arq21.close()
            if i == 2:                                                  # Mudanca de indice para mudar de arquivo destino
                i = 0
            else:
                i += 1

        print("CHEGOU NO FINAL DO 2")

        '''
            ## PARTE 3

        '''
        # Abre os arquivos para leitura
        arq21 = open(a[0], 'r')
        arq22 = open(a[1], 'r')
        arq23 = open(a[2], 'r')
        # Abre e fecha as 3 primeiras fitas para zera-las
        arq11 = open(bolaDaVez[0], 'w')
        arq12 = open(bolaDaVez[1], 'w')
        arq13 = open(bolaDaVez[2], 'w')

        arq11.close()
        arq12.close()
        arq13.close()

        arq1Fechado = 0
        arq2Fechado = 0
        arq3Fechado = 0
        # Setando o indice para 0
        i = 0

        # Mesma logica da parte 2
        while arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
            arq = open(bolaDaVez[i], 'a')

            linhaDo1 = arq21.readline()
            if linhaDo1 != '':
                linhaDo1 = int(linhaDo1)
                arq1Fechado = 0
            else:
                arq1.close()
                arq1Fechado = 2
                linhaDo1 = 9000
            #####
            linhaDo2 = arq22.readline()
            if linhaDo2 != '':
                linhaDo2 = int(linhaDo2)
                arq2Fechado = 0
            else:
                arq2.close()
                arq2Fechado = 2
                linhaDo2 = 9000
            ####
            linhaDo3 = arq23.readline()
            if linhaDo3 != '':
                linhaDo3 = int(linhaDo3)
                arq3Fechado = 0
            else:
                arq3.close()
                arq3Fechado = 2
                linhaDo3 = 9000

            while arq1Fechado == 0 or arq2Fechado == 0 or arq3Fechado == 0:
                if arq1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    linhaDo1 = str(linhaDo1) + '\n'
                    arq.writelines(linhaDo1)
                    linhaDo1 = arq21.readline()
                    if linhaDo1 == '':
                        arq1.close()
                        arq1Fechado = 2
                        linhaDo1 = 999
                    if linhaDo1 == "-\n":
                        arq1Fechado = 1
                        linhaDo1 = 999
                    else:
                        linhaDo1 = int(linhaDo1)
                if arq2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    linhaDo2 = str(linhaDo2) + '\n'
                    arq.writelines(linhaDo2)
                    linhaDo2 = arq22.readline()
                    cont = 0
                    if linhaDo2 == '-\n':
                        linhaDo2 = 999
                        arq2Fechado = 1
                    if linhaDo2 == '':
                        arq2.close()
                        arq2Fechado = 2
                        linhaDo2 = 999
                    else:
                        linhaDo2 = int(linhaDo2)
                if arq3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    linhaDo3 = str(linhaDo3) + '\n'
                    arq.writelines(linhaDo3)
                    linhaDo3 = arq23.readline()
                    if linhaDo3 == "-\n":
                        linhaDo3 = 999
                        arq3Fechado = 1
                    if linhaDo3 == '':
                        arq3.close()
                        arq3Fechado = 2
                        linhaDo3 = 999
                    else:
                        linhaDo3 = int(linhaDo3)
            if arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
                arq.writelines('-\n')
                arq.close()
            if i == 2:
                i = 0
            else:
                i += 1
        ##

        print("CHEGOU NO FINAL DO 3\n")

        passada += 1  # Incrementa +1  na passada


intercalacaoBalanceada('entrada')
