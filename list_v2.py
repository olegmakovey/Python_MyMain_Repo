routers = ['r1', 'r2', 'r3', 'r4', 'r5']
routers.append('r6')
print(routers)
#['r1', 'r2', 'r3', 'r4', 'r5', 'r6']
routers.insert(2, 'r100')
print(routers)
#['r1', 'r2', 'r100', 'r3', 'r4', 'r5', 'r6']
print(routers.pop(1))
#'r2'
print(routers)
#['r1', 'r100', 'r3', 'r4', 'r5', 'r6']