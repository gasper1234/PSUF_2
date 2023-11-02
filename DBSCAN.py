import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

DATA = np.load('tSNE_'+str(20)+'.npy')

eps_s = [1, 1.5, 2, 3]
min_samples = [10, 15, 20]
fig, ax = plt.subplots(len(eps_s), len(min_samples), sharex=True, sharey=True)
plt.subplots_adjust(wspace=0, hspace=0, top=0.98, right=0.98)

for i in range(len(eps_s)):
	ax[i, 0].set_ylabel(r'$\varepsilon=$'+str(eps_s[i]), fontsize=12)
	for j in range(len(min_samples)):
		if i == 0:
			ax[i, j].set_title('min_samp='+str(min_samples[j]), fontsize=12)
		eps_val = eps_s[i]
		min_samples_val = min_samples[j]
		clustering = DBSCAN(eps=eps_val, min_samples=min_samples_val).fit(DATA)

		labels = clustering.labels_

		cmap = plt.get_cmap('rainbow')
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

		ax[i, j].scatter(DATA[:, 0], DATA[:, 1], marker='.', alpha=alpha_s, color=colors)
		ax[i, j].tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=False, labelbottom=False)
plt.show()



