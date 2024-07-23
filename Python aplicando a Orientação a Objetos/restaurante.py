################## AULA 1

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

print(dir(restaurante_praca)) #imprime td da classe, é bom para classe desconhecidas
print(vars(restaurante_praca)) #imprime os atributos nome e categoria


#Exercícios da aula
class Música:
    nome = ''
    artista = ''
    duracao = int

#1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
restaurante_praca.categoria =  'Italiana'

#2 Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_res= restaurante_praca.nome
print(nome_res)

#9 - Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')