#%% import packages
import numpy as np
import matplotlib.pyplot as plt

#%% initialize the maze
# figure size and figure variable
fig = plt.figure(figsize=(5,5))
ax = plt.gca()

# draw the red wall
plt.plot([1,1],[0,1],color='red',linewidth=2)
plt.plot([1,2],[2,2],color='red',linewidth=2)
plt.plot([2,2],[2,1],color='red',linewidth=2)
plt.plot([2,3],[1,1],color='red',linewidth=2)

# draw the states S0~S8
plt.text(0.5,2.5,'S0',size=14,ha='center')
