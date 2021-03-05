'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import ini
import random
import statistics as stat
from station import *
from depiction import show 

def continuation(nodes):
    for node in nodes: 
        if (node.queuesize > ini.max_queue_size):
            show(nodes)
            print('FATAL ERROR:')
            print("Station "+node.id+" surpassed the maximum queue size...")
            print('The current simulation will now terminate.\n')
            return False
    for node in nodes:
        if (node.packetssent < ini.min_station_packets_sent ) :
            return True
    show(nodes)
    return False

def refresh(nodes): 
    for node in nodes: node.update()
    return 

def update_all_vectors(throughput_vects, maxdelay_vects, averagedelay_vects, queuesize_vects, nodes):
    throughput_vects = stat.update_vectors(nodes=nodes, vectors=throughput_vects, vector_var='throughput', step=ini.plot_step)
    maxdelay_vects = stat.update_vectors(nodes=nodes, vectors=maxdelay_vects, vector_var='max delay', step=ini.plot_step)
    averagedelay_vects = stat.update_vectors(nodes=nodes, vectors=averagedelay_vects, vector_var='avg delay', step=ini.plot_step)
    queuesize_vects = stat.update_vectors(nodes=nodes, vectors=queuesize_vects, vector_var='queue size', step=ini.plot_step)
    return (throughput_vects, maxdelay_vects, averagedelay_vects, queuesize_vects)

def collisionhandler(senders):
    for node in senders:
        if (ini.max_backoff_collisions == -1) : node.collisions += 1  #if we do not bound the back-off delay
        elif ((node.collisions) < ini.max_backoff_collisions): node.collisions += 1 #if we bound the back-off delay 
        node.backoffdelay = random.randint(1, 2**node.collisions)
    return


def generate_nodes(number_of_stations):
    nodes = [Station(i) for i in range (number_of_stations) ]
    return nodes

