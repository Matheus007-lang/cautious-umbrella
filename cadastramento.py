class Cliente:
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def exibir_dados(self):
        print(("---CADASTRO DE CLIENTES---"))
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")

if __name__ == "__main__":
    cliente1 = Cliente("João", "4723468760", "João@hotmail.com", "Rua boa vista 653, Centro - Canoas")
    cliente2 = Cliente("Claudia", "4798757621", "Claudia@hotmail.com", "João segundo 890, Centro - Caxias")
    cliente3 = Cliente("Eduardo", "4799057673", "Eduardo@gmail.com", "Avenida Fabio Gomes 650, Bairro Alto das palmeiras")

    cliente1.exibir_dados()
    print("------")
    cliente2.exibir_dados()
    print("------")
    cliente3.exibir_dados()
    print("------")

 