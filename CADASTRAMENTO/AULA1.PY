class Produto:
    """
    Classe que representa um produto de uma loja.
    """
 
    def __init__(self, nome, valor, quantidade):
        """
        Construtor da classe Produto.
 
        Args:
            nome (str): O nome do produto.
            valor (float): O valor do produto.
            quantidade (int): A quantidade do produto em estoque.
        """
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
 
    def exibir_dados(self):
        """
        Exibe as informações do produto.
        """
        print(f"Nome: {self.nome}")
        print(f"Valor: {self.valor:.2f}")  # Formatação para duas casas decimais
        print(f"Quantidade: {self.quantidade}")
 
# Criação de um objeto da classe Produto
produto1 = Produto("chinelo", 99.90, 6)
 
# Exibição dos dados do produto
print("Informações do produto:")
produto1.exibir_dados()
print("-" * 20)
 
# Criação de outro objeto
produto2 = Produto("meia adidas", 99.99, 2)
print("Informações do produto:")
produto2.exibir_dados()