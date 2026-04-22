#calculadora dee operações basicas
def main():

    try:
        op = input("Informe a peração que deseja fazer (+, -, *, /): ")
        n1 = float(input("Informe o primeiro número da operação: "))
        n2 = float(input("Informe o segundo número da operação: "))

        if op == "+" or op == "-" or op == "*" or op == "/":
            pass
        else:
            print("Operação invalida! Tente novamente.")
            print("...................................")
            return main()

    except ValueError:
        print("Valores invalidos! Tente novamente.")
        print("...................................")
        return main()
    
    else:
        if op == "+":
            print(f"A soma de {n1} + {n2} é: {(n1 + n2)}")
        elif op == "-":
            print(f"A subtração de {n1} - {n2} é: {(n1 - n2)}")
        elif op == "*":
            print(f"A multiplicação de {n1} * {n2} é: {(n1 * n2)}")
        else:
            print(f"A divisão {n1} / {n2} é: {(n1 / n2)}")

main()