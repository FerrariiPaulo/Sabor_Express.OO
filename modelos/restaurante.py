from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        """
         Inicializa uma instância de Restaurante

         Parâmetros:
             nome (str):nome do restaurante
             categoria (str): categoria do restaurante
         """
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._status = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante"""
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        """Função para listar os restaurantes cadastrados"""
        print(f"{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {
              "Avaliação".ljust(20)} | {"Status"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {
                  str(restaurante.media_avaliacoes).ljust(20)} | {restaurante._status}")

    @property
    def status(self):
        """Retorna o status como 'Ativo' ou 'Inativo' """
        return "Ativo" if self._status else "Inativo"

    def alterar_status(self):
        """Função para alterar status do restaurante"""
        self._status = not self._status

    def receber_avaliacao(self, cliente, nota):
        """Função para receber notas dos clientes"""
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula média de avaliações"""
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato) 
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida) 