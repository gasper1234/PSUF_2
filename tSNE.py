import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

perp_s = [5, 10, 20, 30, 50, 100]
# if DATA not saved ***
'''
DATA_raw = np.load('DATA.npy')

average_val = np.sum(DATA_raw, axis=0)/DATA_raw.shape[0]
DATA_raw -= average_val[np.newaxis, :]

for l in perp_s:
	DATA = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=l).fit_transform(DATA_raw)

	np.save('tSNE_'+str(l)+'.npy', DATA)
'''
# grupe
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

fig, axes = plt.subplots(3, 2)
ax_s = [axes[0, 0], axes[0, 1], axes[1, 0], axes[1, 1], axes[2, 0], axes[2, 1]]
plt.subplots_adjust(wspace=0.03, hspace=0.03, top=0.98, right=0.98)

# if DATA saved, perp must be in perp_s list ***
for i in range(len(perp_s)):
	ax = ax_s[i]
	perp = perp_s[i]
	DATA = np.load('tSNE_'+str(perp)+'.npy')

	ax.tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False) 
	ax.scatter(DATA[:,0], DATA[:,1], marker='.', alpha=0.1)


	# draw 3 corner plot

	# make 3 corner plot for P1, P2, P3
	colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
	for k in range(len(labels)):
		points_0 = []
		points_1 = []
		for j in data_dict[labels[k]]:
			points_0.append(DATA[j, 0])
			points_1.append(DATA[j, 1])
		ax.scatter(points_0, points_1, color=colors[k])

	ax.legend(title='p='+str(perp_s[i]))
	if i%2 == 0:
		ax.set_ylabel('X2')
	if i > 3:
		ax.set_xlabel('X1')




plt.show()
