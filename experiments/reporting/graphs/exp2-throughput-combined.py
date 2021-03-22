from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as patches
import matplotlib.lines as lines

# TXN_PROPORTIONS = np.array([0, 0.05, 0.1, 0.25, 0.5, 0.75, 1])

# # plt.rc('axes', axisbelow=True)
# # plt.rcParams["figure.figsize"] = (15, 5)
# # plt.rcParams['text.usetex'] = True

# ### SAGAS 100
# SAGAS_100_TOTAL = np.array([18, 14, 11, 7.5, 4, 3, 2.25])
# SAGAS_100_TXN = SAGAS_100_TOTAL * TXN_PROPORTIONS
# SAGAS_100_ALL = (SAGAS_100_TOTAL - SAGAS_100_TXN) + (SAGAS_100_TXN * 5)
# SAGAS_100_REMOTE = (SAGAS_100_TOTAL - SAGAS_100_TXN) + (SAGAS_100_TXN * 3)

# bar_width = 0.1
color_total = 'cornflowerblue'
color_txn = 'coral'
hatch_tpc = '///////'
# all_x_ticks = []
# all_x_ticks_pos = []
# bold_labels = []

# index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02)
# centre_indices = index + bar_width*0.5

# TPC_100_TOTAL = np.array([18, 14, 10, 5, 3, 2, 1.5])
# TPC_100_TXN = TPC_100_TOTAL * TXN_PROPORTIONS
# TPC_100_ALL = (TPC_100_TOTAL - TPC_100_TXN) + (TPC_100_TXN * 7)
# TPC_100_REMOTE = (TPC_100_TOTAL - TPC_100_TXN) + (TPC_100_TXN * 3)
# plt.bar(index + 0.5*bar_width, TPC_100_TOTAL, bar_width / 2,
# edgecolor=color_total,
# fill=False,
# hatch=hatch_tpc)

# plt.bar(index + 0.5*bar_width, TPC_100_TXN, bar_width / 2, 
# edgecolor=color_txn,
# fill=False,
# hatch=hatch_tpc)

# plt.plot(centre_indices + 0.25*bar_width, TPC_100_ALL, 'x', color='black', markersize=6)
# plt.plot(centre_indices + 0.25*bar_width, TPC_100_REMOTE, '+', color='black', markersize=6)

# plt.bar(index, SAGAS_100_TOTAL, bar_width / 2,
# edgecolor=color_total,
# color=color_total)

# plt.bar(index, SAGAS_100_TXN, bar_width / 2, 
# edgecolor=color_txn,
# color=color_txn)

# plt.plot(centre_indices - 0.25*bar_width, SAGAS_100_ALL, 'x', color='black', markersize=6)
# plt.plot(centre_indices - 0.25*bar_width, SAGAS_100_REMOTE, '+', color='black', markersize=6)

# all_x_ticks += TXN_PROPORTIONS.tolist()
# all_x_ticks_pos += centre_indices.tolist()

# plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

# # all_x_ticks.append('\n\n100 keys')
# # all_x_ticks_pos.append(centre_indices[3])
# bold_labels.append(len(all_x_ticks) - 1)

# # ### SAGAS 2000
# # SAGAS_2000_TOTAL = np.array([24, 16, 12, 7.5, 4, 3, 2.25])
# # SAGAS_2000_TXN = SAGAS_2000_TOTAL * TXN_PROPORTIONS
# # SAGAS_2000_ALL = (SAGAS_2000_TOTAL - SAGAS_2000_TXN) + (SAGAS_2000_TXN * 5)
# # SAGAS_2000_REMOTE = (SAGAS_2000_TOTAL - SAGAS_2000_TXN) + (SAGAS_2000_TXN * 3)

# # index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
# # centre_indices = index + bar_width*0.5

# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_2000_ALL, 'x', color='black', markersize=5)
# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_2000_REMOTE, '+', color='black', markersize=5)

# # TPC_2000_TOTAL = np.array([24, 12, 9, 4, 1.5, 1, 0.75])
# # TPC_2000_TXN = TPC_2000_TOTAL * TXN_PROPORTIONS
# # TPC_2000_ALL = (TPC_2000_TOTAL - TPC_2000_TXN) + (TPC_2000_TXN * 7)
# # TPC_2000_REMOTE = (TPC_2000_TOTAL - TPC_2000_TXN) + (TPC_2000_TXN * 3)

# # plt.bar(index + bar_width / 2, TPC_2000_TOTAL, bar_width / 2,
# # edgecolor=color_total,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.bar(index + bar_width / 2, TPC_2000_TXN, bar_width / 2, 
# # edgecolor=color_txn,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.bar(index, SAGAS_2000_TOTAL, bar_width / 2,
# # edgecolor=color_total,
# # color=color_total)

# # plt.bar(index, SAGAS_2000_TXN, bar_width / 2, 
# # edgecolor=color_txn,
# # color=color_txn)

# # plt.plot(centre_indices + bar_width*0.25, TPC_2000_ALL, 'x', color='black', markersize=5)
# # plt.plot(centre_indices + bar_width*0.25, TPC_2000_REMOTE, '+', color='black', markersize=5)

# # all_x_ticks += TXN_PROPORTIONS.tolist()
# # all_x_ticks_pos += centre_indices.tolist()

# # plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

# # all_x_ticks.append('\n\n2000 keys')
# # all_x_ticks_pos.append(centre_indices[3])
# # bold_labels.append(len(all_x_ticks) - 1)

# # ### SAGAS 5000
# # SAGAS_5000_TOTAL = np.array([18, 14, 11, 7.5, 4, 3, 2.25])
# # SAGAS_5000_TXN = SAGAS_5000_TOTAL * TXN_PROPORTIONS
# # SAGAS_5000_ALL = (SAGAS_5000_TOTAL - SAGAS_5000_TXN) + (SAGAS_5000_TXN * 5)
# # SAGAS_5000_REMOTE = (SAGAS_5000_TOTAL - SAGAS_5000_TXN) + (SAGAS_5000_TXN * 3)

# # index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
# # centre_indices = index + bar_width*0.5

# # TPC_5000_TOTAL = np.array([18, 14, 10, 5, 3, 2, 1.5])
# # TPC_5000_TXN = TPC_5000_TOTAL * TXN_PROPORTIONS
# # TPC_5000_ALL = (TPC_5000_TOTAL - TPC_5000_TXN) + (TPC_5000_TXN * 7)
# # TPC_5000_REMOTE = (TPC_5000_TOTAL - TPC_5000_TXN) + (TPC_5000_TXN * 3)

# # plt.bar(index + 0.5*bar_width, TPC_5000_TOTAL, bar_width/2,
# # edgecolor=color_total,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.bar(index + 0.5*bar_width, TPC_5000_TXN, bar_width/2, 
# # edgecolor=color_txn,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.plot(centre_indices + 0.25*bar_width, TPC_5000_ALL, 'x', color='black')
# # plt.plot(centre_indices + 0.25*bar_width, TPC_5000_REMOTE, '+', color='black')


# # plt.bar(index, SAGAS_5000_TOTAL, bar_width / 2,
# # edgecolor=color_total,
# # color=color_total)

# # plt.bar(index, SAGAS_5000_TXN, bar_width / 2, 
# # edgecolor=color_txn,
# # color=color_txn)

# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_5000_ALL, 'x', color='black', markersize=5)
# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_5000_REMOTE, '+', color='black', markersize=5)

# # all_x_ticks += TXN_PROPORTIONS.tolist()
# # all_x_ticks_pos += centre_indices.tolist()

# # plt.axvline(all_x_ticks_pos[-1] + 1.5*bar_width, color='black', linestyle='--')

# # all_x_ticks.append('\n\n5000 keys')
# # all_x_ticks_pos.append(centre_indices[3])
# # bold_labels.append(len(all_x_ticks) - 1)

# # ### SAGAS 10000
# # SAGAS_10000_TOTAL = np.array([18, 14, 11, 7.5, 4, 3, 2.25])
# # SAGAS_10000_TXN = SAGAS_10000_TOTAL * TXN_PROPORTIONS
# # SAGAS_10000_ALL = (SAGAS_10000_TOTAL - SAGAS_10000_TXN) + (SAGAS_10000_TXN * 5)
# # SAGAS_10000_REMOTE = (SAGAS_10000_TOTAL - SAGAS_10000_TXN) + (SAGAS_10000_TXN * 3)

# # index = (np.arange(len(TXN_PROPORTIONS))) * (bar_width + 0.02) + index[-1] + 3 * bar_width
# # centre_indices = index + bar_width*0.5

# # TPC_10000_TOTAL = np.array([18, 14, 10, 5, 3, 2, 1.5])
# # TPC_10000_TXN = TPC_10000_TOTAL * TXN_PROPORTIONS
# # TPC_10000_ALL = (TPC_10000_TOTAL - TPC_10000_TXN) + (TPC_10000_TXN * 7)
# # TPC_10000_REMOTE = (TPC_10000_TOTAL - TPC_10000_TXN) + (TPC_10000_TXN * 3)

# # plt.bar(index + 0.5*bar_width, TPC_10000_TOTAL, bar_width / 2,
# # edgecolor=color_total,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.bar(index + 0.5*bar_width, TPC_10000_TXN, bar_width / 2, 
# # edgecolor=color_txn,
# # fill=False,
# # hatch=hatch_tpc)

# # plt.plot(centre_indices + 0.25*bar_width, TPC_10000_ALL, 'x', color='black')
# # plt.plot(centre_indices + 0.25*bar_width, TPC_10000_REMOTE, '+', color='black')


# # plt.bar(index, SAGAS_10000_TOTAL, bar_width / 2,
# # edgecolor=color_total,
# # color=color_total)

# # plt.bar(index, SAGAS_10000_TXN, bar_width / 2, 
# # edgecolor=color_txn,
# # color=color_txn)

# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_10000_ALL, 'x', color='black', markersize=5)
# # plt.plot(centre_indices - 0.25*bar_width, SAGAS_10000_REMOTE, '+', color='black', markersize=5)

# # all_x_ticks += TXN_PROPORTIONS.tolist()
# # all_x_ticks_pos += centre_indices.tolist()

# # all_x_ticks.append('\n\n10000 keys')
# # all_x_ticks_pos.append(centre_indices[3])
# # bold_labels.append(len(all_x_ticks) - 1)

# # GENERAL

# plt.xlim(-0.5*bar_width, index[-1] + 1.5*bar_width)
# plt.xticks(all_x_ticks_pos, all_x_ticks, fontsize=18, rotation='vertical')
# # plt.xticks(all )
# plt.ylabel('Maximum throughput\n(1000 requests/s)', fontsize=18)
# plt.xlabel(r'Proportion of $\tt{transfer}$ operations in the workload', fontsize=18)
figlegend = plt.figure(figsize=(9.5,1))
# ax = fig.add_subplot(111)
# plt.xticks(fontsize=16)
# for l in bold_labels:
#     # ax.get_xticklabels()[l].set_weight("bold")
#     ax.get_xticklabels()[l].set_style("italic")
#     ax.get_xticklabels()[l].set_rotation('horizontal')
#     ax.get_xticklabels()[l].set_fontsize('18')
# plt.yticks(fontsize=16)
# plt.tick_params(axis='x', length=0)

# plt.grid(axis='y', which='major', color='#CCCCCC', linestyle='--')


total_ops = patches.Patch(facecolor=color_total, edgecolor=color_total)
txn_ops = patches.Patch(facecolor=color_txn, edgecolor=color_txn)
total_remote = lines.Line2D([0], [0], color='black', marker='+', linestyle='None',
                          markersize=6)
total = lines.Line2D([0], [0], color='black', marker='x', linestyle='None',
                          markersize=6)
two_phase_patch = patches.Patch(facecolor='white',hatch='///')
sagas_patch = patches.Patch(facecolor='black')

figlegend.legend([total_ops, txn_ops, total, total_remote, sagas_patch, two_phase_patch], 
['Total operations', r'$\tt{transfer}$ operations', 'Total function invocations',
'Total remote invocations', 'Sagas', 'Two-phase commit'],
loc='center', fontsize='15', numpoints=1, ncol=3)

# plt.tight_layout()
plt.savefig('graphs/exp2-throughput-legend.pdf')
plt.show()