# https://github.com/derekbanas/matplotlib/blob/master/MPL%20Tut.ipynb

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x_1 = np.linspace(0,5,10)
y_1 = x_1 **2
plt.plot(x_1,y_1)
plt.title('Days Ssquared Chart')
plt.xlabel('Days')
plt.ylabel('Days Squered')
plt.show()  # Outside of jupyter notebooks

