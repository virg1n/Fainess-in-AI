from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

# Accuracy on default RAF-DB
x = [0, 1, 2, 3, 4, 5, 6, 7]
y1 = [0, 0.7742, 0.8039, 0.8061, 0.8143, 0.8032, 0.7852, 0.7879]
plt.figure(figsize=(12, 7))
plt.plot(x, y1, 'o-r', alpha=0.7, label="Validation accuracy", lw=5, mec='b', mew=2, ms=10)
plt.legend()
plt.grid(True)
plt.show()


x = [0, 1, 2, 3, 4, 5, 6, 7]
y1 = [0, 0.7478 , 0.7863, 0.8065, 0.8261, 0.8373, 0.8580, 0.8735]
plt.figure(figsize=(12, 7))
plt.plot(x, y1, 'o-r', alpha=0.7, label="train accuracy", lw=5, mec='b', mew=2, ms=10)
plt.legend()
plt.grid(True)