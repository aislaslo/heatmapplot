import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

values = np.random.rand(50, 12)
sns.heatmap(values, cmap='plasma')
plt.show()
