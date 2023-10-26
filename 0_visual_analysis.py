import matplotlib.pyplot as plt
import numpy as np

# load data

wav = np.loadtxt('spektri/val.dat', comments='#')

DATA = np.load('DATA.npy')

# make learning dict

filename = 'spektri/'

data_dict = {}

# Open and read the file
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
label_Ns = [0, 0, 0, 0, 0, 0, 0]

# find most diverse
max_val = 0
for i in range(len(data_dict['MAB'])):
	for j in range((len(data_dict['BIN']))):
		val = np.sum(DATA[data_dict['MAB'][i]] - DATA[data_dict['BIN'][j]])**2
		if val > max_val:
			max_val = val
			label_Ns[0], label_Ns[1] = i, j

for i in range(2, len(label_Ns)):
	max_val = 0
	for j in range(len(data_dict[labels[i]])):
		val = np.sum(DATA[data_dict[labels[i-1]][i]] - DATA[data_dict[labels[i]][j]])**2
		if val > max_val:
			max_val = val
			label_Ns[i] = j

print(label_Ns)


fig, ax = plt.subplots(len(label_Ns), figsize=(8, 10), sharex=True)
plt.subplots_adjust(hspace=0)

for i in range(len(label_Ns)):
	ax[i].plot(wav, DATA[data_dict[labels[i]][label_Ns[i]]], label=labels[i])
	ax[i].legend()
	ax[i].tick_params(direction='in')
	ax[i].yaxis.set_ticks_position('both')
	ax[i].xaxis.set_ticks_position('both')
	ax[i].set_ylabel(r'$\Phi$')
ax[len(label_Ns)-1].set_xlabel(r'$\lambda$')
plt.show()
