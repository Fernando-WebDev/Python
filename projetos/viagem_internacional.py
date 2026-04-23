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
        dias_disponivel = 0
        custo_fixo = 0
        
        if destino = 1:
            idade_min = 18
        elif destino = 2 or destino 3:
            idade_min = 16
        
    except ValueError:
        print("informações invalidas!")
        print("......................")
        return viagem()
        
    else:
        if passaporte == "sim":
            if destino == 1 and idade >= idade_min:
                custo_fixo = 10000
                pass
            elif destino == 2 and idade >= idade_min:
                custo_fixo = 12000
                pass
            elif destino == 3 and idade >= idade_min:
                custo_fixo = 15000
                pass
            else:
                print("idade minima para o destino não atingida)")
                break
                
            if fluencia >= 8:
                dias_disponivel = 90
            elif fluencia >= 5:
                dias_disponivel = 30
            else:
                dias_disponiveis = 15
                
            if dias > dias_disponivel:
                print(f"Viagem Negada: Sua fluência de {fluencia} permite apenas {dias_disponivel} dias, mas você solicitou {dias} dias. ")
                break
            else:
                pass
            
            if (orcamento - custo_fixo)
                    
        else:
             print("viagem negada: (passaporte invalido")

viagem()

'''https://rj.olx.com.br/rio-de-janeiro-e-regiao/games/consoles-de-video-game/venda-ps5-monitor-gamer-ultragear--1496400977?lis=listing_16000'''