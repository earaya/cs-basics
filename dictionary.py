class Dictionary:

	def __init__(self):
		self.data = [None] * 256

	def put(self, key, value):
		# handle collisions:
		# 1. put value in a list
		# 2. find next open slot
		# 3. grow array and try again

		idx = self._hash(key)
		self.data[idx] = value

	def get(self, key):
		idx = self._hash(key)
		return self.data[idx]

	def _hash(self, key):
		# it's nice that pythong has a good hashing function.
		# another simple option would be to multiply by a large prime
		return hash(key) % len(self.data)

	def printer(self):
		print self.data

dictionary = Dictionary();
dictionary.put("testOne", "hello")
dictionary.put("testTwo", "world")
print dictionary.get("testOne")
print dictionary.get("testTwo")
