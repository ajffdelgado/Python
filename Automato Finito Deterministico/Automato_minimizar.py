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

