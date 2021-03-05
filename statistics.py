'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import ini

#converting time slots to milliseconds
def to_abs(slots):
    a = slots*ini.time_slot*1000 
    return round(a, ini.approximation)

#calculating the total maximum packet delay
def tot_max_delay(nodes):
    max_delay = 0
    for node in nodes:
        if (node.totaldelays == []): continue
        max_node_delay = max(node.totaldelays)
        if max_node_delay > max_delay:
            max_delay = max_node_delay
    return max_delay

#calculating the total throughput of all nodes
def tot_throughput(nodes):
    throughput = 0
    for node in nodes:
        throughput += node.throughput
    return round(throughput, ini.approximation)

#calculating the total average packet delay
def tot_avg_delay(nodes):
    tot_avg_list = []
    acc = 0
    for node in nodes:
        for delay in node.totaldelays:
            tot_avg_list.append(delay)
            acc +=delay
    avg_delay = acc / len(tot_avg_list)
    return round(avg_delay, ini.approximation)



def init_time_vector():
    return []

def init_vectors(num_of_stations):
    y = []
    for i in range(num_of_stations):
        y.append([])
    return y

def update_time_vector(vector_time, step):
    if ini.time_elapsed % step == 0:
        vector_time.append(ini.time_elapsed)
    return vector_time

def update_vectors(nodes, vectors, vector_var, step):
    length = len(vectors)-1
    if ini.time_elapsed % step == 0:
        temp = 0
        if vector_var == 'throughput':
            for i in range(length):
                vectors[i].append(nodes[i].throughput)
                temp += nodes[i].throughput
        elif vector_var == 'max delay':
            for i in range(length):
                vectors[i].append(nodes[i].maxdelay)
                temp = max(temp, nodes[i].maxdelay)
        elif vector_var == 'avg delay':
            for i in range(length):
                vectors[i].append(nodes[i].avdelay)
                temp += nodes[i].avdelay
            temp = temp/len(vectors)
        elif vector_var == 'queue size':
            for i in range(length):
                vectors[i].append(nodes[i].queuesize)
                temp += nodes[i].queuesize
        else:
            raise ValueError('Unknown option')
        vectors[-1].append(temp)
    return vectors
