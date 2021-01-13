#pylint:disable=E1101
import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	 # cri  random_walk
	rw = RandomWalk()
	rw.fill_walk() 
	
	plt.style.use('classic')
	fig , ax = plt.subplots()
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s = 15)
	
	# marca o inicio e o fim
	ax.scatter(0, 0, c='green', edgecolor='none', s=1000)	
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=1000)
	
	plt.show()
	
	# pergunta se deve ser gerado outra rw
	keep_running = input("Make anither Walk? (y/n): ")
	
	if keep_running == 'n':
		break
