import matplotlib.pyplot as plt 

from random_walk import RandomWalk

while True:
	 # cri  random_walk
	rw = RandomWalk()
	rw.fill_walk() 
	
	plt.style.use('classic')
	fig , ax = plt.subplots()
	
	ax.scatter(rw.x_values, rw.y_values, s = 15)
	
	plt.show()
	
	# pergunta se deve ser gerado outra rw
	keep_running = input("Make anither Walk? (y/n): ")
	
	if keep_running == 'n':
		break
