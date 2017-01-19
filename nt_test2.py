import logging
from networktables import NetworkTables

logging.basicConfig(level=logging.DEBUG)




# NetworkTables.initialize("10.40.1.12")
NetworkTables.setIPAddress("roborio-4001-frc.local")
NetworkTables.setClientMode()
NetworkTables.initialize()

print(NetworkTables.ipAddress)
print(NetworkTables.port)
print(NetworkTables.isServer())
print(NetworkTables.getRemoteAddress())
print(NetworkTables.isConnected())

table = NetworkTables.getTable("datatable")
print(table.getNumber('X', 0))