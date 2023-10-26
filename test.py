import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data for five vectors
num_samples = 100
vector1 = np.random.randn(num_samples)
vector2 = np.random.randn(num_samples)
vector3 = np.random.randn(num_samples)
vector4 = np.random.randn(num_samples)
vector5 = np.random.randn(num_samples)

# Create a dictionary to store the data
data = {
    'Vector 1': vector1,
    'Vector 2': vector2,
    'Vector 3': vector3,
    'Vector 4': vector4,
    'Vector 5': vector5
}

import pandas as pd

# Create a pair plot using Seaborn
sns.set(style="ticks")
sns.pairplot(pd.DataFrame(data))
plt.show()