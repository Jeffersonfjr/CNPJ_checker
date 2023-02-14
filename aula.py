import funcoes as fd

while True:
    # p_cnpj = input('Digite o CNPJ desejado:\n')
    #
    # if len(p_cnpj) <= 12:
    #     print('Por favor, digite um numero valido.\n')
    #     continue
    #
    # cnpj = fd.arrumar(p_cnpj)
    # teste = fd.digito1(cnpj[:12])
    # teste = fd.digito2(teste)
    #
    # if not teste.isdigit():
    #     print('Por favor, digite um numero valido.\n')
    #     continue
    #
    # if fd.verdadeiro(cnpj, teste):
    #     print(f'\nO CNPJ: {p_cnpj} é valido\n')
    # else:
    #     print(f'\nO CNPJ: {p_cnpj} é invalido\n')
    # cnpj = input('Digite um cnpj:\n')
    cnpj = fd.gera()

    while True:

        if fd.valida(cnpj):
            print(f'{cnpj} é válido')
        else:
            print(f'{cnpj} é inválido')

        x = input('Tentar novamente:\n')

        if x.lower() == 'n':
            break

        cnpj = fd.gera()