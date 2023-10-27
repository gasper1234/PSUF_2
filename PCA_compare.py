import matplotlib.pyplot as plt
import numpy as np

DATA = np.load('PCA_reduced_5.npy')

# add scatter data: use data_dict to find groups
data_dict = {}
with open("tipi.txt", "r") as file:
	for line in file:
		# Split each line into columns
		columns = line.strip().split()
		
		# Ensure that there are exactly 2 columns
		if len(columns) == 2:
			number, label = columns
			# Convert the number to an integer (you can use float for decimal numbers)
			number = int(number)
			
			# Check if the label already exists in the dictionary
			if label in data_dict:
				data_dict[label].append(number-1)
			else:
				data_dict[label] = [number-1]


labels = ['MAB', 'BIN', 'TRI', 'HFR', 'HAE', 'CMP', 'DIB']

# draw 3 corner plot

# make 3 corner plot for P1, P2, P3

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

axes = [ax[1, 0], ax[0, 0], ax[1, 1]]

indices = [(0, 1), (0, 2), (2, 1)]

for k in range(len(indices)):
	labeled_poinst_x = []
	labeled_poinst_y = []
	ind_1, ind_2 = indices[k][0], indices[k][1]
	for i in range(len(labels)):
		points_0 = []
		points_1 = []
		for j in data_dict[labels[i]]:
			points_0.append(DATA[j, ind_1])
			points_1.append(DATA[j, ind_2])
		labeled_poinst_x.append(points_0)
		labeled_poinst_y.append(points_1)

	axes[k].scatter(DATA[:,ind_1], DATA[:,ind_2], marker='.', alpha=0.1)

	# ticks

	axes[k].tick_params(direction='in')
	axes[k].yaxis.set_ticks_position('both')
	axes[k].xaxis.set_ticks_position('both')

	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
	for i in range(len(labels)):
		axes[k].scatter(labeled_poinst_x[i], labeled_poinst_y[i], color=colors[i], label=labels[i])

axes[1].legend(bbox_to_anchor=(1.8, 1.05))
axes[0].set_ylabel('X2')
axes[1].set_ylabel('X1')
axes[0].set_xlabel('X0')
axes[2].set_xlabel('X2')
ax[0,1].remove()

plt.show()

