"""Ananthan Nambiar
   Code that simulates the Heraclitean idea of
   conversion of fire, seas and earth.
"""
def cycles(n):
	f =1
	e = 0
	s = 0
	while n > 0:
		if f > 0:
			s = s + f
			f = 0
		if s > 0:
			f = f +0.5 * s
			e = e + 0.5 * s
			s = 0
		if e > 0:
			s = s + e
			e = 0
		n = n-1
		string = "fire:" + str(f) + ", sea:" + str(s) + ", earth:" + str(e)
	print (string)
