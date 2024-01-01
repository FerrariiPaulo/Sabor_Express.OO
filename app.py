from modelos.restaurante import Restaurante 
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_japones = Restaurante("Kyoko", "japonesa")
bebida_suco = Bebida("Suco de Abacaxi com Hortelã", 7.00, "grande")
bebida_suco.aplicar_desconto()
prato_russo = Prato("Estrogonofe", 20.00, "Estrogonofe de carne com cogumuelos")
prato_russo.aplicar_desconto()
sobremesa_pudim = Sobremesa("Pudim", 9.0, "Pudim de leite condensado sem furinhos")
restaurante_japones.adicionar_no_cardapio(bebida_suco)
restaurante_japones.adicionar_no_cardapio(prato_russo)
restaurante_japones.adicionar_no_cardapio(sobremesa_pudim)



def main():
    restaurante_japones.exibir_cardapio

if __name__ == "__main__":
    main()