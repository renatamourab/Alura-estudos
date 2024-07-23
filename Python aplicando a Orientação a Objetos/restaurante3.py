#aulas anteriores

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self.categoria = categoria
        self._ativo = False                                             #o ativo agora está protegido/privado
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):       # cls - indica q esta se referindo a classe
        print (f'{'Nome do Restaurante'.ljust(25) } | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

#aula nova - Property e metodos de classe
    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    #Property- serve pra mudar atributos privados de forma "mais bonita"

    def alternar_estado(self):                 #como esta privado precisa fazer isso para alternar
        self._ativo = not self._ativo
    
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()