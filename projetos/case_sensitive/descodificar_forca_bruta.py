def descodificar_forca_bruta():

    try:

        key = int(input('Insira a chave: '))

        # Lista com as 50 palavras mais usadas do português
        palavras_mais_usadas = [
            "que", "de", "a", "o", "e", "do", "da", "em", "um", "para",
            "é", "com", "não", "uma", "os", "no", "se", "na", "por", "mais",
            "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "à",
            "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já", "está",
            "eu", "também", "só", "pelo", "pudes", "até", "isso", "ela", "entre", "depois"
        ]

    except ValueError:
        print('Insira uma senha numerica!...............................')
        return descodificar_forca_bruta()

    else:

        bruta = open('/home/fer/Documentos/GitHub/Python/projetos/case_sensitive/crip.txt', 'w')

        descifragem = ''
        #Lendo o arquivo
        for linha in bruta:
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
        #Fechando o arquivo
        bruta.close()