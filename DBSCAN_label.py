import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

# get dict of values
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

label_names = ['MAB', 'BIN', 'TRI', 'HFR', 'HAE', 'CMP', 'DIB', 'GA']
data_dict['GA'] = [26, 115, 117, 119, 120, 137, 176, 184, 228, 304, 449, 556, 873, 928, 940, 984, 1047, 1094, 1111, 1136, 1154, 1185, 1230, 1232, 1360, 1385, 1491, 1510, 1548, 1629, 1692, 1703, 1847, 1869, 1924, 1964, 2025, 2076, 2078, 2103, 2211, 2320, 2358, 2398, 2549, 2560, 2583, 2633, 2732, 2772, 2782, 2789, 2790, 2854, 2979, 3138, 3196, 3201, 3280, 3372, 3414, 3415, 3429, 3435, 3606, 3781, 3788, 3797, 3902, 3951, 4008, 4010, 4011, 4056, 4196, 4208, 4217, 4220, 4257, 4319, 4334, 4339, 4377, 4383, 4446, 4604, 4607, 4667, 4836, 4852, 4893, 4946, 5006, 5058, 5147, 5218, 5880, 6188, 6190, 6191, 6211, 6219, 6241, 6242, 6257, 6607, 6697, 6753, 7237, 7284, 7434, 7611, 7771, 7830, 7994, 8061, 8749, 8907, 9234, 9449, 9555, 9603, 9742, 9789, 9857, 9868, 9888, 9976]
groups = [[] for _ in range(len(label_names))]
locations_x = [[] for _ in range(len(label_names))]
locations_y = [[] for _ in range(len(label_names))]
group_labels = [[2, 15], [36], [48], [12, 16, 28], [7, 37], [4], [8], [9]]
#                ok    ??,ni vse  ok   semi ok     ok        ok   ok
# v naslednjih vrsticah samo tiste za katere je jasno - brez binarnih
#group_labels = [[2, 15], [48], [12, 16, 28], [7, 37], [4], [8]]
#label_names = ['MAB', 'TRI', 'HFR', 'HAE', 'CMP', 'DIB']
ind = 1
# označeno je kam spadajo posamezne zvezde (v katere skupin DBSCANA) pobarvaj da bodo vsi skupaj

DATA = np.load('tSNE_'+str(20)+'.npy')

#eps_val = 2
eps_val = 1.85
min_samples_val = 15
#fig, ax = plt.subplots(len(eps_s), len(min_samples), sharex=True, sharey=True)
#plt.subplots_adjust(wspace=0, hspace=0, top=0.98, right=0.98)

clustering = DBSCAN(eps=eps_val, min_samples=min_samples_val).fit(DATA)

labels = clustering.labels_

for i in range(len(label_names)):
	for n_th in data_dict[label_names[i]]:
		groups[i].append(labels[n_th])
		locations_x[i].append(DATA[n_th, 0])
		locations_y[i].append(DATA[n_th, 1])

known_labels = np.ones_like(labels)*(-1)
for i in range(len(labels)):
	label = labels[i]
	for j in range(len(label_names)):
		if label in group_labels[j]:
			known_labels[i] = j

labels = known_labels
# ------------------------------------------------------------------------------------
# plotting

cmap = plt.get_cmap('gist_rainbow')
cmap = plt.get_cmap('jet')

# create color for each point
N_col = np.max(labels)+1
colors = []
alpha_s = []
for k in range(len(labels)):
	label = labels[k]
	if label == -1:
		colors.append('k')
		alpha_s.append(0.1)
	else:
		colors.append(cmap(label/N_col))
		alpha_s.append(0.5)

plt.scatter(DATA[:, 0], DATA[:, 1], marker='.', alpha=alpha_s, color=colors)
plt.tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False)

import matplotlib.patches as mpatches
patch_list = [mpatches.Patch(color=cmap(i/(N_col)), label=label_names[i]) for i in range(N_col)]

plt.legend(handles=patch_list)
plt.xlabel('X1')
plt.ylabel('X2')
# for matching labels and groups
'''
print(groups[ind])
plt.scatter(locations_x[ind], locations_y[ind], marker='x', color='k', label=label_names[ind])
plt.legend()
'''

# rocna legenda

plt.show()
