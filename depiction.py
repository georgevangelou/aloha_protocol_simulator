'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import ini
import statistics as stat

def gen_row_names(num_of_stations):
    row_names = []
    for i in range(num_of_stations):
        row_names.append('Station '+ str(i))
    return row_names

def gen_col_names():
    header = 'TIME ELAPSED = ' + str(ini.time_elapsed)
    col_names = [header, 'Probability', 'Throughput', 'Maximum Delay', 'Average Delay', 'Queue Size',
        'Packets Sent', 'Successive Collisions', 'Back-off Delay']
    return col_names

def pretty_print(column_titles, row_titles, data):
    line = ''
    for i in range(21*len(column_titles)): line += '~'
    print(line)
    header = ''
    for i in range(len(column_titles)):
        header += "{:^20} "
    print(header.format(*column_titles))
    print()
    for i in range(len(row_titles)):
        row = ""
        for j in range(len(column_titles)):
            row += "{:^20} "
        row_data = [row_titles[i]]
        row_data += data[i]
        print(row.format(*row_data))
    print(line)
    print('\n')

def preprocessing(nodes):
    data = []
    for node in nodes:
        data.append( [round(node.probability, 4), round(node.throughput, 4), node.maxdelay, round(node.avdelay, 4), 
                      node.queuesize, node.packetssent, node.collisions, node.backoffdelay] )
    return data

def show(nodes):
    data = preprocessing(nodes)
    row_titles = gen_row_names(len(nodes))
    column_titles = gen_col_names()
    pretty_print(column_titles, row_titles, data)
    return

def finalprint(nodes):
    brackets = ''
    for i in range(80): brackets += '='
    print()
    print(brackets)
    print(brackets)
    print('\nTOTAL STATISTICS: \n')
    print('Total Throughput is: {}'.format(round(stat.tot_throughput(nodes), 3)))
    spacers = ''
    for i in range(20): spacers += ' '
    column_names = [spacers, 'Slot Time', 'Absolute Time (ms)']
    row_names = ['Total time elapsed', 'Maximum packet delay', 'Average packet Delay']
    a = ini.time_elapsed
    b = stat.tot_max_delay(nodes)
    c = stat.tot_avg_delay(nodes)
    data = [[a, stat.to_abs(a)], [b, stat.to_abs(b)], [c, stat.to_abs(c)] ]
    pretty_print(column_names, row_names, data)
    print(brackets)
    print(brackets)
    print()