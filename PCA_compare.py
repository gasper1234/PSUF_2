import matplotlib.pyplot as plt
import numpy as np

DATA = np.load('PCA_reduced_5.npy')

# draw 3 corner plot

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
				data_dict[label].append(number)
			else:
				data_dict[label] = [number]


labels = ['MAB', 'BIN', 'TRI', 'HFR', 'HAE', 'CMP', 'DIB']

# make 3 corner plot for P1, P2, P3

labeled_poinst_x = []
labeled_poinst_y = []
ind_1 = 0
ind_2 = 1
for i in range(len(labels)):
	points_0 = []
	points_1 = []
	for j in data_dict[labels[i]]:
		points_0.append(DATA[j, ind_1])
		points_1.append(DATA[j, ind_2])
	labeled_poinst_x.append(points_0)
	labeled_poinst_y.append(points_1)

plt.scatter(DATA[:,0], DATA[:,1], marker='.', alpha=0.1)

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
for i in range(len(labels)):
	plt.scatter(labeled_poinst_x[i], labeled_poinst_y[i], color=colors[i], label=labels[i])
plt.legend()

plt.show()

