'''
Classe para criação de Digimon, seja como aliado ou
como inimigo.
É possível manipular a vida com os métodos.
'''
import numpy as np

class Digimon:
	def __init__(self,nome, hp, mp, atk, res, speed):
		self.nome = nome
		self.defendendo = False
		self.status = np.array([hp,mp,atk,res,speed])
	
	def sofreDano(self, dano):
		self.status[0] = self.status[0] - dano
		print(self.nome , " levou " , dano , " de dano! ")
		print(self.nome , " esta com " , self.status[0] , " de hp. ")
	
	def recuperaVida(self, regen):
		self.status[0] = self.status[0] + regen
		print(self.nome , " recuperou " , regen , " de vida ")
		print(self.nome , " esta com " , self.status[0] , " de hp. ")
	
	def defender(self):
		self.status[3] *= 2
		regen = math.floor(self.status[1] * 0.18)
		self.status[1] += regen
		self.defendendo = True
		print(self.nome , " esta defendendo!")
		print(self.nome , " recuperou " , regen , " de mp. ")
		
	def pararDefesa(self):
		self.status[3] /= 2
		self.defendendo = False
		print(self.nome , " parou de defender.")
		
	def getStatus(self):
		return self.status
