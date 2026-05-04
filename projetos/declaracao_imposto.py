def declarar_imposto():

    try:
        rendimento_ano = float(input("Informe qual foi seu rendimento bruto em BRL(R$) desse ano: "))
        isento = 0
        imposto_anual = 0

    except ValueError:
        print("Informações invalidas!Tente novamente.")
        print("......................................")
        return declarar_imposto()
    
    else:
        if rendimento_ano <=  29.145:
            pass
        elif rendimento_ano >  29.145 and rendimento_ano <=  33.919:
            imposto_anual = 4.774 * 0.075
        elif rendimento_ano >  33.919 and rendimento_ano <= 45.012:
            imposto_anual += 11.093 * 0.15
        elif rendimento_ano > 45.012 and rendimento_ano <= 55.976:
            imposto_anual += 10.964 * 0.225
        else:
            imposto_anual += rendimento_ano * 0.275

        print(imposto_anual)

declarar_imposto()