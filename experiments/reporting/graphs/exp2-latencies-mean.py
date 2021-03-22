import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

# Transfer vs. regular --> pattern
# Color --> tpc vs sagas
# Transaction proportion --> first x-axis
# Keys --> second x-axis

exp2_sagas_list = [
    'sagas-exp2-latency/sagas_3_100_uniform_0_read_0_update_100_transfer/all.csv',
    'sagas-exp2-latency/sagas_3_100_uniform_25_read_25_update_50_transfer/all.csv',
    'sagas-exp2-latency/sagas_3_100_uniform_45_read_45_update_10_transfer/all.csv',
    'sagas-exp2-latency/sagas_3_5000_uniform_0_read_0_update_100_transfer/all.csv',
    'sagas-exp2-latency/sagas_3_5000_uniform_25_read_25_update_50_transfer/all.csv',
    'sagas-exp2-latency/sagas_3_5000_uniform_45_read_45_update_10_transfer/all.csv'
]

exp2_tpc_list = [
    'tpc-exp2-latency/tpc_3_100_uniform_0_read_0_update_100_transfer/all.csv',
    'tpc-exp2-latency/tpc_3_100_uniform_25_read_25_update_50_transfer/all.csv',
    'tpc-exp2-latency/tpc_3_100_uniform_45_read_45_update_10_transfer/all.csv',
    'tpc-exp2-latency/tpc_3_5000_uniform_0_read_0_update_100_transfer/all.csv',
    'tpc-exp2-latency/tpc_3_5000_uniform_25_read_25_update_50_transfer/all.csv',
    'tpc-exp2-latency/tpc_3_5000_uniform_45_read_45_update_10_transfer/all.csv'
]

def read_seperate_latencies_as_list(file_path):
    with open(file_path) as f:
        regular_latencies = []
        transfer_latencies = []
        for line in f.readlines():
            splitted = line.split(',')
            if splitted[0] == 'transfer':
                transfer_latencies.append(int(splitted[2]) - int(splitted[1]))
            else:
                regular_latencies.append(int(splitted[2]) - int(splitted[1]))
    if len(regular_latencies) == 0:
        regular_latencies = [0]
    return np.array(transfer_latencies), np.array(regular_latencies)


print("Start reading!")
TPC_TRANSFER_100_100, TPC_REGULAR_100_100 = read_seperate_latencies_as_list(exp2_tpc_list[0])
TPC_TRANSFER_100_50, TPC_REGULAR_100_50 = read_seperate_latencies_as_list(exp2_tpc_list[1])
TPC_TRANSFER_100_10, TPC_REGULAR_100_10 = read_seperate_latencies_as_list(exp2_tpc_list[2])
TPC_TRANSFER_5000_100, TPC_REGULAR_5000_100 = read_seperate_latencies_as_list(exp2_tpc_list[3])
TPC_TRANSFER_5000_50, TPC_REGULAR_5000_50 = read_seperate_latencies_as_list(exp2_tpc_list[4])
TPC_TRANSFER_5000_10, TPC_REGULAR_5000_10 = read_seperate_latencies_as_list(exp2_tpc_list[5])

SAGAS_TRANSFER_100_100, SAGAS_REGULAR_100_100 = read_seperate_latencies_as_list(exp2_sagas_list[0])
SAGAS_TRANSFER_100_50, SAGAS_REGULAR_100_50 = read_seperate_latencies_as_list(exp2_sagas_list[1])
SAGAS_TRANSFER_100_10, SAGAS_REGULAR_100_10 = read_seperate_latencies_as_list(exp2_sagas_list[2])
SAGAS_TRANSFER_5000_100, SAGAS_REGULAR_5000_100 = read_seperate_latencies_as_list(exp2_sagas_list[3])
SAGAS_TRANSFER_5000_50, SAGAS_REGULAR_5000_50 = read_seperate_latencies_as_list(exp2_sagas_list[4])
SAGAS_TRANSFER_5000_10, SAGAS_REGULAR_5000_10 = read_seperate_latencies_as_list(exp2_sagas_list[5])
print("Finished reading!")

bar_width = 0.1
hatch_transfer = '///////'
color_sagas = 'mediumseagreen'
color_tpc = 'indianred'

plt.grid(axis='y', which='major', color='#CCCCCC', linestyle='--')

### 100 keys 0.1
plt.bar(0, np.mean(SAGAS_REGULAR_100_10), bar_width,
edgecolor=color_sagas,
color=color_sagas)

plt.bar(bar_width, np.mean(SAGAS_TRANSFER_100_10), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(2*bar_width, np.mean(TPC_REGULAR_100_10), bar_width,
edgecolor=color_tpc,
color=color_tpc)

plt.bar(3*bar_width, np.mean(TPC_TRANSFER_100_10), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

### 100 keys 0.5
plt.bar(4.5*bar_width, np.mean(SAGAS_REGULAR_100_50), bar_width,
edgecolor=color_sagas,
color=color_sagas)

plt.bar(5.5*bar_width, np.mean(SAGAS_TRANSFER_100_50), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(6.5*bar_width, np.mean(TPC_REGULAR_100_50), bar_width,
edgecolor=color_tpc,
color=color_tpc)

plt.bar(7.5*bar_width, np.mean(TPC_TRANSFER_100_50), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

### 100 keys 1
plt.bar(9*bar_width, np.mean(SAGAS_TRANSFER_100_100), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(10*bar_width, np.mean(TPC_TRANSFER_100_100), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

plt.axvline(12*bar_width, color='black', linestyle='--')

### 5000 keys 0.1
plt.bar(13*bar_width, np.mean(SAGAS_REGULAR_5000_10), bar_width,
edgecolor=color_sagas,
color=color_sagas)

plt.bar(14*bar_width, np.mean(SAGAS_TRANSFER_5000_10), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(15*bar_width, np.mean(TPC_REGULAR_5000_10), bar_width,
edgecolor=color_tpc,
color=color_tpc)

plt.bar(16*bar_width, np.mean(TPC_TRANSFER_5000_10), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

### 5000 keys 0.5
plt.bar(17.5*bar_width, np.mean(SAGAS_REGULAR_5000_50), bar_width,
edgecolor=color_sagas,
color=color_sagas)

plt.bar(18.5*bar_width, np.mean(SAGAS_TRANSFER_5000_50), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(19.5*bar_width, np.mean(TPC_REGULAR_5000_50), bar_width,
edgecolor=color_tpc,
color=color_tpc)

plt.bar(20.5*bar_width, np.mean(TPC_TRANSFER_5000_50), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

### 5000 keys 1
plt.bar(22*bar_width, np.mean(SAGAS_TRANSFER_5000_100), bar_width,
edgecolor=color_sagas,
fill=False,
hatch=hatch_transfer)

plt.bar(23*bar_width, np.mean(TPC_TRANSFER_5000_100), bar_width,
edgecolor=color_tpc,
fill=False,
hatch=hatch_transfer)

ax = plt.gca()

# ax2 = ax.twinx()

dot_pos = [1, 3, 5.5, 7.5, 9.5, 10.5, 14, 16, 18.5, 20.5, 22.5, 23.5]
dot_vals = [11, 3, 2, 1.5, 0.4, 0.16, 9, 3, 2, 8, 2, 1.2] 
# for i in range(len(dot_pos)):
#     ax2.plot(dot_pos[i]*bar_width, dot_vals[i], 'o', color='black')

x_labels = ['0.1', '0.5', '1.0', '0.1', '0.5', '1.0']
x_pos = [2*bar_width, 6.5*bar_width, 10*bar_width, 15*bar_width, 19.5*bar_width, 23*bar_width]
x_labels.extend(['\n100 keys', '\n5000 keys'])
x_pos.extend([5.5*bar_width, 17.5*bar_width])


ax.set_ylabel('Latency (ms)', fontsize=22)
# ax2.set_ylabel('Throughput (1000 requests/s)', fontsize=14)

plt.yticks(fontsize=22)
ax.tick_params(axis='x', length=0)
# ax2.tick_params(axis='x', length=0)
ax.set_xlabel(r'Proportion of $\tt{transfer}$ operations in the workload', fontsize=22)
plt.legend(fontsize=22)

plt.xticks(x_pos, x_labels, fontsize=22)

ax.get_xticklabels()[6].set_style('italic')
ax.get_xticklabels()[7].set_style("italic")

sagas_patch = patches.Patch(facecolor=color_sagas, edgecolor=color_sagas)
tpc_patch = patches.Patch(facecolor=color_tpc, edgecolor=color_tpc)
transfer_patch = patches.Patch(facecolor='white',hatch='///')
regular_patch = patches.Patch(facecolor='black')

througphut_dot = lines.Line2D([0], [0], color='black', marker='o', linestyle='None',
                          markersize=8)

# ax.legend([sagas_patch, tpc_patch, transfer_patch, regular_patch], 
# ['Sagas', 'Two-phase commit', r'$\tt{transfer}$ operations', 'Regular operations'],
# loc='upper right', fontsize='20', numpoints=1)

plt.tight_layout()
plt.savefig('graphs/exp2-latencies-mean.pdf')
plt.show()