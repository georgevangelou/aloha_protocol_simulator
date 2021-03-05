'''
ALOHA PROTOCOL SIMULATION

authors: George Evangelou, Nikos Roussos
date: July 2019
'''


import random
import ini

class Station:
    """This class determines the elements and actions of a station in the network"""

    def __init__(self, id):
        self.probability = random.uniform(ini.min_probability, ini.max_probability)
        self.id = str(id)
        self.throughput = 0
        self.maxdelay = 0
        self.avdelay = 0
        self.queuesize = 0
        self.packetssent = 0
        self.totaldelays = []
        self.currentdelays = []
        self.pending = False
        self.collisions = 0
        self.backoffdelay = 0
        
    def __str__(self):
        a = "This node's statistics are the following: \n"
        b = "probability: {0}, queuesize: {1}, packetssent: {2} \n".format(self.probability, self.queuesize, self.packetssent)
        c = "totaldelays: {0},  pending: {1} \n".format(self.totaldelays, self.pending)
        d = " throughput: {0}, maxdelay: {1}, avdelay: {2} \n".format(self.throughput, self.maxdelay, self.avdelay)
        return a+b+c+d
     
    def successfulsend(self): 
        self.queuesize -= 1
        self.packetssent += 1
        self. backoffdelay = 0
        self.collisions = 0
        self.totaldelays.append(self.currentdelays[0]+1) #+1 packet time to the packet that was successfully sent
        del self.currentdelays[0]
        if (self.queuesize == 0): self.pending = False

        return 
    
    def _newpacket(self):
        if (self.probability > random.random()) :
            self.queuesize += 1
            self.pending = True
            self.currentdelays.append(0)
        return
    
    def wantstosend(self):
        self._newpacket()
        if (self.backoffdelay > 0): self.backoffdelay -= 1
        if (self.backoffdelay == 0): return self.queuesize > 0
        return False

    def _incrementdelays(self):
        if self.currentdelays == []: return
        for i in range(self.queuesize): self.currentdelays[i] += 1
        return

    def update(self):
        self._incrementdelays()
        if (self.totaldelays == []): return
        self.maxdelay = max(self.totaldelays)
        self.avdelay = sum(self.totaldelays)/len(self.totaldelays)
        self.throughput = self.packetssent / ini.time_elapsed
        return




