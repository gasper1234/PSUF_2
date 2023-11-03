import matplotlib.pyplot as plt
import numpy as np

# load data

wav = np.loadtxt('/home/project0/Documents/PSUF/spektri/val.dat', comments='#')

DATA = np.load('/home/project0/Documents/PSUF/DATA.npy')

def PCA(DATA, n):

	# center each dimension
	average_val = np.sum(DATA, axis=0)/DATA.shape[0]
	DATA -= average_val[np.newaxis, :]

	# covariance matrix
	cov = 1/DATA.shape[0] * np.matmul(DATA.transpose(), DATA)

	U, S, Vh = np.linalg.svd(DATA, full_matrices=True)

	sigma_square = S**2

	energ = np.sum(sigma_square)

	# vrne array ucinkovtiosti
	eff = [np.sum(sigma_square[:i])/energ for i in range(10)]
	
	# vrne le vrednost	
	#eff = np.sum(sigma_square[:n])/energ

	# matrix from eigenvector (lines of Vh)
	W = Vh[:n].transpose()

	return W, eff

# smaler sample for testing
DATA_test = DATA

# new number of diemnsions
N = 5

# matrix for dim reduciton
W, eff = PCA(DATA_test, N)

plt.plot(eff, 'x')
plt.xlabel('N')
plt.ylabel('g')
plt.tick_params(axis='both', which='both', direction='in', right=True, left=True, bottom=True, top=True, labelleft=True, labelbottom=True)
plt.show()
'''
# dim reduction
DATA_reduced = np.matmul(DATA_test, W)

#np.save('PCA_reduced_5.npy', DATA_reduced)

# corner plot
import seaborn as sns
import pandas as pd

data_corner = {}
for i in range(N):
	data_corner['X'+str(i)] = DATA_reduced[:, i]

sns.set(style="ticks")
g = sns.pairplot(
	pd.DataFrame(data_corner),
	corner=True,
	diag_kws=dict(bins=30),
	plot_kws=dict(marker="+", linewidth=1)
	)
#g.map_diag(sns.histplot, bins=30, color=".3")
g.map_lower(sns.kdeplot, levels=4, color=".2")
plt.show()
'''