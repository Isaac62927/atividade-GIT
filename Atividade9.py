print("Bem vindo ao MercadO")


class Pessoa:
    def __init__(self, usuario, nome, sobrenome, idade, gmail, senha, cpf):
        self.usuario = usuario
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.gmail = gmail
        self.senha = senha
        self.cpf = cpf


lista_usuarios = []
log_sistema = []
historico_pagamentos = []

cupons = {
    "DESCONTO10": 10,
    "DESCONTO20": 20,
    "MERCADO5": 5
}

estoque = {
    1: {"nome": "Arroz", "valor": 6.99, "quantidade": 10},
    2: {"nome": "Feijao", "valor": 5.99, "quantidade": 10},
    3: {"nome": "Carne", "valor": 19.90, "quantidade": 10},
    4: {"nome": "Frango", "valor": 11.90, "quantidade": 10},
    5: {"nome": "Macarrao", "valor": 7.90, "quantidade": 10},
    6: {"nome": "Detergente", "valor": 4.99, "quantidade": 10},
    7: {"nome": "Sabao em Po", "valor": 14.90, "quantidade": 10},
    8: {"nome": "Desinfetante", "valor": 9.90, "quantidade": 10},
    9: {"nome": "Alcool", "valor": 13.99, "quantidade": 10}
}


def menu_principal():
    print("\n   MENU PRINCIPAL   ")
    print("1 - Cadastrar usuario")
    print("2 - Login")
    print("3 - Sair")


def menu_mercado():
    print("\n   MERCADO   ")
    print("1 - Comprar Produto")
    print("2 - Cadastrar Produto")
    print("3 - Lista Produto")
    print("4 - Repor estoque")
    print("5 - Relatorio(LOG)")
    print("6 - Voltar")
    print("7 - Sair")
    print("8 - Cupons")
    print("9 - Pagamentos")


while True:

    menu_principal()

    opcao = int(input("Qual opcao deseja escolher?: "))

    if opcao == 1:

        continuar = "s"

        while continuar == "s":

            usuario = input("Digite seu usuario: ")
            nome = input("Digite seu nome: ")
            sobrenome = input("Digite seu sobrenome: ")
            idade = int(input("Digite sua idade: "))
            gmail = input("Digite seu gmail: ")
            senha = input("Digite sua senha: ")
            cpf = input("Digite seu cpf: ")

            p = Pessoa(
                usuario,
                nome,
                sobrenome,
                idade,
                gmail,
                senha,
                cpf
            )

            lista_usuarios.append(p)

            log_sistema.append(
                f"Usuario {usuario} cadastrado com sucesso"
            )

            print("Cadastro realizado com sucesso!")

            continuar = input(
                "Deseja cadastrar outro usuario? (s/n): "
            ).lower()

    elif opcao == 2:

        tentativas = 0
        login_sucesso = False

        while tentativas < 3:

            usuario_login = input("Digite seu usuario: ")
            senha_login = input("Digite sua senha: ")

            for pessoa in lista_usuarios:

                if (
                    pessoa.usuario == usuario_login
                    and pessoa.senha == senha_login
                ):

                    login_sucesso = True
                    break

            if login_sucesso:

                print("Login realizado com sucesso!")

                log_sistema.append(
                    f"Usuario {usuario_login} fez login no sistema"
                )

                break

            else:

                tentativas += 1

                print(
                    f"Usuario ou senha incorretos! "
                    f"Tentativas restantes: {3 - tentativas}"
                )

        if not login_sucesso:
            print("Sistema bloqueado por excesso de tentativas!")
            continue

        while True:

            menu_mercado()

            escolhas = int(
                input("Escolha a opcao desejada: ")
            )

            if escolhas == 1:

                print("\n   COMPRAR PRODUTO   ")

                for codigo, produto in estoque.items():

                    print(
                        f"{codigo} - "
                        f"{produto['nome']} "
                        f"R$ {produto['valor']:.2f} "
                        f"| Estoque: "
                        f"{produto['quantidade']}"
                    )

                print("0 - Voltar")

                codigo_produto = int(
                    input("Digite o codigo do produto: ")
                )

                if codigo_produto == 0:
                    continue

                if codigo_produto not in estoque:
                    print("Codigo invalido!")
                    continue

                quantidade = int(
                    input("Digite a quantidade desejada: ")
                )

                if quantidade <= 0:
                    print("Quantidade invalida!")
                    continue

                produto = estoque[codigo_produto]

                if quantidade > produto["quantidade"]:
                    print("Estoque insuficiente!")
                    continue

                produto["quantidade"] -= quantidade

                total = produto["valor"] * quantidade

                print(f"\nProduto: {produto['nome']}")
                print(f"Quantidade: {quantidade}")
                print(
                    f"Valor sem desconto: "
                    f"R$ {total:.2f}"
                )

                usar_cupom = input(
                    "Deseja usar cupom? (s/n): "
                ).lower()

                desconto = 0

                if usar_cupom == "s":

                    codigo_cupom = input(
                        "Digite o cupom: "
                    ).upper()

                    if codigo_cupom in cupons:

                        desconto = cupons[codigo_cupom]

                        valor_desconto = (
                            total * (desconto / 100)
                        )

                        total -= valor_desconto

                        print(
                            f"Cupom aplicado: "
                            f"{desconto}% OFF"
                        )

                    else:
                        print("Cupom invalido!")

                print(f"Valor final: R$ {total:.2f}")

                print("\n==== PAGAMENTO ====")
                print("1 - Pix")
                print("2 - Cartao")
                print("3 - Dinheiro")

                pagamento = int(
                    input(
                        "Escolha a forma de pagamento: "
                    )
                )

                if pagamento == 1:
                    forma_pagamento = "Pix"

                elif pagamento == 2:
                    forma_pagamento = "Cartao"

                elif pagamento == 3:
                    forma_pagamento = "Dinheiro"

                else:
                    print("Forma de pagamento invalida!")
                    continue

                print(
                    f"Pagamento realizado via "
                    f"{forma_pagamento}"
                )

                historico_pagamentos.append(
                    f"Produto: {produto['nome']} | "
                    f"Quantidade: {quantidade} | "
                    f"Forma de pagamento: "
                    f"{forma_pagamento} | "
                    f"Valor pago: R$ {total:.2f}"
                )

                print("Compra realizada com sucesso!")

                log_sistema.append(
                    f"Venda realizada: "
                    f"{produto['nome']} | "
                    f"Quantidade: {quantidade} | "
                    f"Pagamento: {forma_pagamento} | "
                    f"Total: R$ {total:.2f}"
                )

            elif escolhas == 2:

                print("\n   CADASTRAR PRODUTOS   ")

                print("101 - Arroz 6.99$")
                print("102 - Feijao 5.99$")
                print("103 - Carne 19.90$")
                print("104 - Frango 11.90$")
                print("105 - Macarrao 7.90$")
                print("106 - Detergente 4,99$")
                print("107 - Sabao em Po 14,90$")
                print("108 - Desinfetante 9,90$")
                print("109 - Alcool 13,99$")
                print("110 - Voltar")

                item = int(
                    input(
                        "Escolha o item que deseja cadastrar: "
                    )
                )

                if item == 101:
                    nome_produto = "Arroz"
                    valor = 6.99

                elif item == 102:
                    nome_produto = "Feijao"
                    valor = 5.99

                elif item == 103:
                    nome_produto = "Carne"
                    valor = 19.90

                elif item == 104:
                    nome_produto = "Frango"
                    valor = 11.90

                elif item == 105:
                    nome_produto = "Macarrao"
                    valor = 7.90

                elif item == 106:
                    nome_produto = "Detergente"
                    valor = 4.99

                elif item == 107:
                    nome_produto = "Sabao em Po"
                    valor = 14.90

                elif item == 108:
                    nome_produto = "Desinfetante"
                    valor = 9.90

                elif item == 109:
                    nome_produto = "Alcool"
                    valor = 13.99

                elif item == 110:
                    continue

                else:
                    print("Codigo invalido!")
                    continue

                print(
                    f"Produto cadastrado: "
                    f"{nome_produto}"
                )

                print(f"Valor: R$ {valor:.2f}")

                log_sistema.append(
                    f"Produto cadastrado: "
                    f"{nome_produto} - "
                    f"R$ {valor:.2f}"
                )

            elif escolhas == 3:

                print("\n==== LISTA DE PRODUTOS ====")

                for codigo, produto in estoque.items():

                    print(
                        f"{codigo} - "
                        f"{produto['nome']} "
                        f"| R$ {produto['valor']:.2f} "
                        f"| Estoque: "
                        f"{produto['quantidade']}"
                    )

            elif escolhas == 4:

                print("\n   REPOSICAO DE ESTOQUE   ")

                for codigo, produto in estoque.items():

                    print(
                        f"{codigo} - "
                        f"{produto['nome']} "
                        f"| Estoque atual: "
                        f"{produto['quantidade']}"
                    )

                reposicao = int(
                    input(
                        "Qual produto deseja repor?: "
                    )
                )

                if reposicao not in estoque:
                    print("Produto invalido!")
                    continue

                quantidade = int(
                    input(
                        "Digite a quantidade "
                        "que deseja adicionar "
                        "ao estoque: "
                    )
                )

                if quantidade <= 0:
                    print("Quantidade invalida!")
                    continue

                estoque[reposicao]["quantidade"] += quantidade

                produto = estoque[reposicao]["nome"]

                print(
                    f"Estoque do produto "
                    f"{produto} atualizado!"
                )

                print(
                    f"Quantidade adicionada: "
                    f"{quantidade}"
                )

                log_sistema.append(
                    f"Reposicao feita no produto "
                    f"{produto} com quantidade "
                    f"{quantidade}"
                )

            elif escolhas == 5:

                print("\n   RELATORIO LOG   ")

                if len(log_sistema) == 0:
                    print(
                        "Nenhuma movimentacao registrada."
                    )

                else:

                    for log in log_sistema:
                        print(log)

            elif escolhas == 6:
                break

            elif escolhas == 7:
                print("Volte sempre!!")
                exit()

            elif escolhas == 8:

                print("\n   CUPONS DISPONIVEIS   ")
                print("DESCONTO10 = 10% OFF")
                print("DESCONTO20 = 20% OFF")
                print("MERCADO5 = 5% OFF")

            elif escolhas == 9:

                print(
                    "\n   HISTORICO DE PAGAMENTOS   "
                )

                if len(historico_pagamentos) == 0:
                    print(
                        "Nenhum pagamento realizado."
                    )

                else:

                    for pagamento in historico_pagamentos:
                        print(pagamento)

            else:
                print("Opcao invalida!")

    elif opcao == 3:

        print("Volte sempre!!")
        break

    else:
        print("Opcao invalida!")
