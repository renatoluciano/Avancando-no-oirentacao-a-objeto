class Filme:

	def __init__(self, nome, ano, duracao):
		self.nome = nome
		self.ano = ano
		self.duracao = duracao

class Serie:

	def __init__(self, nome, ano, temporadas):
		self.nome = nome
		self.ano = ano
		self.temporadas = temporadas



vingadores = Filme("Vingadores - Guerra Infinita", 2016, 120)
print(vingadores.nome)

atlanta = Serie("Atlanta", 2017, 2)
print(atlanta.nome)