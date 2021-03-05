'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import ini
import ui
import time
import plotters as plots 
import statistics as stat
import handlers as h
from depiction import show, finalprint, gen_row_names


print('=======================================')
print('---- ALOHA PROTOCOL SIMULATION ---')
print('  MADE BY EVANGELOU G. & ROUSSOS N.')
print('=======================================\n')

print("*All simulation options can be modified either by user prompt or by changing the 'ini.py' file.")
print("As required by the project's demands, this program simulates the ALOHA protocol in a network")
print("with 10 stations/nodes. The simulation terminates in case each of them has successfully transmitted")
print("1000 packets or if any queue size is exceeded. If any collisions arise, the colliding nodes execute")
print("the exponential back-off algorithm.\n\n")

while True:
    ui.get_input()
    ini.time_elapsed = 0
    t = stat.init_time_vector()
    nodes = h.generate_nodes(ini.number_of_stations)
    throughput_vects = stat.init_vectors(ini.number_of_stations+1)
    maxdelay_vects = stat.init_vectors(ini.number_of_stations+1)
    averagedelay_vects = stat.init_vectors(ini.number_of_stations+1)
    queuesize_vects = stat.init_vectors(ini.number_of_stations+1)

    while h.continuation(nodes):
        senders = []
        ini.time_elapsed += 1
        for node in nodes:
            if ( node.wantstosend() ):
                senders.append(node)
        status = len(senders) #shows how many nodes transmitted in the channel
        if status == 1: senders[0].successfulsend() #successful transmission
        elif status > 1: h.collisionhandler(senders) #collisions detected
        t = stat.update_time_vector(t, ini.plot_step)
        (throughput_vects, maxdelay_vects, averagedelay_vects, queuesize_vects) = h.update_all_vectors(throughput_vects, maxdelay_vects, averagedelay_vects, queuesize_vects, nodes)
        h.refresh(nodes)
        if (ini.time_elapsed % ini.show_step == 0): show(nodes)

    finalprint(nodes)
    plot_labels = gen_row_names(ini.number_of_stations); plot_labels.append('Total')
    throughput_plot = plots.plotMultipleFunctions(t, throughput_vects, colors=ini.plot_colors, labels=plot_labels, figTitle='Throughput Plot', plotTitle='Throughput Plot', xlabel=ini.x_label, ylabel='Throughput', indexX=0, indexY=0)
    maxd_plot = plots.plotMultipleFunctions(t, maxdelay_vects, colors=ini.plot_colors, labels=plot_labels, figTitle='Maximum Delay Plot', plotTitle='Maximum Delay Plot', xlabel=ini.x_label, ylabel='Maximum Delay', indexX=1, indexY=0)
    avgd_plot = plots.plotMultipleFunctions(t, averagedelay_vects, colors=ini.plot_colors, labels=plot_labels, figTitle='Average Delay Plot', plotTitle='Average Delay Plot', xlabel=ini.x_label, ylabel='Average Delay',indexX=0, indexY=1)
    queue_plot = plots.plotMultipleFunctions(t, queuesize_vects, colors=ini.plot_colors, labels=plot_labels, figTitle='Queue Size Plot', plotTitle='Queue Size Plot', xlabel=ini.x_label, ylabel='Queue Size', indexX=1, indexY=1)
    throughput_plot.show()

    time.sleep(1)
    if (ui.runprogram() == False): break


