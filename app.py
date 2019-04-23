import os
import sys

class FgColors:
	white = '\033[97m'
	red = '\033[31m'
	green = '\033[32m'
	rs = '\033[00m'


def clear():
	IS_WINDOWS = sys.platform.lower() == "win32"
	if IS_WINDOWS:
		os.system('cls')
	else:
		os.system('clear')


def getRows(file):
	file = open('./'+file, 'r')
	r = file.readlines()
	file.close()
	rows = []

	for i in r:
		if i != '\n':
			rows.append(i.replace('\n', ''))

	return rows


def draw(rows):

	#media[0] corrisponde a materia[0]
	materie = []
	medie = []
	voti = []
	voti_max = []
	voti_min = []

	materie_da_recuperare = []
	voti_della_materia_da_recuperare = []
	lista_voti_necessari = []

	for i in range(len(rows)):
		if i%2 == 0:
			#aggiungi materia
			materie.append(rows[i])
		else:
			#aggiungi i voti 
			voti_matria_corrente = rows[i].split()
			voti_matria_corrente = [float(i) for i in voti_matria_corrente]
			voti.append(voti_matria_corrente)

			#aggiungi le medie
			medie.append(round(sum(voti_matria_corrente)/len(voti_matria_corrente), 2))
			
			#aggiungi voto massimo
			voti_max.append(max(voti_matria_corrente))

			#aggiungi voto minimo
			voti_min.append(min(voti_matria_corrente))

	for i in range(len(materie)):
		print('{}:\n\tvoti: {}\n\tmedia: {}\n\tvoto massimo: {}\n\tvoto minimo: {}\n'.format(materie[i].upper(), voti[i], medie[i], voti_max[i], voti_min[i]))

	print('\n\nMEDIE')
	for i in range(len(materie)):
		color = FgColors.white
		if medie[i] < 6:
			color = FgColors.red
		else:
			color = FgColors.green
		print('{}: {}'.format(materie[i], color+str(medie[i])+FgColors.rs))

	print('\n\nPAGELLA')
	for i in range(len(materie)):
		color = FgColors.white
		if round(medie[i]) < 6:
			color = FgColors.red
		else:
			color = FgColors.green
		print('{}: {}'.format(materie[i], color+str(round(medie[i]))+FgColors.rs))

	for i in medie:
		if i < 6:
			index = medie.index(i)
			materie_da_recuperare.append(materie[index])
			voti_delle_materie_da_recuperare.append(voti[index])

			#ottieni lista voti per recuperare (lista_voti_necessari)
			for v in range(600, 1000):
				voti_necessari_materia_corrente = []
				l = voti[index]
				l.append(v/100)
				if sum(l)/len(l) >= 6:
					voti_necessari_materia_corrente.append(v/100)
					lista_voti_necessari.append(voti_necessari_materia_corrente)
					break
			else:
				shit = True

	print(voti_delle_materie_da_recuperare)

	if len(materie_da_recuperare) > 0 and not shit:
		print('\n\nRECUPERI')
		for i in range(len(materie_da_recuperare)):
			print('{}: hai {} e ti serve {} per recuperare'.format(materie_da_recuperare[i]), voti_delle_materie_da_recuperare[i], lista_voti_necessari[i])
	elif shit:
		print('Ti serve un voto maggiore di 10: spegni il computer e comincia a studiare ')


while True:
	clear()
	rows = getRows('votes.txt')
	draw(rows)
	input()
