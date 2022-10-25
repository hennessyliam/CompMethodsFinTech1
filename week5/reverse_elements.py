# Reverse elements in slice S[start:stop]

def reverse(seq, start, stop):
	if start == stop - 1 or start == stop:
		return seq
	elif start < stop - 1:
		seq[start], seq[stop-1] = seq[stop-1], seq[start]
		return reverse(seq, start+1, stop-1)


seq1 = [2, 5, 7, 9, 11]
print(reverse(seq1, 0, 4))
