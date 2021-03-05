'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


''' NODES CONFIGURATION '''
number_of_stations = 10 #number of stations/nodes in the network
min_station_packets_sent = 1000 #minimum number of packets sent by each station to end the simulation
min_probability = 0.015 #minimum probability of packet generation in a station  {nominal values for 0.3 throughput:}
max_probability = 0.040 #minimum probability of packet generation in a station  {    [0.015 0.040]                 }
max_backoff_collisions = 10
max_queue_size = 100

''' CHANNEL CONFIGURATION '''
channel_bandwidth = 100000 #bps
bit_time = 1/channel_bandwidth #seconds
packet_length = 10 #bits per packet
time_slot = bit_time * packet_length #seconds

''' SIMULATION CONFIGURATION '''
plot_step = 100
show_step = 1000

''' PLOTTING CONSTANTS '''
x_label = 'Time Elapsed (slots)'
thr_y_label = 'Throughput'
black_width_ratio = 1.5
basic_colors = ['red', 'blue', 'green', '#FFBF00', 'magenta', 'cyan', '#3D0C02', '#54626F', '#4D1A7F', '#006A4E', '#C32148', '#004225', '#808000', '#4aff00', 'orange', '#aaffc3', 'navy', '#9ACD32']
plot_colors = basic_colors[0:number_of_stations]; plot_colors.append('black')
window_size_X = 900
window_size_Y = 450

''' PROGRAM CONSTANTS '''
time_elapsed = 0
approximation = 3

