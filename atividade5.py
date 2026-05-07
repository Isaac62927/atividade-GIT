class Pessoa:
    def __init__(self, nome, email, sexo, numero, cpf):
        self.nome = nome
        self.email = email
        self.sexo = sexo
        self.numero = numero
        self.cpf = cpf

    def dados(self):
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Sexo:", self.sexo)
        print("Número:", self.numero)
        print("CPF:", self.cpf)


pessoa1 = Pessoa(
    "Isaac Pereira",
    "isaaclp006@gmail.com",
    "Masculino",
    "(61) 99201-7159",
    "823.128.472-52"
)

pessoa1.dados()
