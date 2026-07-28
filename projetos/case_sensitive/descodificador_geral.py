def descodificador():

    def descodificar_ASCII():

        key = int(input('Insira a key: '))
        palavras_descod = []
        while key > 26:
                    key = key % 26

        #Adicionando a criptografia a um arquivo de texto
        criptografia = open('/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/crip.txt', 'r')
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
        criptografia = open('/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/crip_altbash.txt', 'r')
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
    
    def descodificar_altbash_variacao():
    
        #Printando no terminal a mensagem do arquivo "original.txt"
        arquivo = open("/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/original.txt", "r")
        mensagem = arquivo.read()
        arquivo.close()

        print(f"Mensagem Original: {mensagem}")

        #Usando as chaves do "chave.txt" para cifrar a mensagem
        arquivo = open("/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/chave.txt", "r")
        chaves = arquivo.read()
        arquivo.close

        #Separando as chaves do arquivo em uma lista
        lista_chaves = chaves.split(",")
        print(lista_chaves)

        #Definindo as trocas de letras usando a posição delas
        antes = ""
        depois = ""
        for chave in lista_chaves:
            if chave[0] in antes or chave[1] in antes: continue
            
            antes += chave[0] + chave[1]
            depois += chave[1] + chave[0]

        #Criando uma tabela das trocas e aplicando na mensagem original
        tabela_chaves = str.maketrans(antes, depois)
        cifragem = mensagem.translate(tabela_chaves)

        #Escrevendo a mensagem original cifrada no 'cifrado.txt'
        arquivo = open("/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/cifrado.txt", "w", encoding = "utf-8")
        arquivo.write(cifragem)
        arquivo.close()

        #Decifrando a mensagem do 'cifrado.txt' e escrevendo no 'decifrado.txt'
        arquivo = open("/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/cifrado.txt", "r")
        criptografada = arquivo.read()
        arquivo.close()

        decifragem = criptografada.translate(tabela_chaves)

        #Abrindo o arquivo 'decifrado.txt' e escrevendo o resultado final (precisa ser igual a mensagem original)
        arquivo = open("/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/decifrado.txt", "w", encoding = "utf-8")
        arquivo.write(decifragem)
        arquivo.close()

        if mensagem == decifragem:
            print("Deu tudo certo")
        else: 
            print("Erro")

    escolher_metodo = int(input('Metodos:\n1-Descodicifar ASCII\n2-Descodiicar altbash simples\n3-Descodificar variação do altbash\nOBS: Insira somente 1, 2 ou 3!\nResposta: '))
    
    if escolher_metodo == 1:
        descodificar_ASCII()
        exit()
    elif escolher_metodo == 2:
        descodificar_altbash()
        exit()
    elif escolher_metodo == 3:
        descodificar_altbash_variacao()
        exit()
    else:
        print('Informação invalida! Tente novamente.\n.........................................')
        return descodificador()

    
descodificador()