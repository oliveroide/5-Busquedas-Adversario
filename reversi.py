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
			return tuple([0 for _ in range(8 * 8)])
			
	def jugadas_legales(self, s, j):
			return 0
		
	def sucesor(self, s, a, j):
		s = list(s[:])
		return tuple(s)

		
		
	def ganancia(self, s):
		return 0
		
	def terminal(self, s):
		if 0 not in s:
			return True
		return self.ganancia(s) != 0