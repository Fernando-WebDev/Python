def descodificador():
    
    try:
        palavras_cod = []
        valores_asc = []
        palavras = ''
        asc = ''
        key = int(input('Dgite a key: '))
        quantidade_palavras = int(input('Quantidade de palavras que deseja descodificar: '))

    except ValueError:
        print('Informações invalidas! favor digitar somente números.\n.................................................')
        return descodificador()
    
    else:
        
        rep = 0
        while rep < quantidade_palavras:
            palavras = input('Digite a palavra codificada: ')
            asc = input('Digite o código ASCII codificado: ')
            rep += 1
            palavras_cod.append(palavras)
            valores_asc.append(asc)

        for itens in palavras_cod:
            for letras in itens:
                