def descodificador():

    def descodificador_arquivo():

        key = int(input('Insira a key: '))
        palavras_descod = []


        #Adicionando a criptografia a um arquivo de texto
        criptografia = open('/home/fer/Documentos/GitHub/Python/crip.txt', 'r')
        #Lendo o arquivo
        for linha in criptografia:
            palavra_descod = ''

            #Descodificando letra por letra
            for letras_cod in linha:
                palavra_descod += chr(ord(letras_cod) - key)

            #Adicionando a palavra descodificada a lista
            palavras_descod.append(palavra_descod)
        
        #Mostrando os valores descodificados
        print(f'Palavra descodificada: {palavras_descod}')

        #Fechando o arquivo
        criptografia.close()
    
    try:

        escolher_metodo = int(input('Metodos:\n1-Descodificar arquivo\n2-Copiar e colar palavras códificadas\nOBS: Insira somente 1 ou 2!\nResposta: '))
        
        if escolher_metodo == 1:
            descodificador_arquivo()
            exit()
        elif escolher_metodo == 2:
            #coleta e definição de dados
            palavras_cod = []
            palavras_descod = []
            valores_asc_descod = []
            palavras = ''
            key = int(input('Dgite a key: '))
            quantidade_palavras = int(input('Quantidade de palavras que deseja descodificar: '))
        else:
            print('Informação invalida! Tente novamente.\n.........................................')
            return descodificador()

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