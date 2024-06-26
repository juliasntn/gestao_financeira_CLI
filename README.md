# Gestão Financeira CLI

Um simples programa de gestão financeira desenvolvido em Python com uma interface de linha de comando (CLI). Este programa permite gerenciar depósitos, despesas variáveis e despesas fixas, além de calcular o saldo atual e fornecer um resumo financeiro.

## Funcionalidades

- Adicionar depósitos
- Adicionar despesas variáveis
- Adicionar despesas fixas
- Remover despesas variáveis
- Remover despesas fixas
- Calcular saldo atual
- Mostrar resumo financeiro detalhado

## Pré-requisitos

- Python 3.6 ou superior

## Como usar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/gestao-financeira-cli.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd gestao-financeira-cli
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

4. Siga as instruções na tela para gerenciar suas finanças.

## Exemplo de Uso

Ao iniciar o programa, você verá um menu com opções:

```
Gestão Financeira CLI
1. Adicionar Depósito
2. Adicionar Despesa
3. Adicionar Despesa Fixa
4. Remover Despesa
5. Remover Despesa Fixa
6. Mostrar Resumo
7. Sair
Escolha uma opção:
```

### Adicionar um Depósito

Selecione a opção `1` e insira o valor do depósito quando solicitado.

### Adicionar uma Despesa

Selecione a opção `2`, insira a descrição e o valor da despesa quando solicitado.

### Adicionar uma Despesa Fixa

Selecione a opção `3`, insira a descrição e o valor da despesa fixa quando solicitado.

### Remover uma Despesa

Selecione a opção `4` e insira a descrição da despesa a ser removida.

### Remover uma Despesa Fixa

Selecione a opção `5` e insira a descrição da despesa fixa a ser removida.

### Mostrar Resumo

Selecione a opção `6` para ver um resumo detalhado de suas finanças.

### Sair

Selecione a opção `7` para sair do programa.

## Código

Aqui está um trecho do código principal do programa:

```python
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
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Contato

Email: falecomjuliasantana@gmail.com
