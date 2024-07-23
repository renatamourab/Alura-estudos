from modelo.restaurante import Restaurante

restaurante_vegetariano = Restaurante ('Veg', 'vegetariana')
restaurante_vegetariano.alternar_estado()
restaurante_vegetariano.receber_avaliacao('Nata', 10)
restaurante_vegetariano.receber_avaliacao('Joao', 8.5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
