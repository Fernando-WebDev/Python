def codificador():

    try:
        #Coleta e definição de dados
        letras = []
        letras_cod = []
        nomes = ''
        quant = int(input('Quantos nomes pretende digiar? '))
        key = int(input("Insira um chave de codificação: "))
        while key > 26:
            key = key % 26

    #Exvessão para valores errados
    except  ValueError:
        print("Insira a quantidade em números inteiros!\n................................................")
        return codificador()
 
    else:

        #Coleta de palavras a codificar
        rep = 0
        while rep < quant:
            nomes = input('Digite um nome: ')
            letras.append(nomes)
            rep += 1

        #Analisando palavra por palavra
        for itens in letras:
            #Descodificando letra por letra
            palavra_cod = ''
            for letra in itens:
                nova_letra = ''

                if 'A'<= letra <= 'Z':
                    nova_letra = (ord(letra) + key) % 26
                    nova_letra = chr(90 - nova_letra)

                elif 'a' <= letra <= 'z':
                    nova_letra = (ord(letra) + key) % 26
                    nova_letra = chr(122 - nova_letra)

                else: 
                    nova_letra = letra

                palavra_cod += nova_letra
            #Adicionando as palavras codificadas a lista
                
            letras_cod.append(palavra_cod)
            
        
        #Mostrando os valores finais ao usuario
        print('Suas palavras: ', letras)
        print('Suas palavras codificadas: ', letras_cod)

        #Adicionando a criptografia a um arquivo de texto
        # criptografia = open('/home/fer/Documentos/GitHub/Python/crip.txt', 'w')
        # sentence = ''
        # for i in letras_cod:
        #     sentence = i
        #     #Adicionando nova linha ao arquivo
        #     criptografia.write(sentence)
        # #Fechando o arquivo
        # criptografia.close()

codificador()