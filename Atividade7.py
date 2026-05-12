print("Bem vindo ao CineMark")
print("Escolha a opcao desejada!")
print("1 - Cadastrar usuario")
print("2 - Entrar em um usuario")
print("3 - Sair")

opcao = int(input("Qual opcao deseja escolher?: "))


class Pessoa:
    def __init__(self, nome, sobrenome, idade, gmail, senha, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.gmail = gmail
        self.senha = senha
        self.cpf = cpf


lista = []

if opcao == 1:

    continuar = "s"

    while continuar == "s":

        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        idade = int(input("Digite sua idade: "))
        gmail = input("Digite seu gmail: ")
        senha = input("Digite sua senha: ")
        cpf = input("Digite seu cpf: ")

        p = Pessoa(nome, sobrenome, idade, gmail, senha, cpf)

        lista.append(p)

        continuar = input("Deseja cadastrar outra conta? (s/n): ").lower()

    print("\nDados das pessoas cadastradas:")

    for pessoa in lista:
        print("Nome:", pessoa.nome)
        print("Sobrenome:", pessoa.sobrenome)
        print("Idade:", pessoa.idade)
        print("Gmail:", pessoa.gmail)
        print("Senha:", pessoa.senha)
        print("CPF:", pessoa.cpf)


elif opcao == 2:

    print("Logando...")

    print("\nCinema")
    print("1 - Comprar ingresso")
    print("2 - Sair")

    escolhas = int(input("Escolha a opcao desejada: "))

    if escolhas == 1:

        print("\nDigite o filme que deseja assistir")
        print("1 - Os Vingadores 19,90$")
        print("2 - Vingadores: Era de Ultron 22,99$")
        print("3 - Vingadores: Guerra Infinita 25,90$")
        print("4 - Vingadores: Ultimato 29,90$")

        filme = int(input("Escolha o filme: "))
        ingresso = int(input("Quantos ingressos deseja comprar?: "))

        if filme == 1:
            valor_ingresso = 19.90
            nome_filme = "Os Vingadores"

        elif filme == 2:
            valor_ingresso = 22.99
            nome_filme = "Vingadores: Era de Ultron"

        elif filme == 3:
            valor_ingresso = 25.90
            nome_filme = "Vingadores: Guerra Infinita"

        elif filme == 4:
            valor_ingresso = 29.90
            nome_filme = "Vingadores: Ultimato"

        else:
            print("Filme invalido!")
            valor_ingresso = 0

        total = ingresso * valor_ingresso

        print("\nFilme escolhido:", nome_filme)
        print("Total da compra: R$", total)

        print("\nEscolha a forma de pagamento")
        print("1 - PIX")
        print("2 - Debito")
        print("3 - Credito")
        print("4 - Cancelar")

        pagamento = int(input("Escolha a forma de pagamento: "))

        if pagamento == 1:
            print("Pagamento Sendo Realizado...")

        elif pagamento == 2:
            print("Pagamento Sendo Realizado...")

        elif pagamento == 3:
            print("Pagamento Sendo Realizado...")

        elif pagamento == 4:
            print("Compra cancelada!")

        else:
            print("Opcao invalida!")

        print("Compra finalizada com sucesso!")

    elif escolhas == 2:
        print("Saindo do sistema...")

elif opcao == 3:

    print("Volte sempre!!")

else:

    print("Opcao invalida!")
