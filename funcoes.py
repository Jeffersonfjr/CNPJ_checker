"""
04.252.011/0001-10
40.688.134/0001-61
71.506.168/0001-11
12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1   X   X
5   4   3   2   9   8   7   6   5   4   3   2
0  16   6  10  18   0   7   6   0   0   0   2  = 65
formula -> 11 - ( 65 % 11) = 1


0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0  20   8  15   4   0   8   7   0   0   0   3   2   = 67  ##
Formula -> 11 - (67 % 11) = 11  (Resultado maior que 9, é = a 0)

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Orifginal      = 04.252.011/0001-10

Recap.
543298765432 -> Primeiro Digito
6543298765432 -> Segundo Digito Digito
"""

# def junta(v1, v2):
#     v3 = v1 + v2
#     return v3
#
#
# def digito1(cnpj):
#     if not '.' in cnpj or not '/' in cnpj or not '-' in cnpj:
#         novo_cnpj = cnpj[0:15].replace('.', '').replace('/', '').replace('-', '')
#     else:
#         novo_cnpj = cnpj
#     soma_d1 = 0
#     contador = 5
#     for i in novo_cnpj:
#         i = int(i)
#         i = i * contador
#         soma_d1 += i
#         contador -= 1
#
#         if contador < 2:
#             contador = 9
#
#     digito1 = str(11 - (soma_d1 % 11))
#
#     if int(digito1) > 9:
#         digito1 = str(0)
#
#     novo_cnpj = novo_cnpj + digito1
#
#     return novo_cnpj
#
#
# def digito2 (cnpj):
#     contador = 6
#     soma_d2 = 0
#     for i in cnpj:
#         i = int(i)
#         i = i * contador
#         soma_d2 += i
#         contador -= 1
#
#         if contador < 2:
#             contador = 9
#
#     digito2 = str(11 - (soma_d2 % 11))
#     if int(digito2) > 9:
#         digito2 = str(0)
#
#     cnpj = cnpj + digito2
#
#     return cnpj
#
#
# def verdadeiro(cnpj, cnpj_testeado):
#     cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
#
#     if cnpj == cnpj_testeado:
#         return True
#     else:
#         return False
#
#
# def arrumar(cnpj):
#     cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
#
#     return cnpj

import re
import random as rd

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = apenas_numeros(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = REGRESSIVOS[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def gera():
    digito1 = str(rd.randint(0, 9))
    digito2 = str(rd.randint(0, 9))
    bloco2 = str(rd.randint(100, 999))
    bloco3 = str(rd.randint(100, 999))
    bloco4 = '0001'

    novo_numero = f'{digito1}{digito2}{bloco2}{bloco3}{bloco4}00'
    novo_numero = calcula_digito(cnpj=novo_numero,digito=1)
    novo_numero = calcula_digito(cnpj=novo_numero,digito=2)
    novo_numero=formata(novo_numero)
    return novo_numero

def formata(cnpj):
    cnpj = apenas_numeros(cnpj)
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    # 17.537.434/0001-22