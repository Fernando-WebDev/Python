def altbash_simples():

    try:
        para_descod = []
        cod = []
        palavra = ''
        quant = int(input('Quantas palavras/frases vai digitar? '))

    except ValueError:

        print('Informe um valor númerico!.........................')
        return altbash_simples()
    else:

        x = 0
        while x < quant:
            palavra = input('Digite uma palavra/frase: ')
            para_descod.append(palavra)
            x += 1

        for palavras in para_descod:
            palavar_cod = ''
            for letra in palavras:
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

        cod.append(palavar_cod)

        crip_inversa = open('/home/fer/Documentos/GitHub/Python/crip_altbash.txt', 'w')
        adicionada = ''
        for item in cod:
            adicionada = item
            crip_inversa.write(adicionada)

        crip_inversa.close()

altbash_simples()