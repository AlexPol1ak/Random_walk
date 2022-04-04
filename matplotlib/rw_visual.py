import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()
	#rw.showlists()

	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9), dpi=128)
	point_number = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c = point_number, cmap=plt.cm.Blues, edgecolors = 'none', s = 1)
	ax.scatter(0, 0 , c= 'green', edgecolors = 'none', s = 100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100 )
	#plt.plot(rw.x_values, rw.y_values, linewidth = 1)

	# Удаление осей.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()
	#plt.savefig('random_walk.png', bbox_inches= 'tight')
	#rw.showlists()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break

