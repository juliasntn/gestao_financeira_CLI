import sys

class FinancialManagement:
    def __init__(self):
        self.deposits = []
        self.expenses = []
        self.fixed_expenses = []

    def add_deposit(self, amount):
        self.deposits.append(amount)
        print(f'Depósito de R${amount} adicionado com sucesso!')

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))
        print(f'Despesa "{description}" de R${amount} adicionada com sucesso!')

    def add_fixed_expense(self, description, amount):
        self.fixed_expenses.append((description, amount))
        print(f'Despesa fixa "{description}" de R${amount} adicionada com sucesso!')

    def remove_expense(self, description):
        self.expenses = [expense for expense in self.expenses if expense[0] != description]
        print(f'Despesa "{description}" removida com sucesso!')

    def remove_fixed_expense(self, description):
        self.fixed_expenses = [expense for expense in self.fixed_expenses if expense[0] != description]
        print(f'Despesa fixa "{description}" removida com sucesso!')

    def calculate_balance(self):
        total_deposits = sum(self.deposits)
        total_expenses = sum(amount for _, amount in self.expenses)
        total_fixed_expenses = sum(amount for _, amount in self.fixed_expenses)
        return total_deposits - total_expenses - total_fixed_expenses

    def show_summary(self):
        print("\nResumo Financeiro:")
        print("Depósitos:")
        for deposit in self.deposits:
            print(f" - R${deposit}")
        print("Despesas:")
        for desc, amount in self.expenses:
            print(f" - {desc}: R${amount}")
        print("Despesas Fixas:")
        for desc, amount in self.fixed_expenses:
            print(f" - {desc}: R${amount}")
        print(f"\nSaldo atual: R${self.calculate_balance()}\n")

def main():
    fm = FinancialManagement()

    while True:
        print("\nGestão Financeira CLI")
        print("1. Adicionar Depósito")
        print("2. Adicionar Despesa")
        print("3. Adicionar Despesa Fixa")
        print("4. Remover Despesa")
        print("5. Remover Despesa Fixa")
        print("6. Mostrar Resumo")
        print("7. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            amount = float(input("Informe o valor do depósito: "))
            fm.add_deposit(amount)
        elif choice == '2':
            description = input("Informe a descrição da despesa: ")
            amount = float(input("Informe o valor da despesa: "))
            fm.add_expense(description, amount)
        elif choice == '3':
            description = input("Informe a descrição da despesa fixa: ")
            amount = float(input("Informe o valor da despesa fixa: "))
            fm.add_fixed_expense(description, amount)
        elif choice == '4':
            description = input("Informe a descrição da despesa a ser removida: ")
            fm.remove_expense(description)
        elif choice == '5':
            description = input("Informe a descrição da despesa fixa a ser removida: ")
            fm.remove_fixed_expense(description)
        elif choice == '6':
            fm.show_summary()
        elif choice == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
