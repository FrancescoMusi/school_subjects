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

	


while True:
	clear()
	rows = getRows('votes.txt')
	draw(rows)
	input()
