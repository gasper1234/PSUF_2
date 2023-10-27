import matplotlib.pyplot as plt
import numpy as np

DATA = np.load('PCA_reduced_5.npy')

# add scatter data: use data_dict to find groups
labels = []
values = [[], [], []]
with open("parametri.txt", "r") as file:
	next(file)
	for line in file:
		# Split each line into columns
		columns = line.strip().split()
		
		# Ensure that there are exactly 2 columns
		if len(columns) == 4:
			labels.append(int(columns[0])-1)
			values[0].append(float(columns[1]))
			values[1].append(float(columns[2]))
			values[2].append(float(columns[3]))

value_names = ['T', 'g', 'kovinskost']

fig, ax = plt.subplots(3, 3, sharex='col')
plt.subplots_adjust(wspace=0, hspace=0)

print(labels)
print(values)

for x in range(3):
	ax[2, x].set_xlabel('X'+str(x))
	ax[x, 0].set_ylabel(value_names[x])
	for i in range(len(value_names)):

		points_0 = []

		for j in labels:
			points_0.append(DATA[j, x])
		ax[i, x].scatter(points_0, values[i])

		# ticks
		ax[i, x].tick_params(direction='in')
		ax[i, x].yaxis.set_ticks_position('both')
		ax[i, x].xaxis.set_ticks_position('both')
		if x > 0:	
			ax[i, x].get_yaxis().set_visible(False)

plt.show()