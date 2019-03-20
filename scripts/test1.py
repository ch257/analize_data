items = [6,5,1,2,2,4,5,3,6,0,1]
ins = []

for k in items:
	print(k)
	inserted = False
	for i in range(len(ins)):
		if ins[i] > k:
			m = ins[i]
			ins[i] = k
			k = m
		elif ins[i] == k:
			inserted = True
			break
		
	if not inserted:
		ins.append(k)
		
print(ins)