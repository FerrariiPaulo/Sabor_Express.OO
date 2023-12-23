from modelos.restaurante import Restaurante

restaurante_japones = Restaurante("Kyoko", "japonesa")
restaurante_japones.receber_avaliacao("Gui", 4.5)
restaurante_japones.receber_avaliacao("Mari", 3.5)




def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()