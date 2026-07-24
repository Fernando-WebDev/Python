def altbash_variacao():

    try:
        para_descod = []
        cod = []
        palavra = ''
        key = input('Digite um combinação de inversão de valores:\n...............\nEx.: aO,iN,uq,nx,').split(',')
        quant = int(input('Quantas palavras/frases vai digitar? '))

    except ValueError:
        print('Informe um valor númerico!.........................')
        return altbash_variacao()
    
    else:

        rep = 0
        while rep < quant:
            palavra = input('Digite sua palavra/frase: ')
            para_descod.append(palavra)
            rep += 1

        # for linha in para_descod:

        #     for letra in linha:
        #         if letra == key[0]:
