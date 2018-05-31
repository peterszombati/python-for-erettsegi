# 1. feladat
f = open('forras/naplo.txt', 'r')
content = f.read()
data = []
f.close()
content = content.split('\n')
datum = [-1,-1]
for i in range(len(content)):
	content[i] = content[i].strip("\r")
	if (len(content[i]) > 0):
		content[i] = content[i].split(' ')
		if(content[i][0][0] == '#'):
			datum = [int(content[i][1]),int(content[i][2])]
		elif(datum[0] != -1):
			nev = ''
			for i2 in range(len(content[i]) - 1):
				if (i2 != 0):
					nev += ' '
				nev += content[i][i2]
			data.append([nev, content[i][len(content[i]) - 1], datum[0], datum[1]])
def a(x):
	return x[0]
data = sorted(data, key=a)
# 2. feladat
print('2. feladat')
print('A naplóban ',len(data),' bejegyzés van.',sep='')

# 3. feladat
print('3. feladat')
x=0
y=0
for i in data:
	i = i[1]
	for j in i:
		if(j == 'X'):
			x+=1
		elif(j == 'I'):
			y+=1
print('Az igazolt hiányzások száma ',x,', az igazolatlanoké ',y,' óra.',sep='')

# 4. feladat
def hetnapja(honap, nap):
	napnev = ["vasarnap","hetfo","kedd","szerda","csutortok","pentek","szombat"]
	napszam = [0,31,59,90,120,151,181,212,243,273,304,335]
	napsorszam = (napszam[honap - 1] + nap) % 7
	return napnev[napsorszam]

# 5. feladat
print('5. feladat')
honap = int(input('A hónap sorszáma='))
nap = int(input('A nap sorszáma='))
print('Azon a napon ',hetnapja(honap,nap),' volt.',sep='')

# 6. feladat
print('6. feladat')
nap = input('A nap neve=')
ora = int(input('Az óra sorszáma='))
h = 0
for i in data:
	if(hetnapja(i[2],i[3]) == nap):
		if (len(i[1]) >= ora):
			if (i[1][ora - 1] == 'X' or i[1][ora - 1] == 'I'):
				h += 1
print('Ekkor összesen ',h,' óra hiányzás történt.',sep='')
# 7. feladat
print('7. feladat')
for i in range(len(data)):
	h = 0
	for j in data[i][1]:
		if (j == 'X' or j == 'I'):
			h+=1
	data[i][1] = h
tanulok = []
for i in range(len(data)):
	place = -1
	for i2 in range(len(tanulok)):
		if (data[i][0] == tanulok[i2][0]):
			place = i2
			break
	if (place == -1):
		tanulok.append([data[i][0],data[i][1]])
	else:
		tanulok[place][1] += data[i][1]
def b(x):
	return x[1]
tanulok = sorted(tanulok, key=b)
legtobb = tanulok[len(tanulok) - 1][1]

i = len(tanulok) - 1
nevek = ''
while(i >= 0 and tanulok[i][1] == legtobb):
	nevek += ' '
	nevek += tanulok[i][0]
	i -= 1
print('A legtöbbet hiányzó tanulók:',nevek,sep='')