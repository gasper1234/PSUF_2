import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
from sklearn.gaussian_process.kernels import Matern

# Create synthetic data
'''
rng = np.random.default_rng(42)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y += 0.2 * rng.normal(size=X.shape[0])
'''

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

DATA = np.load('tSNE_'+str(20)+'.npy')
points_0 = []
points_1 = []
for j in range(len(labels)):
	l = labels[j]
	points_0.append(DATA[l, 0])
	points_1.append(DATA[l, 1])
N = max(values)
min_val = min(values)
N -= min_val

X = np.empty((len(points_0), 2))
y = np.empty((len(points_0)))
for i in range(X.shape[0]):
	X[i, 0] = points_0[i]
	X[i, 1] = points_1[i]
	y[i] = values[i]

y = (y-np.min(y)) / (np.max(y)-np.min(y))

# Define the kernel (RBF kernel with a constant term)
kernel = C() * RBF()
nu = 2.5
kernel = Matern(length_scale=10, nu=nu)

# Create and fit the Gaussian Process Regressor
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X, y)

# Generate test data for predictions
x_test = DATA
#x_test = X

# Predict the mean and standard deviation of the function at test points
y_pred, sigma = gp.predict(x_test, return_std=True)
print(np.sum(abs(sigma/y_pred))/len(y_pred))
# save predicted DATA
np.save(str(nu)+'T_fit.npy', y_pred)

'''
# Plot the results
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

print(len(y))
print(len(sigma))
ax.scatter(X[:, 0], X[:, 1], y, c='k', label='Data')
ax.scatter(x_test[:, 0], x_test[:, 1], y_pred, c='r', label='Data')
#ax.plot(x_test, y_pred, 'b', label='Prediction')
#ax.fill_between(x_test[:, 0], y_pred - sigma, y_pred + sigma, alpha=0.2, color='blue')
#ax.xlabel('X')
#ax.ylabel('y')
#ax.legend()
#ax.title('Gaussian Process Regression')
plt.show()
'''