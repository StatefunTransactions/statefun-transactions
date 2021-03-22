from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.lines as lines

TXN_PROPORTIONS = np.array([0, 0.05, 0.1, 0.25, 0.5, 0.75, 1])

plt.rc('axes', axisbelow=True)
plt.rcParams["figure.figsize"] = (15, 5)
# plt.rcParams['text.usetex'] = True

### TPC 100
TPC_100_TOTAL = np.array([29, 3, 2, 1, 0.5, 0.25, 0.25])
TPC_100_TXN = TPC_100_TOTAL * TXN_PROPORTIONS
TPC_100_ALL = (TPC_100_TOTAL - TPC_100_TXN) + (TPC_100_TXN * 7)
TPC_100_REMOTE = (TPC_100_TOTAL - TPC_100_TXN) + (TPC_100_TXN * 3)

bar_width = 0.05
color_total = 'cornflowerblue'
color_txn = 'coral'
all_x_ticks = []
all_x_ticks_pos = []
bold_labels = []

index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02)
centre_indices = index + bar_width*0.5

plt.bar(index, TPC_100_TOTAL, bar_width,
edgecolor=color_total,
color=color_total)

plt.bar(index, TPC_100_TXN, bar_width, 
edgecolor=color_txn,
color=color_txn)

plt.plot(centre_indices, TPC_100_ALL, 's', color='black')
plt.plot(centre_indices, TPC_100_REMOTE, 'o', color='black')

all_x_ticks += TXN_PROPORTIONS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append('\n\n100 keys')
all_x_ticks_pos.append(centre_indices[3])
bold_labels.append(len(all_x_ticks) - 1)

### TPC 2000
TPC_2000_TOTAL = np.array([24, 12, 9, 4, 1.5, 1, 0.75])
TPC_2000_TXN = TPC_2000_TOTAL * TXN_PROPORTIONS
TPC_2000_ALL = (TPC_2000_TOTAL - TPC_2000_TXN) + (TPC_2000_TXN * 7)
TPC_2000_REMOTE = (TPC_2000_TOTAL - TPC_2000_TXN) + (TPC_2000_TXN * 3)

index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index, TPC_2000_TOTAL, bar_width,
edgecolor=color_total,
color=color_total)

plt.bar(index, TPC_2000_TXN, bar_width, 
edgecolor=color_txn,
color=color_txn)

plt.plot(centre_indices, TPC_2000_ALL, 's', color='black')
plt.plot(centre_indices, TPC_2000_REMOTE, 'o', color='black')

all_x_ticks += TXN_PROPORTIONS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append('\n\n2000 keys')
all_x_ticks_pos.append(centre_indices[3])
bold_labels.append(len(all_x_ticks) - 1)

### TPC 5000
TPC_5000_TOTAL = np.array([18, 14, 10, 5, 3, 2, 1.5])
TPC_5000_TXN = TPC_5000_TOTAL * TXN_PROPORTIONS
TPC_5000_ALL = (TPC_5000_TOTAL - TPC_5000_TXN) + (TPC_5000_TXN * 7)
TPC_5000_REMOTE = (TPC_5000_TOTAL - TPC_5000_TXN) + (TPC_5000_TXN * 3)

index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index, TPC_5000_TOTAL, bar_width,
edgecolor=color_total,
color=color_total)

plt.bar(index, TPC_5000_TXN, bar_width, 
edgecolor=color_txn,
color=color_txn)

plt.plot(centre_indices, TPC_5000_ALL, 's', color='black')
plt.plot(centre_indices, TPC_5000_REMOTE, 'o', color='black')

all_x_ticks += TXN_PROPORTIONS.tolist()
all_x_ticks_pos += centre_indices.tolist()

plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

all_x_ticks.append('\n\n5000 keys')
all_x_ticks_pos.append(centre_indices[3])
bold_labels.append(len(all_x_ticks) - 1)

### TPC 10000
TPC_10000_TOTAL = np.array([18, 14, 10, 5, 3, 2, 1.5])
TPC_10000_TXN = TPC_10000_TOTAL * TXN_PROPORTIONS
TPC_10000_ALL = (TPC_10000_TOTAL - TPC_10000_TXN) + (TPC_10000_TXN * 7)
TPC_10000_REMOTE = (TPC_10000_TOTAL - TPC_10000_TXN) + (TPC_10000_TXN * 3)

index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
centre_indices = index + bar_width*0.5

plt.bar(index, TPC_10000_TOTAL, bar_width,
edgecolor=color_total,
color=color_total)

plt.bar(index, TPC_10000_TXN, bar_width, 
edgecolor=color_txn,
color=color_txn)

plt.plot(centre_indices, TPC_10000_ALL, 's', color='black')
plt.plot(centre_indices, TPC_10000_REMOTE, 'o', color='black')

all_x_ticks += TXN_PROPORTIONS.tolist()
all_x_ticks_pos += centre_indices.tolist()

all_x_ticks.append('\n\n10000 keys')
all_x_ticks_pos.append(centre_indices[3])
bold_labels.append(len(all_x_ticks) - 1)

# GENERAL

plt.xlim(-0.5*bar_width, index[-1] + 1.5*bar_width)
plt.xticks(all_x_ticks_pos, all_x_ticks, fontsize=14, rotation='vertical')
# plt.xticks(all )
plt.ylabel('Maximum throughput (1000 requests/s)', fontsize=14)
plt.xlabel(r'Proportion of $\tt{transfer}$ operations in the workload', fontsize=14)
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


total_ops = patches.Patch(facecolor=color_total, edgecolor=color_total)
txn_ops = patches.Patch(facecolor=color_txn, edgecolor=color_txn)
total_remote = lines.Line2D([0], [0], color='black', marker='o', linestyle='None',
                          markersize=8)
total = lines.Line2D([0], [0], color='black', marker='s', linestyle='None',
                          markersize=8)

ax.legend([total_ops, txn_ops, total, total_remote], 
['Total operations', r'$\tt{transfer}$ operations', 'Total function invocations (lower bound)', 'Total remote invocations'],
loc='upper right', fontsize='12', numpoints=1)

plt.tight_layout()
plt.savefig('graphs/exp2-throughput-tpc.pdf')
plt.show()