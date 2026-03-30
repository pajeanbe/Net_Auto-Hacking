output = """Neighbor ID     Pri   State           Dead Time   Address         Interface
2.2.2.2           1   FULL/DR         00:00:32    192.168.3.2     Ethernet1/0
3.3.3.3           1   FULL/DR         00:00:36    192.168.2.6     Ethernet0/3
2.2.2.2           1   FULL/DR         00:00:34    192.168.2.2     Ethernet0/2
2.2.2.2           1   2WAY/DROTHER    00:00:37    192.168.0.2     Ethernet0/1
3.3.3.3           1   2WAY/DROTHER    00:00:36    192.168.0.3     Ethernet0/1
4.4.4.4           1   FULL/BDR        00:00:31    192.168.0.4     Ethernet0/1
192.168.0.5       1   FULL/DR         00:00:35    192.168.0.5     Ethernet0/1
2.2.2.2           1   2WAY/DROTHER    00:00:31    192.168.1.4     Ethernet0/0
3.3.3.3           1   FULL/BDR        00:00:32    192.168.1.5     Ethernet0/0
4.4.4.4           1   FULL/DR         00:00:36    192.168.1.6     Ethernet0/0
"""
#get all the router ID
router_ids = [line.split()[4] for line in output.split('\n')[2:-1]]
print(router_ids)