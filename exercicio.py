import matplotlib.pyplot as plt
 
x_axis = range(0, 5000) 
y_axis = [x**3 for x in x_axis]

plt.style.use('seaborn')

fig, ax = plt.subplots() 
ax.scatter(x_axis, y_axis, c=y_axis, cmap=plt.cm.Blues, s=100)

ax.axis([0, 5100, 0, 135000000000])

plt.show()