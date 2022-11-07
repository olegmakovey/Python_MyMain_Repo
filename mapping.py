datacenter1 = {'spines': ['r1', 'r2', 'r3', 'r4']}
datacenter1['leafs'] = ['l1', 'l2', 'l3', 'l4']
print(datacenter1)
#{'leafs': ['l1', 'l2', 'l3', 'l4'], 'spines': ['r1','r2', 'r3', 'r4']}
print(datacenter1['spines'])
#['r1', 'r2', 'r3', 'r4']
print(datacenter1['leafs'])
#['l1', 'l2', 'l3', 'l4']