class ItemCardapio:
    def __init__(self, nome, preco):
        """Construtor"""
        self._nome = nome
        self._preco = preco
        
    def __str__(self):
        return self._nome