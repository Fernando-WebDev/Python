def altbash_variacao():
    
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

altbash_variacao()