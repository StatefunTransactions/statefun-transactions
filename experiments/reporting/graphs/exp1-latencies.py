import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# plt.rc('axes', axisbelow=True)
plt.rcParams["figure.figsize"] = (9, 5)

exp1_file_list = [
    'exp1-latencies/original_3_100_uniform_0_read_100_update_0_transfer/all.csv',
    'exp1-latencies/original_3_100_uniform_100_read_0_update_0_transfer/all.csv',
    'exp1-latencies/original_3_5000_uniform_0_read_100_update_0_transfer/all.csv',
    'exp1-latencies/original_3_5000_uniform_100_read_0_update_0_transfer/all.csv',
    'exp1-latencies/sagas_3_100_uniform_0_read_100_update_0_transfer/all.csv',
    'exp1-latencies/sagas_3_100_uniform_100_read_0_update_0_transfer/all.csv',
    'exp1-latencies/sagas_3_5000_uniform_0_read_100_update_0_transfer/all.csv',
    'exp1-latencies/sagas_3_5000_uniform_100_read_0_update_0_transfer/all.csv',
]

exp1_file_list_lower_througphut = [
    'exp-1-latency-low-throughput/original_3_100_uniform_0_read_100_update_0_transfer/all.csv',
    'exp-1-latency-low-throughput/original_3_100_uniform_100_read_0_update_0_transfer/all.csv',
    'exp-1-latency-low-throughput/original_3_5000_uniform_100_read_0_update_0_transfer/all.csv',
    'exp-1-latency-low-throughput/original_3_5000_uniform_0_read_100_update_0_transfer/all.csv'
]

def read_latencies_as_list(file_path):
    with open(file_path) as f:
        latencies = []
        for line in f.readlines():
            splitted = line.split(',')
            latencies.append(int(splitted[2]) - int(splitted[1]))
    return np.array(latencies)

# for i in exp1_file_list:
#     print(np.percentile(read_latencies_as_list(i)))

print("Start reading!")
OS_100_29_WRITE = read_latencies_as_list(exp1_file_list[0])
OS_100_29_READ = read_latencies_as_list(exp1_file_list[1])
CF_100_22_WRITE = read_latencies_as_list(exp1_file_list[4])
CF_100_22_READ = read_latencies_as_list(exp1_file_list[5])
OS_100_22_WRITE = read_latencies_as_list(exp1_file_list_lower_througphut[0])
OS_100_22_READ = read_latencies_as_list(exp1_file_list_lower_througphut[1])

OS_5000_WRITE = read_latencies_as_list(exp1_file_list[2])
OS_5000_READ = read_latencies_as_list(exp1_file_list[3])
CF_5000_WRITE = read_latencies_as_list(exp1_file_list[6])
CF_5000_READ = read_latencies_as_list(exp1_file_list[7])
OS_5000_WRITE_LOW = read_latencies_as_list(exp1_file_list_lower_througphut[3])
OS_5000_READ_LOW = read_latencies_as_list(exp1_file_list_lower_througphut[2])
print("Finished reading!")

bar_width = 0.1
hatch_write = '///////'
color_one = 'cornflowerblue'
color_two = 'coral'
color_three = 'palevioletred'
color_four = 'mediumseagreen'
color_five = 'indianred'
color_six = 'mediumturquoise'

plt.grid(axis='y', which='major', color='#CCCCCC', linestyle='--')

plt.bar(0, np.percentile(OS_100_29_READ, 95), bar_width,
edgecolor=color_one,
color=color_one)

plt.bar(bar_width, np.percentile(OS_100_29_WRITE, 95), bar_width,
edgecolor=color_one,
fill=False,
hatch=hatch_write)

plt.bar(0.05 + 2*bar_width, np.percentile(CF_100_22_READ, 95), bar_width,
edgecolor=color_two,
color=color_two)

plt.bar(0.05 + 3*bar_width, np.percentile(CF_100_22_WRITE, 95), bar_width,
edgecolor=color_two,
fill=False,
hatch=hatch_write)

plt.bar(0.1 + 4*bar_width, np.percentile(OS_100_22_READ, 95), bar_width,
edgecolor=color_three,
color=color_three)

plt.bar(0.1 + 5*bar_width, np.percentile(OS_100_22_WRITE, 95), bar_width,
edgecolor=color_three,
fill=False,
hatch=hatch_write)

plt.bar(0.2 + 6*bar_width, np.percentile(OS_5000_READ, 95), bar_width,
edgecolor=color_four,
color=color_four)

plt.bar(0.2 + 7*bar_width, np.percentile(OS_5000_WRITE, 95), bar_width,
edgecolor=color_four,
fill=False,
hatch=hatch_write)

plt.bar(0.25 + 8*bar_width, np.percentile(CF_5000_READ, 95), bar_width,
edgecolor=color_five,
color=color_five)

plt.bar(0.25 + 9*bar_width, np.percentile(CF_5000_WRITE, 95), bar_width,
edgecolor=color_five,
fill=False,
hatch=hatch_write)

plt.bar(0.3 + 10*bar_width, np.percentile(OS_5000_READ_LOW, 95), bar_width,
edgecolor=color_six,
color=color_six)

plt.bar(0.3 + 11*bar_width, np.percentile(OS_5000_WRITE_LOW, 95), bar_width,
edgecolor=color_six,
fill=False,
hatch=hatch_write)

# plt.xticks(bar_width, 'OS@29K', fontsize=14)


# plt.xticks(bar_width, 'OS@29K', fontsize=14)

x = [' OS@29K ', ' CF@22K ', '\n100 keys', ' OS@22K ', ' OS@16K ', '\n5000 keys', ' CF@14K ',
 ' OS@14K ']

xpos = [
    bar_width, 
    0.05 + 3*bar_width, 0.05 + 3*bar_width, 
    0.1 + 5*bar_width, 
    0.2 + 7*bar_width,  0.25 + 9*bar_width, 
    0.25 + 9*bar_width, 0.3 + 11*bar_width
]
plt.xticks(xpos, x, fontsize=18)


plt.xlim(-0.05, 0.35 + 12*bar_width)
plt.axvline(0.15 + 6*bar_width, color='black', linestyle='--')

write_patch = patches.Patch(facecolor='white',hatch='///')
read_patch = patches.Patch(facecolor='black')

plt.ylabel('Latency (ms)', fontsize=18)
plt.yticks(fontsize=18)
plt.tick_params(axis='x', length=0)
plt.legend(fontsize=20)

ax = plt.gca()
ax.legend([read_patch, write_patch], ['read', 'write'], loc='upper right', fontsize=20)
ax.get_xticklabels()[2].set_weight("bold")
ax.get_xticklabels()[5].set_weight("bold")

ax.text(0.2 + 6.5*bar_width, 5 + np.percentile(OS_5000_READ, 95),
                '%d' % int(np.percentile(OS_5000_READ, 95)),
                ha='center', va='bottom', fontsize=18)
ax.text(0.2 + 7.5*bar_width, 5 + np.percentile(OS_5000_WRITE, 95),
                '%d' % int(np.percentile(OS_5000_WRITE, 95)),
                ha='center', va='bottom', fontsize=18)

ax.text(0.25 + 8.5*bar_width, 5 + np.percentile(CF_5000_READ, 95),
                '%d' % int(np.percentile(CF_5000_READ, 95)),
                ha='center', va='bottom', fontsize=18)
ax.text(0.25 + 9.5*bar_width, 5 + np.percentile(CF_5000_WRITE, 95),
                '%d' % int(np.percentile(CF_5000_WRITE, 95)),
                ha='center', va='bottom', fontsize=18)

ax.text(0.3 + 10.5*bar_width, 5 + np.percentile(OS_5000_READ_LOW, 95),
                '%d' % int(np.percentile(OS_5000_READ_LOW, 95)),
                ha='center', va='bottom', fontsize=18)
ax.text(0.3 + 11.5*bar_width, 5 + np.percentile(OS_5000_WRITE_LOW, 95),
                '%d' % int(np.percentile(OS_5000_WRITE_LOW, 95)),
                ha='center', va='bottom', fontsize=18)

# plt.figure(figsize=(3, 2))
plt.tight_layout()

plt.savefig('graphs/exp1-latencies-95.pdf')
plt.show()