def viagem():

    try:
        # dados solicitados
        dias = int(input("informe quantos dias você pretende viajar: "))
        destino = int(input("OPÇÕES: \n1 - Nova York\n2 - Paris\n3 - Tóquio\ninforme o seu destino(1, 2 ou 3): "))
        passaporte = input("você possui passaporte? (sim ou não)").lower()
        orcamento = float(input("informe seu orçamento em R$: "))
        idade = int(input("informe sua idade: "))
        fluencia = int(input("informe seu nivel de fluencia no idioma local (0 a 10): "))
        idade_min = 0 
        
        if destino = 1:
            idade_min = 18
        elif destino = 2 or destino = 3:
            idade_min = 16
        
    except ValueError:
        print("informações invalidas!")
        print("......................")
        return viagem()
        
    else:
        if passaporte == "sim":
            if destino == 1 and idade >= idade_min:
                pass
            elif destino == 2 and idade >= idade_min:
                pass
            elif destino == 3 and idade >= idade_min:
                pass
            else:
                print("idade minima para o destino não atingida)")
        else:
             print("viagem negada: (passaporte invalido")
        



viagem()