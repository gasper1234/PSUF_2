import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

labels = []
values = []
with open("parametri.txt", "r") as file:
	next(file)
	for line in file:
		# Split each line into columns
		columns = line.strip().split()
		
		# Ensure that there are exactly 2 columns
		if len(columns) == 4:
			labels.append(int(columns[0])-1)
			values.append(float(columns[1]))

value_name = 'T'


# if DATA saved, perp must be in perp_s list ***
DATA = np.load('tSNE_'+str(20)+'.npy')

fig, ax = plt.subplots(2)

T_all = np.load('2.5T_fit.npy')

cmap = plt.get_cmap('plasma')  # You can choose any colormap you prefer

# Create a list of colors by sampling the colormap

ax[0].tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False) 
ax[1].tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False) 
ax[0].scatter(DATA[:,0], DATA[:,1], marker='.', alpha=0.1)

points_0 = []
points_1 = []
for j in range(len(labels)):
	l = labels[j]
	points_0.append(DATA[l, 0])
	points_1.append(DATA[l, 1])
N = max(values)
min_val = min(values)
N -= min_val
colors = [cmap((i-min_val) / N) for i in values]
colors_all = [cmap(i) for i in T_all]
ax[0].scatter(points_0, points_1, color=colors)

# uporabi ML za to !!!!!!!!!!!!!!!!!!!!!!!!!

ax[0].set_title(r'$T$', x=1.04, y=0.45, rotation = 270)
ax[0].set_ylabel('X2')
ax[0].set_xlabel('X1')
ax[1].set_title(r'$T_{fit}$', x=1.04, y=0.45, rotation = 270)
ax[1].set_ylabel('X2')
ax[1].set_xlabel('X1')
ax[1].scatter(DATA[:,0], DATA[:,1], marker='.', color=colors_all, alpha=0.3)
plt.show()