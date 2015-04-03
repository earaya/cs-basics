def permute_heap(xs, n):
	if n == 1:
		print xs
	else:
		for i in range(0, n):
			permute_heap(xs, n - 1)
			if n % 2 != 0:
				j = 0
			else:
				j = i
			xs[j], xs[n-1] = xs[n-1], xs[j]

def permute(xs):
	permute_heap(xs, len(xs))

permute(["a", "b", "c", "d"])
