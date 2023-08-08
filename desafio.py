menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
                opcao = input(menu)
                if opcao == "d":
                                print("Deposito")
                elif opcao == "s":
                                print("Saque")
                elif opcao == "e":
                                print("Extrato")
                elif opcao == "q":
                                print("Saindo do sistema.")
                                break
                else:
                                print("Operação inválida, por favor digite novamente a operação desejada.")
