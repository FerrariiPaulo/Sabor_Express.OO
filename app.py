""" from modelos.restaurante import Restaurante """
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# restaurante_japones = Restaurante("Kyoko", "japonesa")
bebida_suco = Bebida("Suco de Abacaxi com Hortelã", 7.00, "grande")
prato_russo = Prato("Estrogonofe", 20.00, "Estrogonofe de carne com cogumuelos")



def main():
    print(bebida_suco)
    print(prato_russo)

if __name__ == "__main__":
    main()