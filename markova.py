from random import choice

class MarkovChains:
	def __init__(self, data, sp="слово"):
		self.sp = sp
		self.base = {}
		if type(data) == str:
			self.dataset = self.funktsyja(data)
		elif type(data) == list:
			self.dataset = data

	def learn(self):
		for i, word in enumerate(self.dataset):
			if i < len(self.dataset)-1:
				self.addChain(word, self.dataset[i+1])

	def addChain(self, key, value):
		if key not in self.base:
			self.base[key] = [value]
		else:
			self.base[key].append(value)

	def generateSequence(self, lenght, auth=None):
		if not auth:
			auth = choice([key for key in self.base])
		if auth == "<start>":
			auth = " "
		current = self.base[auth]
		out = []
		for now in range(lenght):
			try :
				key = choice(current)
				current = self.base[key]
				out.append(key)
			except KeyError:
				return out

		return out

	def funktsyja(self, filename):
		with open(filename, "r", encoding="UTF-8") as text:
			r = text.read()
			r = r.replace("\n", " ")
			r = r.replace(".", "")
			r = r.replace("!", "")
			for i in range(7):
				r = r.replace("  ", " ")
			if self.sp == "слово":
				rl = r.split(" ")
			elif self.sp == "буква":
				rl = []
				for i in r:
					rl.append(i)
			return r
		