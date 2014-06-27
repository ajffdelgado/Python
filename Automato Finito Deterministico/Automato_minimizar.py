# -*- coding:utf-8 -*-
# Automato Finito Deterministico (AFD) / Minimização do AFD
# Autor: Antonio Jorge Ferreira Delgado Filho

class AFD:
	def __init__(self,alfabeto,estados,estado_inicial,estado_final):
		self.alfabeto = alfabeto
		self.estados = estados
		self.estado_inicial = estado_inicial
		self.estado_final = estado_final
		self.func = {}

	def funcao_transicao(self,estado1,cadeia,estado2):
		if (estado1 or estado2) not in (self.estados):
			print "O estado não se encontra no automato"
		else:
			if estado1 in self.func:
				trans = self.func[estado1]
				trans[cadeia] = estado2
			else:
				self.func[estado1] = {cadeia:estado2}

	def reconhecer_cadeia(self,cadeia):
		self.cadeia = cadeia
		estado_corrente = self.estado_inicial
		for i in self.cadeia:
			if i not in self.alfabeto:
				print "Elemento %s da cadeia, não pertence ao alfabeto" %(i)
				break
			else:
				estado_corrente = self.func[estado_corrente][i]
		if estado_corrente in self.estado_final:
			print "A cadeia é aceita no AFD"
		else:
			print "A cadeia não é aceita no AFD"



	def get_AFD(self):
		print "Alfabeto: ",self.alfabeto
		print "Estados: ",self.estados
		print "Estado inicial: ",self.estado_inicial
		print "Estado final: ",self.estado_final
		print "Função de transição: ",self.func
 
 # --------- Tentativa de minimizar ------------------#
	def novo_estado_min(self):
		return []

	def caminho_final(self, estado): # método para descobrir qual o caminho para chegar ao estado final mais proximo
		trans = self.func[estado]
		estado_atual = estado 
		caminho = ''

		for i in self.alfabeto:
			estado_cor = trans[i]
			while True:
				if estado_cor == estado_atual:
					break
				else:
					if estado_cor in self.final:
						caminho = caminho + i
						break
					else:
						caminho = caminho + i
						estado_cor = trans[i]
		return caminho

	def minimizar(self):
		finais = []
		n_finais =[]
		estado_comp = self.estado_inicial
		novos_estados=[]

		for i in self.func:
			if i in self.estado_final:
				finais.append(i)
			else:
				n_finais.append(i)

		for comp in n_finais:
			for comp_b in n_finais:
				if self.caminho_final(comp) == self.caminho_final(comp_b):
					novo_estado_min = novo_estado_min()
					novo_estado_min.append(comp)
					novo_estado_min.append(comp_b) 
					novos_estados.append(novo_estado_min)
				else:
					continue

