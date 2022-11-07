class router(object):
  def __init__(self, name, interface_number, vendor):
     self.name = name
     self.interface_number = interface_number
     self.vendor = vendor


#>>>
r1 = router("SFO1-R1", 64, "Cisco")
print(r1.name)
#'SFO1-R1'
print(r1.interface_number)
#64
print(r1.vendor)
#'Cisco'
###
r2 = router("LAX-R2", 32, "Juniper")
print(r2.name)
#'LAX-R2'
print(r2.interface_number)
#32
print(r2.vendor)
#'Juniper'
#>>>