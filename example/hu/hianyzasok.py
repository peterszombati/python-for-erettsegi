def feladat(x):
	print(x,'. feladat',sep='')

# 1. feladat
f = open('forras/naplo.txt', 'r')
content = f.read()
f.close()
content = content.split('\n')
for i in range(len(content)):
	content[i] = content[i].strip("\r")

# 2. feladat
feladat(2)

hianyzas = 0
for i in range(len(content)):
	if (content[i][0] != "#" and len(content[i]) > 0):
		hianyzas += 1
print('A naplóban ',hianyzas,' bejegyzés van.',sep='')

# 3. feladat
'''
O = jelen
X = igazolt
I = igazolatlan
'''
feladat(3)

i = 0
x = 0
for j in range(len(content)):
	if (len(content[j]) > 0 and content[j][0] != "#"):
		line = content[j].split(' ')
		line = line[len(line) - 1]
		for j2 in range(len(line)):
			if (line[j2] == 'X'):
				x += 1
			elif (line[j2] == 'I'):
				i += 1
print('Az igazolt hiányzások száma ',x,', az igazolatlanoké ',i,' óra.',sep='')

# 4. feladat
def hetnapja(honap, nap):
	napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
	napszam = [0,31,59,90,120,151,181,212,243,273,304,335]
	napsorszam = (napszam[honap - 1] + nap) % 7
	return napnev[napsorszam]

# 5. feladat
feladat(5)

honap = int(input('A hónap sorszáma='))
nap = int(input('A nap sorszáma='))
print('Azon a napon ',hetnapja(honap, nap),' volt.',sep='')

# 6. feladat
feladat(6)

napneve = input('A nap neve=')
ora = int(input('Az óra sorszáma='))
aktiv = False
hianyzas = 0
for i in range(len(content)):
	if (len(content[i]) > 0):
		if (content[i][0] == "#"):
			line = content[i].split(' ')
			nap = int(line[2])
			honap = int(line[1])
			if (hetnapja(honap, nap) == napneve):
				aktiv = True
			else:
				aktiv = False
		elif (aktiv == True):
			line = content[i].split(' ')
			line = line[len(line) - 1]
			if (len(line) >= ora and (line[ora - 1] =='I' or line[ora - 1] == 'X')):
				hianyzas += 1
print('Ekkor összesen ',hianyzas,' óra hiányzás történt.',sep='')

# 7. feladat
feladat(7)

tanulok = []

def tanulo(data):
	place = -1
	for i in range(len(tanulok)):
		if (len(tanulok[i]) == len(data)):
			match = True
			for i2 in range(len(tanulok[i]) - 1):
				if (tanulok[i][i2] != data[i2]):
					match = False
					break
			if (match == True):
				place = i
				break

	line = data[len(data) - 1]
	if (place == -1):
		tanulok.append(data)
		place = len(tanulok) - 1
		tanulok[place][len(tanulok[place]) - 1] = 0

	hianyzas = 0
	for i in line:
		if (i == 'X' or i == 'I'):
			hianyzas += 1
	tanulok[place][len(tanulok[place]) - 1] += hianyzas

for i in range(len(content)):
	if (len(content[i]) > 0 and content[i][0] != "#"):
		tanulo(content[i].split(' '))

def a(key):
	return key[len(key) - 1]

tanulok = sorted(tanulok, key=a)

legtobb = tanulok[len(tanulok) - 1][len(tanulok[len(tanulok) - 1]) - 1]

nevek = ''
i = len(tanulok) - 1
while(i >= 0):
	d = tanulok[i]
	i -= 1
	if (d[len(d) -1] != legtobb):
		break

	i2 = 0
	while(i2 < len(d) - 1):
		if (len(nevek) > 0):
			nevek += ' '
		nevek += d[i2]
		i2 += 1
print('A legtöbbet hiányzó tanulók: ',nevek,sep='')