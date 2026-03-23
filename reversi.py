"""
Juego de reversi

El estado se va a representar como una lista de 64 elementos, tal que


0  1  2  3  4  5  6  7
8  9 10 11 12 13 14 15
16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31
32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63



y cada elemento puede ser 0, 1 o -1, donde 0 es vacío, 1 es una ficha del
jugador 1 y -1 es una ficha del jugador 2.
El juego inicia con 4 piesas en el centro 27=-1, 28=1, 35=1, 36=-1

Las acciones son poner una ficha en una casilla vacia

Un estado terminal es aquel en el que ninguno de los 2 jugadores tiene movimientos validos disponibles

La ganancia es 1 si gana el jugador 1, -1 si gana el jugador 2 y 0 si es un
empate.

"""

import juegos_simplificado as js
import minimax
class reversi(js.JuegoZT2):
	def inicializa(self):
			return (
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0, -1,  1,  0,  0,  0,
        0,  0,  0,  1, -1,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0,
        0,  0,  0,  0,  0,  0,  0,  0
    )
			
	def jugadas_legales(self, s, j):
		oponente = -j
		movimientos_validos = [] 
  
		for pieza in range(64):
			if s[pieza] == j:
				
				# Arriba (-8)
				i = pieza
				rival = 0
				while True:
					i -= 8
					if i < 0: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Abajo (+8) 
				i = pieza
				rival = 0
				while True:
					i += 8
					if i > 63: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Izquierda (-1) 
				i = pieza
				rival = 0
				while True:
					if i % 8 == 0: break 
					i -= 1
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Derecha (+1)
				i = pieza
				rival = 0
				while True:
					if i % 8 == 7: break 
					i += 1
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Diagonal arriba izquierda (-9)
				i = pieza
				rival = 0
				while True:
					if i % 8 == 0: break 
					i -= 9
					if i < 0: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Diagonal arriba derecha (-7)
				i = pieza
				rival = 0
				while True:
					if i % 8 == 7: break 
					i -= 7
					if i < 0: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Diagonal abajo izquieda (+7) 
				i = pieza
				rival = 0
				while True:
					if i % 8 == 0: break 
					i += 7
					if i > 63: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

				# Diagonal abajo derecha (+9)
				i = pieza
				rival = 0
				while True:
					if i % 8 == 7: break 
					i += 9
					if i > 63: break 
					
					if s[i] == oponente: 
						rival += 1
					elif s[i] == 0:
						if rival > 0 and i not in movimientos_validos: 
							movimientos_validos.append(i)
						break
					elif s[i] == j:
						break

		return movimientos_validos
		
	def sucesor(self, s, a, j):
		s = list(s[:])
		rival = -j
		s[a] = j

		# Arriba (-8)
		i = a
		volteo = []
		while True:
			i -= 8
			if i < 0: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Abajo (+8)
		i = a
		volteo = []
		while True:
			i += 8
			if i > 63: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Izquierda (-1)
		i = a
		volteo = []
		while True:
			if i % 8 == 0: break 
			i -= 1
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Derecha (+1)
		i = a
		volteo = []
		while True:
			if i % 8 == 7: break 
			i += 1
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Diagonal arriba izquierda (-9)
		i = a
		volteo = []
		while True:
			if i % 8 == 0: break 
			i -= 9
			if i < 0: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Diagonal arriba derecha (-7)
		i = a
		volteo = []
		while True:
			if i % 8 == 7: break 
			i -= 7
			if i < 0: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Diagonal abajo izquierda (+7)
		i = a
		volteo = []
		while True:
			if i % 8 == 0: break 
			i += 7
			if i > 63: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		# Diagonal abajo derecha (+9)
		i = a
		volteo = []
		while True:
			if i % 8 == 7: break 
			i += 9
			if i > 63: break 
			
			if s[i] == rival:
				volteo.append(i)
			elif s[i] == j:
				for p in volteo:
					s[p] = j
				break
			elif s[i] == 0:
				break

		return tuple(s)

		
		
	def ganancia(self, s):
		return 0
		
	def terminal(self, s):
		if 0 not in s:
			return True
		elif len(self.jugadas_legales(s, 1)) == 0 and len(self.jugadas_legales(s, -1)) == 0:
			return True
		return self.ganancia(s) != 0