import funcoes as fd

while True:
   
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
