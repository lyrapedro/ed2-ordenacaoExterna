# ed2-ordenacaoExterna
Trabalho de Ordenação em Memória Externa utilizando o Método: Intercalação balanceada de Vários Caminhos. Estrutura de Dados ll - Prof. Saulo Ribeiro

Este programa realiza a Intercalacao Balanceada de Vários Caminhos, utilizando:
- 1 arquivo com dados de entrada
- 6 fitas auxiliares

O programa é dividido em 3 funções:

ArmazenarValoresDeEntradaNoVetor:
Armazena os valores do arquivo de entrada dentro de um vetor auxiliar que será usado para realizar as operações nas fitas de entrada.

DistribuirEntreAsFitasDeEntrada:
O arquivo com os dados de entrada é divido em blocos de 3 e colocado nas 3 primeiras fitas, ordenadamente

Intercalacao:
Aqui está contida a lógica principal do programa.
um loop é executado enquanto o número de "passadas" não alcança o resultado do cálculo.
Os registros até o separador de cada arquivo (" - "), é considerado um bloco, esses blocos são ordenados e colocado nas próximas 3 fitas. 
O programa termina com todos os registros ordenados na 1ª fita.
