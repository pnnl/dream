print ("""
========================plot_best_campaign_ttds.py========================
Plots DREAM TTD spread per scenario for each campaign

Programmed by K. Mansoor - Mar 2016
Updated by J. Whiting - Dec 2019
========================================================================
""")

# python plot_dreamout01.py objective_summary_best.csv


import sys, re, os, csv
import numpy as np
import time
import matplotlib.pyplot as plt

t0=float(time.process_time())

# Make sure that we have the correct number of arguments, otherwise abort
if (len(sys.argv) != 2):
	print('Usage : plot_best_campaign_ttds.py <csv file>\n')
	exit()

# Arguments
csvfile=sys.argv[1]
#csvfile='C:\\Users\\whit162\\OneDrive - PNNL\\Documents\\Projects\\DreamProject\\Results_20191203160351\\best_campaign_ttds.csv'

if not re.search('.csv$',csvfile.lower()):
	print('\nError - input file must be a *.csv file\n')
	exit()

# Determine the directory where we save results
new_folder = os.path.join(os.path.dirname(csvfile) + '/best_campaign_ttd_plots')
print(new_folder)
if not os.path.isdir(new_folder): os.mkdir(new_folder)
else: print('already exists')

filepre=re.sub('.csv$','',csvfile)
fignamepdf='%s.pdf'%filepre

## Get the data ##
names = []
ttds = set()
list_of_counts = []
with open(csvfile) as f:
    reader = csv.reader(f)
    for row in reader:
        if 'Time to Detection' in row[0]: #Header
            unit = row[0][row[0].find("(")+1:row[0].find(")")]
        else: #Information for a campaign
            names.append(row[0]) #Creates a list of campaign names
            count = {} #Stores the scenario count per ttd (not cumulative)
            for entry in row[1:]:
                if entry =='': continue
                value = float(entry)
                ttds.add(value)
                if value not in count:
                    count[value] = 0
                count[value] += 1
            list_of_counts.append(count)

ttds = sorted(ttds)
to_plot_list = []
for count in list_of_counts:
    counts = []
    cumulative = 0 #stores detections at earlier ttds
    for ttd in ttds:
        if ttd in count:
            counts.append(count[ttd] + cumulative)
            cumulative += count[ttd]
        else:
            counts.append(cumulative)
    to_plot_list.append(counts)

## Plot the data ##
i = 0
for x in to_plot_list:
    print ("Plotting Campaign_%d"%(i+1))
    
    N = len(ttds)
    if N>10: #Too many values won't plot, need to take intervals
        interval = round(N/10)
        x = x[round(interval/2)-1::interval]
        labels = ttds[round(interval/2)-1::interval]
        ind = np.arange(N/interval) + 1  # the x locations for the groups
    else:
        labels = ttds
        ind = np.arange(N) + 1  # the x locations for the groups
    
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, x, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Number of Scenarios')
    ax.set_xlabel('Time to Detection (%s)'%(unit))
    ax.set_title('Campaign_%d - Number of Scenarios Detected by TTD'%(i+1))
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 0.90*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.savefig(new_folder + '/' + names[i] + '.pdf')
    plt.close()
    i += 1

t1=float(time.process_time())
print('\n  Done!! [%3ds] open %s\n\n\n' % (t1-t0,fignamepdf))