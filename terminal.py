from sisbanco import Banco

def terminal():
   sisbanco = Banco()
   while(True):
      print("SisBanco::Bem-Vindo!")
      print(".::Opcoes::.")
      print("[0] Cadastrar Conta")
      print("[1] Creditar")
      print("[2] Debitar")
      print("[3] Transferir")
      print("[4] Consultar Saldo")
      print("[5] Render Juros")
      print("[6] Render Bonus")
      print("[7] Alterar Taxa_Juros")      
      print("[8] Alterar Taxa_Imposto")
      print("[9] Sair")
      opcao = int(input("Digite:"))
      
      if opcao == 0:
         pass
         #qual tipo de conta a ser criada:
         #S - Simples  | P - Poupanca | E - Especial | I - Imposto
         #solicite o numero da conta a ser criada
         #instancie uma conta do tipo selecionado com esse numero
         #cadastre a conta no sisbanco

      elif opcao == 1:
         pass
         #solicite o numero da conta alvo
         #solicite o valor a ser creditado
         #realize a operacao de credito no sisbanco

      elif opcao == 2:
         pass
         #solicite o numero da conta alvo
         #solicite o valor a ser debitado
         #realize a operacao de debito no sisbanco

      elif opcao == 3:
         pass
         #solicite o numero da conta origem
         #solicite o numero da conta destino
         #solicite o valor a ser transferido
         #realize a operacao de transferencia no sisbanco

      elif opcao == 4:
         pass
         #solicite o numero da conta alvo
         #realize a operacao de obtencao de saldo no sisbanco
         #exiba o saldo na tela
      
      elif opcao == 5:
         pass
         #solicite o numero da conta alvo
         #realize a operacao correcao da poupanca no sisbanco
      
      elif opcao == 6:
         pass
         #solicite o numero da conta alvo
         #realize a operacao conversao/rendimento de bonus no sisbanco
      
      elif opcao == 7:
         pass
         #solicite a nova taxa de correcao da poupanca
         #realize a operacao de alteracao da taxa no sisbanco

      elif opcao == 8:
         pass
         #solicite a nova taxa de imposto
         #realize a operacao de alteracao da taxa no sisbanco
         
      elif opcao == 9:
         print("SisBanco::Bye!")
         break

if __name__ == "__main__":
   terminal()