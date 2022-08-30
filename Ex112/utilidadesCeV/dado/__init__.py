def leiaDinheiro(mensagem):
    validacao = False
    while not validacao:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            validacao = True
            return float(entrada)