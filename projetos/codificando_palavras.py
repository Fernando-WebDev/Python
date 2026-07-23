def codificador():

    try:
        #Coleta e definição de dados
        l = []
        l_letras_cod = []
        l_asc = []
        l_asc_codificado = []
        nomes = ''
        quant = int(input('Quantos nomes pretende digiar? '))
        key = int(input("Insira um chave de codificação: "))

    #Exvessão para valores errados
    except  ValueError:
        print("Insira a quantidade em números inteiros!\n................................................")
        return codificador()
 
    else:

        #Coleta de palavras a codificar
        rep = 0
        while rep < quant:
            nomes = input('Digite um nome: ')
            l.append(nomes)
            rep += 1

        #Analisando palavra por palavra
        for itens in l:
            acomulado = ''
            acomulado_cod = ''
            codificacao = ''

            #Descodificando letra por letra
            palavar_cod = ''
            for letra in itens:
                nova_letra = ''

                if 'A'<= letra <= 'Z':
                    nova_letra = ord(letra) + key
                    nova_letra = chr(90 - nova_letra)

                elif 'a' <= letra <= 'z':
                    nova_letra = ord(letra) - 97
                    nova_letra = chr(122 - nova_letra)

                else: 
                    nova_letra = letra

            palavar_cod += nova_letra
            #Adicionando as palavras codificadas a lista
            l_letras_cod.append(codificacao)
            l_asc.append(acomulado)
            l_asc_codificado.append(acomulado_cod)
        
        #Mostrando os valores finais ao usuario
        print('Suas palavras: ', l)
        print('Suas palavras codificadas: ', l_letras_cod)
        print('ASCII: ', l_asc)
        print('ASCII codificado: ', l_asc_codificado)

        #Adicionando a criptografia a um arquivo de texto
        # criptografia = open('/home/fer/Documentos/GitHub/Python/crip.txt', 'w')
        # sentence = ''
        # for i in l_letras_cod:
        #     sentence = i
        #     #Adicionando nova linha ao arquivo
        #     criptografia.write(sentence)
        # #Fechando o arquivo
        # criptografia.close()

codificador()