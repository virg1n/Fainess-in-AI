from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

# Accuracy on default RAF-DB
correct = np.array([1-0.5714285714285714, 1-0.09995746490854955, 1-0.61965811965])
mistakes = np.array([0.5714285714285714, 0.09995746490854955, 0.61965811965])

width = 0.35
fig, ax = plt.subplots()

labels = ['Asian', 'Caucasian', 'African-American']
ax.bar(labels, correct, width, label='correct')
ax.bar(labels, mistakes, width, bottom=correct,
      label='mistakes')



ax.set_ylabel('Ratio')
ax.set_title('correct/mistakes')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='rafdb')

plt.show()