from conta_bancaria.conta import ContaBancaria


def menu():
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    conta = ContaBancaria(saldo_inicial)

    while True:
        print("\nMenu:")
        print("1. Consultar saldo")
        print("2. Consultar cheque especial")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Pagar boleto")
        print("6. Verificar uso do cheque especial")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
        elif opcao == '2':
            dados = conta.consultar_cheque_especial()
            print(f"Limite: R$ {dados['limite']:.2f}, Uso atual: R$ {dados['uso']:.2f}")
        elif opcao == '3':
            valor = float(input("Valor do deposito: "))
            conta.depositar(valor)
            print(f"Depósito de R$ {valor:.2f} realizado.")
        elif opcao == '4':
            valor = float(input("Valor do saque: "))
            if conta.sacar(valor):
                print(f"Saque de R$ {valor:.2f} realizado.")
            else:
                print("Saldo insuficiente.")
        elif opcao == '5':
            valor = float(input("Valor do boleto: "))
            if conta.sacar(valor):
                print(f"Boleto de R$ {valor:.2f} pago.")
            else:
                print("Saldo insuficiente para pagar o boleto.")
        elif opcao == '6':
            if conta.uso_cheque > 0:
                print(f"Uso atual do cheque especial: R$ {conta.uso_cheque:.2f}")
            else:
                print("Nenhum uso do cheque especial.")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()