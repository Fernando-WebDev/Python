def descodificador():
    
    try:
        #coleta e definição de dados
        palavras_cod = []
        palavras_descod = []
        valores_asc_descod = []
        palavras = ''
        key = int(input('Dgite a key: '))
        quantidade_palavras = int(input('Quantidade de palavras que deseja descodificar: '))

    #excessão para valores errados
    except ValueError:
        print('Informações invalidas! favor digitar somente números.\n.................................................')
        return descodificador()
    
    else:
        
        #Coleta de palavras códificadas
        rep = 0
        while rep < quantidade_palavras:
            palavras = input('Digite a palavra codificada: ')
            rep += 1
            palavras_cod.append(palavras)

        #Analise das palavras códificadas
        for itens in palavras_cod:
            palavra_descod = ''
            asc_descod = ''

            #Descodificando letra por letra
            for letras_cod in itens:
                asc_descod += str(ord(letras_cod) - key)
                palavra_descod += chr(ord(letras_cod) - key)
            
            #Adicionando a palavra descodificada a lista
            palavras_descod.append(palavra_descod)
            valores_asc_descod.append(asc_descod)

        #Mostrando os valores descodificados
        print(palavras_descod)
        print(valores_asc_descod)

descodificador()