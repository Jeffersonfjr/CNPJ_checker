import validator as fd

while True:

    cnpj = input('Enter a valid CNPJ please: ')

    if fd.valid(cnpj):
        print(f'\n{fd.format(cnpj)} is valid\n')
    else:
        print(f'\n{fd.format(cnpj)} is not valid\n')

    x = input('Do you want to do validation?:\n'
              '[N] -  No\n')

    if x.lower() == 'n':
        break


