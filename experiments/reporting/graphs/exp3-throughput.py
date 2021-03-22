from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.lines as lines

WORKERS = np.array([1, 3, 5, 7])

SAGAS_01_TOTAL = np.array([4.6, 11, 12, 12.5])
SAGAS_05_TOTAL = np.array([1.8, 4, 4.5, 4.5])
SAGAS_1_TOTAL = np.array([1.1, 2.25, 2.5, 2.5])

TPC_01_TOTAL = np.array([4.5, 10, 10.5, 10.5])
TPC_05_TOTAL = np.array([1.5, 3, 3.4, 3.4])
TPC_1_TOTAL = np.array([0.7, 1.5, 1.7, 1.6])

plt.rc('axes', axisbelow=True)
plt.rcParams["figure.figsize"] = (15, 5)

### SAGAS 01
bar_width = 0.05
color_sagas = 'cornflowerblue'
color_tpc = 'coral'

all_x_ticks = []
all_x_ticks_pos = []
bold_labels = []

index = (np.arange(len(WORKERS))) * (bar_width + 0.02)
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, SAGAS_01_TOTAL, bar_width,
edgecolor=color_sagas,
color=color_sagas)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'0.1 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

### SAGAS 05
index = (np.arange(len(WORKERS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, SAGAS_05_TOTAL, bar_width,
edgecolor=color_sagas,
color=color_sagas)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'0.5 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

### SAGAS 1
index = (np.arange(len(WORKERS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, SAGAS_1_TOTAL, bar_width,
edgecolor=color_sagas,
color=color_sagas)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'1.0 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

### TPC 01
index = (np.arange(len(WORKERS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, TPC_01_TOTAL, bar_width,
edgecolor=color_tpc,
color=color_tpc)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'0.1 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

### TPC 05
index = (np.arange(len(WORKERS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, TPC_05_TOTAL, bar_width,
edgecolor=color_tpc,
color=color_tpc)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'0.5 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

### TPC 1
index = (np.arange(len(WORKERS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index + 0.5*bar_width, TPC_1_TOTAL, bar_width,
edgecolor=color_tpc,
color=color_tpc)

all_x_ticks += WORKERS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append("\n" r'1.0 $\tt{transfer}$ ops')
all_x_ticks_pos.append((centre_indices[1] + centre_indices[2])/2)
bold_labels.append(len(all_x_ticks) - 1)

# GENERAL

plt.xlim(-bar_width, index[-1] + 2*bar_width)
plt.xticks(all_x_ticks_pos, all_x_ticks, fontsize=14)#, rotation='vertical')
# plt.xticks(all )
plt.ylabel('Maximum throughput (1000 requests/s)', fontsize=14)
plt.xlabel("Number of StateFun workers", fontsize=14)
ax = plt.gca()
plt.xticks(fontsize=12)
for l in bold_labels:
    # ax.get_xticklabels()[l].set_weight("bold")
    ax.get_xticklabels()[l].set_style("italic")
    ax.get_xticklabels()[l].set_rotation('horizontal')
    ax.get_xticklabels()[l].set_fontsize('14')
plt.yticks(fontsize=12)
plt.tick_params(axis='x', length=0)

plt.grid(axis='y', which='major', color='#CCCCCC', linestyle='--')


sagas_patch = patches.Patch(facecolor=color_sagas, edgecolor=color_sagas)
tpc_patch = patches.Patch(facecolor=color_tpc, edgecolor=color_tpc)

ax.legend([sagas_patch, tpc_patch], 
['Sagas', 'Tpc'],
loc='upper right', fontsize='12', numpoints=1)

plt.tight_layout()
plt.savefig('graphs/exp3-throughput.pdf')
plt.show()