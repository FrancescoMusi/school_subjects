import os
import sys

#classe contenente i colori
class FgColors:
	white = '\033[97m'
	red = '\033[31m'
	green = '\033[32m'
	rs = '\033[00m'

#pulisce lo schermo
def clear():
	IS_WINDOWS = sys.platform.lower() == "win32"
	if IS_WINDOWS:
		os.system('cls')
	else:
		os.system('clear')

#legge il file txt e restituisce una lista con le righe
def getRows(file):
	file = open('./'+file, 'r')
	r = file.readlines()
	file.close()
	rows = []

	for i in r:
		if i != '\n':
			rows.append(i.replace('\n', ''))

	return rows

#stampa tutto colorato
def draw(rows):

	print('---by Francesco Musi---\nPANORAMICA PER MATERIA:\n')


	#media[0] corrisponde a materia[0]
	materie = []
	medie = []
	voti = []
	voti_max = []
	voti_min = []


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

	#scorre i voti, medie... e se sono suffucienti gli attribuisce il colore verde, altrimenti rosso
	for i in range(len(materie)):
		data = [medie[i], voti_max[i], voti_min[i]]
		data = [str(x) for x in data]

		media, voto_max, voto_min = data

		#attribuisce il colore a questi valori di questa materia 
		if float(data[0]) > 6:
			media = FgColors.green+data[0]+FgColors.rs
		else:
			media = FgColors.red+data[0]+FgColors.rs

		if float(data[1]) > 6:
			voto_max = FgColors.green+data[1]+FgColors.rs
		else:
			voto_max = FgColors.red+data[1]+FgColors.rs

		if float(data[2]) > 6:
			voto_min = FgColors.green+data[2]+FgColors.rs
		else:
			voto_min = FgColors.red+data[2]+FgColors.rs

		###STAMPA LA PANORAMICA (per ogni materia)###
		print('{}:\n\tvoti: {}\n\tmedia: {}\n\tvoto massimo: {}\n\tvoto minimo: {}\n'.format(materie[i].upper(), voti[i], media, voto_max, voto_min))

	###STAMPA LE MEDIE COLORATE###
	print('\n\nMEDIE')
	for i in range(len(materie)):
		color = FgColors.white
		if medie[i] < 6:
			color = FgColors.red
		else:
			color = FgColors.green
		print('{}: {}'.format(materie[i], color+str(medie[i])+FgColors.rs))

	###STAMPA LA PROBABILE PAGELLA COLORATA###
	print('\n\nPAGELLA')
	for i in range(len(materie)):
		color = FgColors.white
		if round(medie[i]) < 6:
			color = FgColors.red
		else:
			color = FgColors.green
		print('{}: {}'.format(materie[i], color+str(round(medie[i]))+FgColors.rs))

	##########################################################
	#################### DA FARE: RECUPERI ###################
	##########################################################

#mainloop
while True:
	clear()
	rows = getRows('votes.txt')
	draw(rows)
	z = input('\nreload (q per uscire)')
	if z.lower() == 'q':
		clear()
		break
