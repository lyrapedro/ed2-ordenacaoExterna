import math
import mergeSort


def IntercalacaoBalanceada(nomeDoArquivo):
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


def Intercalacao(fitaEntrada, fitaSaida, numRegistros):
    n = numRegistros
    # Num de registros no bloco
    m = 3
    # Num de fitas
    f = 6

    passada = 0

    # Passadas necessarias no loop:
    while passada <= math.ceil(math.log(n / m) / math.log(f)):
        # Abre os arquivos para leitura
        fita1 = open(fitaEntrada[0], 'r')
        fita2 = open(fitaEntrada[1], 'r')
        fita3 = open(fitaEntrada[2], 'r')
        # Abre e fecha as 3 primeiras fitas de saida para inicializar
        fita4 = open(fitaSaida[0], 'w')
        fita5 = open(fitaSaida[1], 'w')
        fita6 = open(fitaSaida[2], 'w')
        fita4.close()
        fita5.close()
        fita6.close()

        fita1Fechado = 0
        fita2Fechado = 0
        fita3Fechado = 0

        # fitaFechado = 0 - A variavel percorre o arquivo
        # fitaFechado = 1 - A variavel encontrou um separador de blocos, entao ela tera que esperar as outras chegarem tambem para voltarem a ser 0
        # fitaFechado = 2 - A variavel chegou no final do arquivo

        # LinhaDo1 - Variavel que percorre o arquivo 1 dos 3 a ser comparados
        # LinhaDo2 - Variavel que percorre o arquivo 2 dos 3 a ser comparados
        # LinhaDo3 - Variavel que percorre o arquivo 3 dos 3 a ser comparados

        # Setando o indice para 0
        i = 0
        while fita1Fechado != 2 and fita2Fechado != 2 and fita3Fechado != 2:
            fita4 = open(fitaSaida[i], 'a')

            # Le a linha do primeiro arquivo
            linhaDo1 = fita1.readline()
            # Tratamento caso a linha seja igual a um separador de blocos
            if linhaDo1 == '-\n':
                linhaDo1 = fita1.readline()
            # Se for igual a '' quer dizer que chegou no final do arquivo
            if linhaDo1 != '':
                linhaDo1 = int(linhaDo1)
                fita1Fechado = 0
            else:
                fita1.close()
                fita1Fechado = 2
                linhaDo1 = 99999  # LinhaDo1 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas
            #####
            # Le a linha do segundo arquivo
            linhaDo2 = fita2.readline()
            if linhaDo2 == '-\n':
                linhaDo2 = fita2.readline()
            if linhaDo2 != '':
                linhaDo2 = int(linhaDo2)
                fita2Fechado = 0
            else:
                fita2.close()
                fita2Fechado = 2
                linhaDo2 = 99999
            linhaDo3 = fita3.readline()
            if linhaDo3 == '-\n':
                linhaDo3 = fita3.readline()
            if linhaDo3 != '':
                linhaDo3 = int(linhaDo3)
                fita3Fechado = 0
            else:
                fita3.close()
                fita3Fechado = 2
                linhaDo3 = 99999

            while fita1Fechado == 0 or fita2Fechado == 0 or fita3Fechado == 0:
                # Se linhaDo1 for menor que linhaDo2 e linhaDo3:
                if fita1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    # Converte para string e pula uma linha
                    linhaDo1 = str(linhaDo1) + '\n'
                    # Escreve a linha no final do arquivo
                    fita4.writelines(linhaDo1)
                    linhaDo1 = fita1.readline()
                    if linhaDo1 == '':
                        fita1.close()
                        fita1Fechado = 2
                        linhaDo1 = 99999
                    if linhaDo1 == "-\n":
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        fita1Fechado = 1
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo1 = 99999
                    else:
                        # Converta para inteiro, para continuar as comparacoes
                        linhaDo1 = int(linhaDo1)
                # Se linhaDo2 for menor que linhaDo1 e linhaDo3:
                if fita2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    # Converte para string e pula uma linha
                    linhaDo2 = str(linhaDo2) + '\n'
                    # Escreve a linha no final do arquivo
                    fita4.writelines(linhaDo2)
                    linhaDo2 = fita2.readline()
                    if linhaDo2 == '':
                        fita2.close()
                        fita2Fechado = 2
                        linhaDo2 = 99999
                    if linhaDo2 == '-\n':
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo2 = 99999
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        fita2Fechado = 1
                    else:
                        # Se nao, converta para inteiro, para continuar as comparacoes
                        linhaDo2 = int(linhaDo2)
                # Se linhaDo3 for menor que linhaDo1 e linhaDo2:
                if fita3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    # Converte para string e pula uma linha
                    linhaDo3 = str(linhaDo3) + '\n'
                    # Escreve a linha no final do arquivo
                    fita4.writelines(linhaDo3)
                    linhaDo3 = fita3.readline()
                    if linhaDo3 == '':
                        fita3.close()
                        fita3Fechado = 2
                        linhaDo3 = 99999
                    if linhaDo3 == "-\n":
                        # Atribui um valor alto a linha, para continuar as comparacoes
                        linhaDo3 = 99999
                        # ArqFechado = 1, para nao entrar mais nesse bloco
                        fita3Fechado = 1
                    else:
                        # Se nao, converta para inteiro, para continuar as comparacoes
                        linhaDo3 = int(linhaDo3)
            # Se nao estiver chegado no final dos 3 arquivos:
            if fita1Fechado != 2 and fita2Fechado != 2 and fita3Fechado != 2:
                # Escreva o separador do bloco
                fita4.writelines('-\n')
                fita4.close()
            if i == 2:                                                  # Mudanca de indice para mudar de arquivo destino
                i = 0
            else:
                i += 1

        # Abre os arquivos para leitura
        fita4 = open(fitaSaida[0], 'r')
        fita5 = open(fitaSaida[1], 'r')
        fita6 = open(fitaSaida[2], 'r')
        # Abre e fecha as 3 primeiras fitas para zera-las
        fita11 = open(fitaEntrada[0], 'w')
        fita12 = open(fitaEntrada[1], 'w')
        fita13 = open(fitaEntrada[2], 'w')

        fita11.close()
        fita12.close()
        fita13.close()

        fita1Fechado = 0
        fita2Fechado = 0
        fita3Fechado = 0
        # Setando o indice para 0
        i = 0

        # Mesma logica da parte 2
        while fita1Fechado != 2 and fita2Fechado != 2 and fita3Fechado != 2:
            arq = open(fitaEntrada[i], 'a')

            linhaDo1 = fita4.readline()
            if linhaDo1 != '':
                linhaDo1 = int(linhaDo1)
                fita1Fechado = 0
            else:
                fita1.close()
                fita1Fechado = 2
                linhaDo1 = 9000
            #####
            linhaDo2 = fita5.readline()
            if linhaDo2 != '':
                linhaDo2 = int(linhaDo2)
                fita2Fechado = 0
            else:
                fita2.close()
                fita2Fechado = 2
                linhaDo2 = 9000
            ####
            linhaDo3 = fita6.readline()
            if linhaDo3 != '':
                linhaDo3 = int(linhaDo3)
                fita3Fechado = 0
            else:
                fita3.close()
                fita3Fechado = 2
                linhaDo3 = 9000

            while fita1Fechado == 0 or fita2Fechado == 0 or fita3Fechado == 0:
                if fita1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    linhaDo1 = str(linhaDo1) + '\n'
                    arq.writelines(linhaDo1)
                    linhaDo1 = fita4.readline()
                    if linhaDo1 == '':
                        fita1.close()
                        fita1Fechado = 2
                        linhaDo1 = 99999
                    if linhaDo1 == "-\n":
                        fita1Fechado = 1
                        linhaDo1 = 99999
                    else:
                        linhaDo1 = int(linhaDo1)
                if fita2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    linhaDo2 = str(linhaDo2) + '\n'
                    arq.writelines(linhaDo2)
                    linhaDo2 = fita5.readline()
                    if linhaDo2 == '-\n':
                        linhaDo2 = 99999
                        fita2Fechado = 1
                    if linhaDo2 == '':
                        fita2.close()
                        fita2Fechado = 2
                        linhaDo2 = 99999
                    else:
                        linhaDo2 = int(linhaDo2)
                if fita3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    linhaDo3 = str(linhaDo3) + '\n'
                    arq.writelines(linhaDo3)
                    linhaDo3 = fita6.readline()
                    if linhaDo3 == "-\n":
                        linhaDo3 = 99999
                        fita3Fechado = 1
                    if linhaDo3 == '':
                        fita3.close()
                        fita3Fechado = 2
                        linhaDo3 = 99999
                    else:
                        linhaDo3 = int(linhaDo3)
            if fita1Fechado != 2 and fita2Fechado != 2 and fita3Fechado != 2:
                arq.writelines('-\n')
                arq.close()
            if i == 2:
                i = 0
            else:
                i += 1
        ##

        passada += 1  # Incrementa +1  na passada


IntercalacaoBalanceada('entrada')
