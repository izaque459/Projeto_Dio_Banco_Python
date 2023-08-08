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
                                valor = float(input("Informe o valor de desposito: "))

                                if valor>0:
                                                saldo+=valor
                                                extrato+=f"Deposito: R${valor:.2f}\n"
                                else:
                                            print("Operação falhou! Usuario informe valor válido")

                elif opcao == "s":
                                print("Saque")
                elif opcao == "e":
                                print("Extrato")
                elif opcao == "q":
                                print("Saindo do sistema.")
                                break
                else:
                                print("Operação inválida, por favor digite novamente a operação desejada.")
