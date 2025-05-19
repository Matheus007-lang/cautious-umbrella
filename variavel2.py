class Produto:
    # Construtor com os atributos do produto
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo          # Código identificador do produto
        self.nome = nome              # Nome do produto
        self.preco = preco            # Preço unitário
        self.quantidade = quantidade  # Quantidade em estoque
 
    # Método para exibir as informações do produto
    def exibir_informacoes(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")
        print("-" * 30)

    # Método para atualizar o preço do produto
    def atualizar_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço do produto '{self.nome}' atualizado para R${self.preco:.2f}")
 
    # Método para adicionar mais unidades ao estoque
    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
        print(f"{quantidade} unidades adicionadas ao estoque de '{self.nome}'.")
 
    # Método para remover unidades do estoque (ex: em uma venda)
    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades removidas do estoque de '{self.nome}'.")
        else:
            print("Estoque insuficiente!")
 
 
# Exemplo de uso:
if __name__ == "__main__":
    # Criando um objeto da classe Produto
    produto1 = Produto("001", "Mouse Gamer", 120.00, 10)
 
    # Exibindo informações
    produto1.exibir_informacoes()
 
    # Atualizando o preço
    produto1.atualizar_preco(135.00)
 
    # Adicionando estoque
    produto1.adicionar_estoque(5)
 
    # Removendo estoque
    produto1.remover_estoque(3)
 
    # Exibindo informações novamente
    produto1.exibir_informacoes()