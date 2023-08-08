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
LIMITE_SAQUES = 3

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
                                valor = float(input("Informe valor de saque: "))

                                if valor>saldo:
                                                print("Operação falhou! Você não tem saldo suficiente para esta operação. ")
                                elif valor>limite:
                                                print("Operação falhou! Você não pode ultrapassar o limite para seu saque.")     
                                elif numero_saques>=LIMITE_SAQUES:
                                                print("Operação falhou! Você excedeu o numero de saques diários. Tente amanhã.") 
                                elif valor>0:
                                                saldo-=valor
                                                extrato+=f"Saque: R$ {valor:.2f}\n"    
                                                numero_saques+=1
                                else:
                                                print("Operacação falhou! Valor informado é invalido.")           
                
                elif opcao == "e":
                                print(" EXTRATO ".center(41,"="))
                                print("Não foram realizadas movimentações." if not extrato else extrato)
                                print(f"\nSaldo: R$ {saldo:.2f}")
                                print("".center(41,"="))

                
                elif opcao == "q":
                                print("Saindo do sistema.")
                                break
                
                else:
                                print("Operação inválida, por favor digite novamente a operação desejada.")
