import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

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


# if DATA saved, perp must be in perp_s list ***
DATA = np.load('tSNE_'+str(20)+'.npy')

fig, ax = plt.subplots(3, sharex=True)

cmap = plt.get_cmap('plasma')  # You can choose any colormap you prefer

# Create a list of colors by sampling the colormap

for i in range(3):
	
	ax[i].tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False) 
	ax[i].scatter(DATA[:,0], DATA[:,1], marker='.', alpha=0.1)

	points_0 = []
	points_1 = []
	for j in range(len(labels)):
		l = labels[j]
		points_0.append(DATA[l, 0])
		points_1.append(DATA[l, 1])
	N = max(values[i])
	min_val = min(values[i])
	N -= min_val
	colors = [cmap((i-min_val) / N) for i in values[i]]
	ax[i].scatter(points_0, points_1, color=colors)



ax[0].set_title('T', x=1.04, y=0.45, rotation = 270)
ax[1].set_title('g', x=1.04, y=0.45, rotation = 270)
ax[2].set_title('kovinskost', x=1.04, y=0.3, rotation = 270)
ax[0].set_ylabel('X2')
ax[1].set_ylabel('X2')
ax[2].set_ylabel('X2')
ax[2].set_xlabel('X1')
plt.show()