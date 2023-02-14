import re


def just_numb(cnpj):
    # Function will strip all unwanted characters.
    return re.sub(r'[^0-9]', '', cnpj)


def sequential(cnpj):
    # Function that makes it impossible to repeat numbers 14 times, causing incorrect validation in the app.
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def valid(cnpj):
    # Function that receives the data from the previous functions to analyze numerical sequence

    cnpj = just_numb(cnpj)

    try:
        # If it returned False in the "sequential" function, it closes the app with "not valid"
        if sequential(cnpj):
            return False
    except:
        return False

    try:
        # This function will return the validator values of the "digit_analysis" function.
        new_cnpj = digit_analysis(cnpj=cnpj, digit=1)
        new_cnpj = digit_analysis(cnpj=new_cnpj, digit=2)

    except Exception as e:
        return False

    if new_cnpj == cnpj:
        # If the variable "new_cnpj" is equal to "cnpj", it will return true and validate the information.
        return True
    else:
        return False


def digit_analysis(cnpj, digit):
    # This function will use an algorithm for validating the cnpj.

    regressive = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    if digit == 1:
        regressivos = regressive[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        regressivos = regressive
        new_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0

    return f'{new_cnpj}{digit}'


def format(cnpj):
    cnpj = just_numb(cnpj)
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
