################## AULA 2

# init - cria o metodo construtor

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça' , 'Gourmet')
restaurante_pizza = Restaurante('Pizza express' , 'Italiana')
print('teste')
print(restaurante_praca)
print("fim teste")
print(vars(restaurante_praca))
print(vars(restaurante_pizza))

############# AULA 3 MÉTODOS ESPECIAIS

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):   #usa return por ser parte escrita
        return f' {self.nome} | {self.categoria}'


restaurante_praca = Restaurante('Praça' , 'Gourmet')
restaurante_pizza = Restaurante('Pizza express' , 'Italiana')

print((restaurante_praca))
print((restaurante_pizza))

########### AULA 4 CRIANDO MEUS MÉTODOS

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()
