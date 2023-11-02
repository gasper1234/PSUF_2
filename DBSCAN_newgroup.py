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

label_names = ['MAB', 'BIN', 'TRI', 'HFR', 'HAE', 'CMP', 'DIB']
ind = 1
# označeno je kam spadajo posamezne zvezde (v katere skupin DBSCANA) pobarvaj da bodo vsi skupaj

DATA = np.load('tSNE_'+str(20)+'.npy')

#eps_val = 2
eps_val = 1.85
min_samples_val = 15

clustering = DBSCAN(eps=eps_val, min_samples=min_samples_val).fit(DATA)

labels = clustering.labels_

print(max(labels))

ind_1 = 9
#labels[labels != 9] = -1
labels_9 = []
labels_basic = []
for i in range(len(labels)):
	l = labels[i]
	if l == 9:
		labels_9.append(i)
	if l < 3 and l > -1:
		labels_basic.append(i)
print(labels_9)
print(labels_basic)
# ------------------------------------------------------------------------------------
# plotting
'''
cmap = plt.get_cmap('gist_rainbow')
cmap = plt.get_cmap('hsv')

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

plt.show()
'''
# -----------------------------------------------------------------------------------
# specter plotting

DATA = np.load('DATA.npy')
ave = np.zeros_like(DATA[0])
ave_9 = np.zeros_like(DATA[0])

for i in range(len(labels_basic)):
	ave += DATA[labels_basic[i]]
ave /= len(labels_basic)

for i in range(len(labels_9)):
	ave_9 += DATA[labels_9[i]]
ave_9 /= len(labels_9)

wav = np.loadtxt('val.dat', comments='#')

plt.plot(wav, ave, label='povprecje')
plt.plot(wav, ave_9, label='skupina')
#plt.plot(ave_9-ave, label=2)
plt.legend()
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$\phi$')
plt.show()
