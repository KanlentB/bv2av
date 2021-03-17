table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
	tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608

def dec(x):
	r=0
	for i in range(6):
		r+=tr[x[s[i]]]*58**i
	return (r-add)^xor

with open(r"BV.txt","r") as f:
    data=f.readlines()
print(len(data))
with open(r"av.txt","w") as f:
    num=0
    while num<len(data):
        f.write('av'+str(dec(data[num]))+'\n')
        num+=1