def descodificador():

    def descodificar_ASCII():

        key = int(input('Insira a key: '))
        palavras_descod = []
        while key > 26:
                    key = key % 26

        #Adicionando a criptografia a um arquivo de texto
        criptografia = open('/home/fer/Documentos/GitHub/Python/crip.txt', 'r')
        #Lendo o arquivo
        for linha in criptografia:
            palavra_descod = ''

            #Descodificando letra por letra
            for letras_cod in linha:
                nova_letra = ''

                if 'A'<= letras_cod <= 'Z':
                    nova_letra = (ord(letras_cod) + key) % 26
                    nova_letra = chr(90 - nova_letra)

                elif 'a' <= letras_cod <= 'z':
                    nova_letra = (ord(letras_cod) + key) % 26
                    nova_letra = chr(122 - nova_letra)

                else: 
                    nova_letra = letras_cod

                palavra_descod += nova_letra
            #Adicionando a palavra descodificada a lista
            palavras_descod.append(palavra_descod)
        
        #Mostrando os valores descodificados
        print(f'Palavra descodificada: {palavras_descod}')

        #Fechando o arquivo
        criptografia.close()

    def descodificar_altbash():

        descod = []

        #Adicionando a criptografia a um arquivo de texto
        criptografia = open('/home/fer/Documentos/GitHub/Python/crip_altbash.txt', 'r')
        #Lendo o arquivo
        for linhas in criptografia:
            palavar_cod = ''
            for letra in linhas:
                nova_letra = ''

                if 'A'<= letra <= 'Z':
                    nova_letra = ord(letra) - 65
                    nova_letra = chr(90 - nova_letra)

                elif 'a' <= letra <= 'z':
                    nova_letra = ord(letra) - 97
                    nova_letra = chr(122 - nova_letra)

                else: 
                    nova_letra = letra

                palavar_cod += nova_letra
        
            descod.append(palavar_cod)

        #Mostrando os valores descodificados
        print(f'Palavra descodificada: {descod}')

        #Fechando o arquivo
        criptografia.close()
    
    

    escolher_metodo = int(input('Metodos:\n1-Descodicifar ASCII\n2-Descodiicar altbash simples\nOBS: Insira somente 1 ou 2!\nResposta: '))
    
    if escolher_metodo == 1:
        descodificar_ASCII()
        exit()
    elif escolher_metodo == 2:
        descodificar_altbash()
        exit()
    else:
        print('Informação invalida! Tente novamente.\n.........................................')
        return descodificador()

    
descodificador()