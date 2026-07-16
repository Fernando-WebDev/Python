def codificar():

    try:
        descodificados = []
        codificados = []
        palavra = ''
        key = int(input('Digite uma key: '))
        quant_palavras = int(input('Quantas palavras vai codificar? '))

    except ValueError:
        print('Tente Novamente!\n..............................')
        return codificar()
    
    else:
        x = 0
        while x < quant_palavras:
            palavra += input('Digite sua palavra/frase: ')
            descodificados.append(palavra)
            x += 1

        for item in descodificados:
            for letra in item:
                letra_asc = ord(letra)
                cod = 122 - letra_asc
                
                if 97 <= letra_asc <= 122:
                    