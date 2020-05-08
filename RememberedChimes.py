import random
import math

M = int(raw_input('number of morning songs: '))
A = int(raw_input('number of afternoon songs: '))
E = int(raw_input('number of evening songs: '))

M_meas = [138] # morning rag
A_meas = []
E_meas = []

for i in range(1, M + 1):
    M_meas.append(int(raw_input('measures in morning song ' + str(i) + ': ')))
for i in range(1, A + 1):
    A_meas.append(int(raw_input('measures in afternoon song ' + str(i) + ': ')))
for i in range(1, E + 1):
    E_meas.append(int(raw_input('measures in evening song ' + str(i) + ': ')))

A_meas.append(32) # alma mater
E_meas.append(32) # evening song

M_prop = []
A_prop = []
E_prop = []

for i in M_meas:
    M_prop.append(int(round(float(i) / sum(M_meas) * 15)))
for i in A_meas:
    A_prop.append(int(round(float(i) / sum(A_meas) * 15)))
for i in E_meas:
    E_prop.append(int(round(float(i) / sum(E_meas) * 15)))

if sum(M_prop) != 15:
    diff = 15 - sum(M_prop)
    if diff < 0:
        M_prop[M_prop.index(max(M_prop))] = max(M_prop) + diff
    else:
        M_prop[M_prop.index(min(M_prop))] = min(M_prop) + diff
if sum(A_prop) != 15:
    diff = 15 - sum(A_prop)
    if diff < 0:
        A_prop[A_prop.index(max(A_prop))] = max(A_prop) + diff
    else:
        A_prop[A_prop.index(min(A_prop))] = min(A_prop) + diff
if sum(E_prop) != 15:
    diff = 15 - sum(E_prop)
    if diff < 0:
        E_prop[E_prop.index(max(E_prop))] = max(E_prop) + diff
    else:
        E_prop[E_prop.index(min(E_prop))] = min(E_prop) + diff

playlist = []

for i in range(0, M + 1):
    rand = []
    for j in range(0, M_prop[i]):
        rand.append(random.random())
    rand.sort()
    for j in range(0, len(rand)):
        length = int(math.ceil(random.random() * 3))
        playlist.append(['M' + str(i + 1), int(math.ceil(rand[j] * M_meas[i])), round(random.random(), 3), length])
for i in range(0, A + 1):
    rand = []
    for j in range(0, A_prop[i]):
        rand.append(random.random())
    rand.sort()
    for j in range(0, len(rand)):
        length = int(math.ceil(random.random() * 3))
        playlist.append(['A' + str(i + 1), int(math.ceil(rand[j] * A_meas[i])), round(random.random(), 3), length])
for i in range(0, E + 1):
    rand = []
    for j in range(0, E_prop[i]):
        rand.append(random.random())
    rand.sort()
    for j in range(0, len(rand)):
        length = int(math.ceil(random.random() * 3))
        playlist.append(['E' + str(i + 1), int(math.ceil(rand[j] * E_meas[i])), round(random.random(), 3), length])

for i in playlist:
    print i