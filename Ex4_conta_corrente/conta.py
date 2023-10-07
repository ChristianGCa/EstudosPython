
import csv

# Definindo a classe
class ContaCorrente:

    # Criando o método construtor
    def __init__(self, numero_da_conta: int, nome_do_correntista: str, saldo=0.0):
        self.numero_da_conta = numero_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo

    # Método par consultar o saldo atual
    def extrato(self):
        print(f"{self.nome_do_correntista} R$", self.saldo)


    # Criando um método para alterar o nome
    def alterar_nome(self, novo_nome: str):
        self.nome_do_correntista = novo_nome
        print(f"Conta: {self.nome_do_correntista}. Nome do correntista alterado para {novo_nome}.")

    # Criando um método para efetuar depósito
    def depositar(self, deposito: float):
        if deposito >= 0:
            self.saldo += deposito
            print(f"Conta: {self.nome_do_correntista}. Depósito de R$ {deposito} efetuado com sucesso!")
        else:
            print(f"Conta: {self.nome_do_correntista}. Erro: o depósito não pode ser negativo")

    # Criando um método para efetuar saque
    def sacar(self, sacar: float):
        if sacar <= self.saldo:
            self.saldo -= sacar
            print(f"Conta: {self.nome_do_correntista}. Saque de R$ {sacar} efetuado com sucesso")
        else:
            print(f"Conta: {self.nome_do_correntista}. Saldo insuficiente para saque")

    # Criando um método para transferências
    def transferir(self, conta_destino, quantia: float):
        if quantia <= self.saldo:
            self.sacar(quantia)
            conta_destino.depositar(quantia)
            print(f"Conta: {self.nome_do_correntista}. Transferência efetuada com sucesso.")
        else:
            print(f"Conta: {self.nome_do_correntista}. Saldo insuficiente para a transferência")

# Usando a classe
# Criando contas correntes
contaCorrente1 = ContaCorrente(100, "Carl Johnson")
contaCorrente2 = ContaCorrente(101, "Big Smoke", 10000.50)
contaCorrente3 = ContaCorrente(100, "Ryder", 1000)

# Depósitos
contaCorrente1.depositar(100)
contaCorrente2.depositar(500.50)
contaCorrente3.depositar(1)

#contaCorrente1.extrato()
#contaCorrente2.extrato()
#contaCorrente3.extrato()
print()

# Saques
contaCorrente1.sacar(21312312)
contaCorrente2.sacar(500.50)
contaCorrente3.sacar(1)

#contaCorrente1.extrato()
#contaCorrente2.extrato()
##contaCorrente3.extrato()
print()

# Transferências
contaCorrente1.transferir(contaCorrente3, 5)
contaCorrente2.transferir(contaCorrente1, 10000)
contaCorrente3.transferir(contaCorrente1, 1000)

#contaCorrente1.extrato()
#contaCorrente2.extrato()
#contaCorrente3.extrato()

# Gerando o relatório em CSV
with open('relatorio.csv', mode = 'w') as arquivo_csv:
    w = csv.writer(arquivo_csv)
    w.writerow(['Conta', 'Correntista', 'Saldo'])
    for conta in [contaCorrente1, contaCorrente2, contaCorrente3]:
        w.writerow([conta.numero_da_conta, conta.nome_do_correntista, conta.saldo])