rendimento_mensal = 0
rendimento_anual = 0
imposto_retido_anual = 0
dedutiveis_totais = 0
imposto_anual = 0
imposto_retido_mensal = 0
dedutiveis_mensais = 0
cntg = 0

while cntg < 12:
    rendimento_mensal = float(input("informe o salário bruto de cada um dos 12 meses (Janeiro a Dezembro): "))
    imposto_retido_mensal = float(input("informe quanto de imposto já foi descontado em folha em cada um dos 12 meses: "))
    dedutiveis_mensais = float(input("informe os gastos isentos: "))

    print("...............................................................................................................")

    rendimento_anual += rendimento_mensal
    imposto_retido_anual += imposto_retido_mensal
    dedutiveis_totais += dedutiveis_mensais
    cntg += 1

else:
    if rendimento_anual <=  29.145:
        pass
    elif rendimento_anual >  29.145 and rendimento_anual <=  33.919:
        imposto_anual = 0.075 * rendimento_anual - 4.774
    elif rendimento_anual >  33.919 and rendimento_anual <= 45.012:
        imposto_anual +=  0.15 * rendimento_anual - 11.093
    elif rendimento_anual > 45.012 and rendimento_anual <= 55.976:
        imposto_anual += 0.225 * rendimento_anual - 10.964
    else:
        imposto_anual += rendimento_anual * 0.275

    diferenca = imposto_anual - dedutiveis_totais
    if diferenca < 0:
        print(f"Você tem R${diferenca:.2f} a receber!")
    elif diferenca > 0:
        print(f"Você tem R${diferenca:.2f} a pagar!")
    else:
        print(f"Saldo inexistente")

    print(f"Seu rendimento total anual é de R${rendimento_anual}, Você pagou R${dedutiveis_totais} de R${imposto_anual}")