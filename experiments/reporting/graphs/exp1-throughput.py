from matplotlib import pyplot as plt
import numpy as np

plt.rc('axes', axisbelow=True)

original = [36, 24, 20, 20]
new = [29, 20, 18, 18]
x = ['100', '2000', '5000', '10000']

color_original = 'cornflowerblue'
color_new = 'coral'

# create plot
fig, ax = plt.subplots()
index = np.arange(len(x)) * 0.6
bar_width = 0.10
opacity = 1

rects1 = plt.bar(index, original, bar_width,
alpha=opacity,
color=color_original,
edgecolor=color_original,
label='Original StateFun - read only')

rects2 = plt.bar(index + bar_width, original, bar_width,
alpha=opacity,
edgecolor=color_original,
fill = False,
hatch = '///////',
label='Original StateFun - write only')

rects3 = plt.bar(index + 2 * bar_width, new, bar_width,
alpha=opacity,
edgecolor=color_new,
color=color_new,
label='Coordinator Functions - read only')

rects4 = plt.bar(index + 3 * bar_width, new, bar_width,
alpha=opacity,
edgecolor=color_new,
fill = False,
hatch = '///////',
label='Coordinator Functions - write only')

plt.xlabel('Keys (#)', fontsize=18)
plt.ylabel('Maximum throughput\n(1000 requests/s)', fontsize=18)
plt.xlim(index[0] - 0.1, index[len(index) - 1] + 0.5)
plt.xticks(index + 2 * bar_width, x, fontsize=18)
plt.yticks(fontsize=18)
plt.grid(axis='y', which='major', color='#CCCCCC', linestyle='--')
plt.tick_params(axis='x', length=0)
plt.legend(fontsize=16)

plt.tight_layout()
plt.savefig('graphs/exp1-throughput.pdf')
plt.show()