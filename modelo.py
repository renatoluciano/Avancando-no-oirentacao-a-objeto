class Programa:

	def __init__(self, nome, ano, duracao):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, novo_nome):
		self._nome = novo_nome.title()

	@property
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1


class Filme(Programa):

	def __init__(self, nome, ano, duracao):
		self._nome = nome.title()
		self.ano = ano
		self.duracao = duracao
		self._likes = 0



class Serie(Programa):
	def __init__(self, nome, ano, temporadas):
		self._nome = nome.title()
		self.ano = ano
		self.temporadas = temporadas
		self._likes = 0



vingadores = Filme("vingadores - guerra infinita", 2016, 120)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}' )

atlanta = Serie("atlanta", 2017, 2)
atlanta.dar_like()
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')