d=0
s=0
t=[0]*7
while d<=6:
	t[d] =int(input("Δώσε θερμοκρασία ημέρας: "))
	s=s+t[d]
	d+=1
d=0
c=0
m=s/7
while d<=6:
	if d==0:
		mini=t[0]
		maxi=t[0]
		flag=1
	else:
		if mini>t[d]:
			mini=t[d]
		if maxi<t[d]:
			maxi=t[d]
	if t[d]>m:
		c+=1
	d+=1
print("Μέση θερμοκρασία:", m)
print("Ημέρες με θερμοκρασία πάνω από τον μέσο όρο:", c)
print("Μικρότερη θερμοκρασία:", mini)
print("Μεγαλύτερη θερμοκρασία:", maxi)
