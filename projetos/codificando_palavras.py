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
            for letras in itens:
                asc = ord(letras)
                print(f'CARACTERS: ', letras  , ', ASCII = ', asc)
                if asc < 100:
                    acomulado += '0'
                    acomulado += str(asc)
                else:
                    acomulado += str(asc)

                asc += key
                print(f'NOVO_CARACTERS: ', chr(asc)  , ', ASCII = ', asc)
                if asc < 100:
                    acomulado_cod += '0'
                    acomulado_cod += str(asc)
                    codificacao += chr(asc)
                else:
                     acomulado_cod += str(asc)
                     codificacao += chr(asc)

            #Adicionando as palavras codificadas a lista
            l_letras_cod.append(codificacao)
            l_asc.append(acomulado)
            l_asc_codificado.append(acomulado_cod)
        
        #Mostrando os valores finais ao usuario
        print('Suas palavras: ', l)
        print('Suas palavras codificadas: ', l_letras_cod)
        print('ASCII: ', l_asc)
        print('ASCII codificado: ', l_asc_codificado)

codificador()