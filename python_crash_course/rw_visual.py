#pylint:disable=E1101
import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	 # cri  random_walk
	rw = RandomWalk(50_000)
	rw.fill_walk() 
	
	plt.style.use('classic')
	fig , ax = plt.subplots(figsize=(9, 19), dpi=128)
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s = 1)
	
	# marca o inicio e o fim
	ax.scatter(0, 0, c='green', edgecolor='none', s=1000)	
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=1000)
	
	 # desabilita os eixos
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False) 
	 	 
	plt.show()
	
	# pergunta se deve ser gerado outra rw
	keep_running = input("Make anither Walk? (y/n): ")
	
	if keep_running == 'n':
		break
