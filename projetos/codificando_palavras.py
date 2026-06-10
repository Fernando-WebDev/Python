def codificador():

    try:

        l = []
        l_asc = []
        l_asc_codificado = []
        nomes = ''
        quant = int(input('Quantos nomes pretende digiar? '))
        key = int(input("Insira um chave de codificação: "))

    except  ValueError:
        print("Insira a quantidade em números inteiros!\n................................................")
        return codificador()
 
    else:

        rep = 0
        while rep < quant:
            nomes = input('Digite um nome: ')
            l.append(nomes)
            rep += 1

        for itens in l:
            acomulado = ''
            acomulado_cod = ''
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
                else:
                     acomulado_cod += str(asc)

            l_asc.append(acomulado)
            l_asc_codificado.append(acomulado_cod)
        print(l)
        print(l_asc)
        print(l_asc_codificado)

codificador()